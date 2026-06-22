"""扫描 20 章对应原书中的图片资源。"""
import os
import json

CHAPTER_TO_BOOKS = {
    "01 机器学习入门":      ["pumpkin-book", "easy-rl", "leedl-tutorial", "hands-dirty-nlp", "joyful-pandas"],
    "02 线性代数":          ["math-for-ai", "pumpkin-book", "powerful-numpy"],
    "03 概率统计":          ["math-for-ai", "pumpkin-book", "statistical-learning-method-solutions-manual"],
    "04 Python与NumPy":     ["powerful-numpy", "joyful-pandas", "learn-python-the-smart-way-v2"],
    "05 数据预处理":        ["joyful-pandas", "fun-rec", "leedl-tutorial"],
    "06 线性回归":          ["pumpkin-book", "leedl-tutorial", "machine-learning-toy-code"],
    "07 逻辑回归":          ["pumpkin-book", "leedl-tutorial", "machine-learning-toy-code"],
    "08 梯度下降":          ["pumpkin-book", "leedl-tutorial"],
    "09 模型评估":          ["pumpkin-book", "leedl-tutorial"],
    "10 过拟合与正则化":    ["pumpkin-book", "leedl-tutorial", "machine-learning-toy-code"],
    "11 神经网络基础":      ["leedl-tutorial", "dive-into-bishop-dl", "udl-tutorial", "easy-nlp"],
    "12 反向传播":          ["leedl-tutorial", "pumpkin-book", "udl-tutorial"],
    "13 激活函数":          ["leedl-tutorial", "udl-tutorial", "easy-grokking-deep-learning"],
    "14 CNN":               ["leedl-tutorial", "team-learning-cv", "udl-tutorial"],
    "15 RNN与LSTM":         ["leedl-tutorial", "hands-dirty-nlp", "learn-nlp-with-transformers", "udl-tutorial"],
    "16 优化算法":          ["leedl-tutorial", "pumpkin-book", "udl-tutorial"],
    "17 批归一化与Dropout": ["leedl-tutorial", "udl-tutorial", "thorough-pytorch"],
    "18 PyTorch基础":       ["thorough-pytorch", "easy-pocket", "leedl-tutorial"],
    "19 训练技巧":          ["leedl-tutorial", "thorough-pytorch", "udl-tutorial"],
    "20 迁移学习":          ["leedl-tutorial", "thorough-pytorch", "udl-tutorial"],
}

IMG_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp")

result = {}
for ch, books in CHAPTER_TO_BOOKS.items():
    result[ch] = []
    for book in books:
        book_path = f"F:/datawhale_books/{book}"
        if not os.path.isdir(book_path):
            continue
        imgs = []
        try:
            for root, dirs, files in os.walk(book_path):
                # 跳过 .git
                dirs[:] = [d for d in dirs if d not in (".git", "node_modules")]
                for f in files:
                    if f.lower().endswith(IMG_EXT):
                        rel = os.path.relpath(os.path.join(root, f), "F:/datawhale_books")
                        imgs.append(rel)
                if len(imgs) >= 200:
                    break
        except Exception as e:
            result[ch].append((book, 0, [f"ERROR: {e}"]))
            continue
        result[ch].append((book, len(imgs), imgs[:30]))  # 最多列前 30 个示例
    # 按图片数降序
    result[ch].sort(key=lambda x: -x[1])

# 输出
for ch, books in result.items():
    print(f"\n=== {ch} ===")
    if not books:
        print("  (无候选仓库)")
        continue
    for b, n, samples in books:
        print(f"  [{b}] {n} 张")
        for s in samples[:5]:
            print(f"      {s}")
        if len(samples) > 5:
            print(f"      ... 还有 {len(samples)-5} 张示例")

# 顺便存到文件
out_path = "F:/datawhale_books/_image_inventory.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({ch: [(b, n, samples) for b, n, samples in books] for ch, books in result.items()}, f, ensure_ascii=False, indent=2)
print(f"\n\n清单已保存到: {out_path}")
