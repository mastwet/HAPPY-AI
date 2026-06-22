"""第二阶段：从原书 md 中提取所有图片引用（带上下文），按 20 章主题筛选。"""
import os
import re
import json

CHAPTER_TOPICS = {
    "01 机器学习入门":      ["机器学习", "监督", "无监督", "分类", "回归", "决策树"],
    "02 线性代数":          ["线性代数", "向量", "矩阵", "张量", "特征值", "范数", "内积", "点积", "外积"],
    "03 概率统计":          ["概率", "统计", "贝叶斯", "分布", "期望", "方差", "高斯", "正态"],
    "04 Python与NumPy":     ["numpy", "python", "数组", "广播", "向量化"],
    "05 数据预处理":        ["数据", "预处理", "缺失", "异常", "归一化", "标准化", "特征工程", "pandas"],
    "06 线性回归":          ["线性回归", "最小二乘", "正规方程", "梯度下降线性"],
    "07 逻辑回归":          ["逻辑回归", "对数几率", "sigmoid分类", "梯度下降逻辑"],
    "08 梯度下降":          ["梯度下降", "批量", "随机梯度", "学习率", "sgd", "动量"],
    "09 模型评估":          ["评估", "roc", "auc", "混淆矩阵", "准确率", "召回", "f1", "交叉验证"],
    "10 过拟合与正则化":    ["过拟合", "欠拟合", "正则化", "L1", "L2", "Dropout", "早停"],
    "11 神经网络基础":      ["神经网络", "感知机", "MLP", "神经元", "激活", "前向", "隐藏层"],
    "12 反向传播":          ["反向传播", "BP", "梯度反向", "链式法则"],
    "13 激活函数":          ["激活函数", "sigmoid", "tanh", "relu", "leaky", "softmax"],
    "14 CNN":               ["CNN", "卷积", "卷积神经网络", "池化", "滤波器", "特征图"],
    "15 RNN与LSTM":         ["RNN", "LSTM", "GRU", "循环", "序列", "门控", "时间步"],
    "16 优化算法":          ["Adam", "RMSprop", "Momentum", "优化器", "自适应", "学习率衰减"],
    "17 批归一化与Dropout": ["批归一化", "BatchNorm", "LayerNorm", "Dropout", "归一化"],
    "18 PyTorch基础":       ["PyTorch", "Tensor", "Dataset", "DataLoader", "nn.Module", "自动求导"],
    "19 训练技巧":          ["训练技巧", "学习率调度", "warmup", "数据增强", "梯度裁剪", "早停"],
    "20 迁移学习":          ["迁移学习", "预训练", "微调", "fine-tune", "特征提取", "冻结"],
}

# 候选原书 -> 关注的章节目录前缀
BOOK_FOCUS = {
    "pumpkin-book":          ["docs/chapter1", "docs/chapter2", "docs/chapter3", "docs/chapter4", "docs/chapter5", "docs/chapter6", "docs/chapter7", "docs/chapter8", "docs/chapter9", "docs/chapter10", "docs/chapter11"],
    "leedl-tutorial":        ["docs", "笔记＆勘误", "notes"],
    "udl-tutorial":          ["docs"],
    "math-for-ai":           ["docs"],
    "powerful-numpy":        ["docs", "src"],
    "thorough-pytorch":      ["docs"],
    "fun-rec":               ["docs"],
    "machine-learning-toy-code": [""],
    "joyful-pandas":         ["docs"],
    "easy-rl":               ["docs"],
    "easy-nlp":              ["docs"],
    "easy-grokking-deep-learning": ["docs"],
    "team-learning-cv":      [""],
    "learn-nlp-with-transformers": ["docs"],
    "dive-into-bishop-dl":   ["docs"],
    "hands-dirty-nlp":       [""],
    "statistical-learning-method-solutions-manual": ["docs"],
    "learn-python-the-smart-way-v2": ["docs"],
    "easy-pocket":           ["docs"],
}

# md 图片引用正则（支持 ![alt](path) 和 <img src=...>）
MD_IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_IMG_RE = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"']", re.IGNORECASE)

def extract_images_from_md(md_path):
    """从单个 md 文件中提取 (alt, src) 列表"""
    try:
        with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except Exception:
        return []
    results = []
    for alt, src in MD_IMG_RE.findall(text):
        results.append((alt, src))
    for src in HTML_IMG_RE.findall(text):
        results.append(("", src))
    return results

def chapter_score(text, topics):
    """简单打分：章节文本含多少相关关键词"""
    text_lower = text.lower()
    score = 0
    matched = []
    for t in topics:
        if t.lower() in text_lower:
            score += 1
            matched.append(t)
    return score, matched

def is_content_md(path, book_focus):
    """判断 md 是否在候选目录范围内"""
    if not book_focus:
        return True
    rel = path.lower()
    return any(focus.lower() in rel for focus in book_focus if focus)

results = {}
BASE = "F:/datawhale_books"

for ch, topics in CHAPTER_TOPICS.items():
    ch_result = {"images": [], "matched_files": 0}
    for book, focus_dirs in BOOK_FOCUS.items():
        book_path = f"{BASE}/{book}"
        if not os.path.isdir(book_path):
            continue
        # 找该书所有 md
        for root, dirs, files in os.walk(book_path):
            dirs[:] = [d for d in dirs if d not in (".git", "node_modules")]
            for f in files:
                if not (f.endswith(".md") or f.endswith(".mdx")):
                    continue
                full = os.path.join(root, f)
                if not is_content_md(full, focus_dirs):
                    continue
                imgs = extract_images_from_md(full)
                if not imgs:
                    continue
                # 读全文打分
                try:
                    with open(full, "r", encoding="utf-8", errors="ignore") as fp:
                        text = fp.read()[:8000]  # 只看前 8KB 决定是否相关
                except Exception:
                    continue
                score, matched = chapter_score(text, topics)
                if score == 0:
                    continue
                ch_result["matched_files"] += 1
                # 收集本文件的图片
                for alt, src in imgs:
                    # src 可能是相对路径或 http
                    if src.startswith("http") or src.startswith("data:"):
                        continue
                    if not src or src.endswith(".git"):
                        continue
                    ch_result["images"].append({
                        "book": book,
                        "md_file": os.path.relpath(full, BASE).replace("\\", "/"),
                        "alt": alt[:100],
                        "src": src,
                        "score": score,
                        "matched_keywords": matched,
                    })
    # 按 score 降序
    ch_result["images"].sort(key=lambda x: -x["score"])
    # 限制每章最多 30 张候选
    ch_result["images"] = ch_result["images"][:30]
    results[ch] = ch_result

# 打印汇总
print("=" * 80)
total = 0
for ch, data in results.items():
    print(f"\n## {ch}  — 匹配 {data['matched_files']} 个原书文件，候选图 {len(data['images'])} 张")
    for img in data["images"][:8]:
        print(f"  [{img['book']:30s}] score={img['score']:2d} kws={img['matched_keywords']}")
        print(f"     alt: {img['alt']}")
        print(f"     src: {img['src']}")
        print(f"     in : {img['md_file']}")
    if len(data["images"]) > 8:
        print(f"  ... +{len(data['images'])-8} 更多")
    total += len(data["images"])

print(f"\n\n=== 总计候选图：{total} 张（每章前 30）===")

# 保存
out = "F:/datawhale_books/_image_refs.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"详细清单: {out}")
