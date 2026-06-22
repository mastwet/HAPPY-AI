"""把精选图片插入对应章节 mdx（修正 marker 版本）。"""
import os

BASE = r"C:\Users\Administrator\Documents\HAPPY-AI\content\docs"

INSERTS = [
    # 02 线性代数 — 在"张量"和"在机器学习中的应用"分别插
    ("foundations/02-linear-algebra/index.mdx", "02-matrix-decomp.png", "矩阵分解与张量变换示意", "## 张量（Tensor）"),
    ("foundations/02-linear-algebra/index.mdx", "02-svd.png",            "SVD 奇异值分解示意",     "## 在机器学习中的应用"),

    # 03 概率统计
    ("foundations/03-probability-stats/index.mdx", "03-distribution.png", "常见概率分布示意", "## 随机变量"),
    ("foundations/03-probability-stats/index.mdx", "03-bayes.png",        "贝叶斯推断示意",   "## 最大似然估计（MLE）"),

    # 08 梯度下降
    ("foundations/08-gradient-descent/index.mdx", "08-loss-surface.png",  "损失函数曲面示意", "## 梯度下降的核心思想"),
    ("foundations/08-gradient-descent/index.mdx", "08-gd-path.png",       "梯度下降路径示意", "## 三种梯度下降变体"),

    # 09 模型评估
    ("foundations/09-model-evaluation/index.mdx", "09-roc.png",            "ROC 曲线示意",    "## ROC 曲线与 AUC"),

    # 10 过拟合
    ("foundations/10-overfitting-regularization/index.mdx", "10-bias-variance.png", "偏差-方差分解示意", "## 其他防止过拟合的方法"),
    ("foundations/10-overfitting-regularization/index.mdx", "10-overfit.png",       "过拟合与欠拟合对比", "## 什么是过拟合"),

    # 13 激活函数
    ("deep-learning/13-activation-functions/index.mdx", "13-activation-curves.png", "激活函数曲线对比", "## 激活函数对比"),

    # 14 CNN
    ("deep-learning/14-cnn/index.mdx", "14-network-arch.png", "网络架构示意", "## 卷积操作"),
]


def find_insertion_point(text, marker):
    lines = text.splitlines(keepends=True)
    marker_idx = None
    for i, line in enumerate(lines):
        if line.strip() == marker.strip():
            marker_idx = i
            break
    if marker_idx is None:
        return None
    # marker 标题之后，下一个 ## 标题之前
    insert_idx = None
    for j in range(marker_idx + 1, len(lines)):
        if lines[j].startswith("## "):
            insert_idx = j
            break
    if insert_idx is None:
        insert_idx = len(lines)
    return insert_idx


for rel, img, title, marker in INSERTS:
    mdx_path = os.path.join(BASE, rel)
    if not os.path.exists(mdx_path):
        print(f"❌ MISS: {mdx_path}")
        continue
    with open(mdx_path, "r", encoding="utf-8") as f:
        text = f.read()
    if f"/images/{img}" in text:
        print(f"⏭️  SKIP: {rel} <- {img}")
        continue
    idx = find_insertion_point(text, marker)
    if idx is None:
        print(f"❌ MARKER MISS: {rel} <- '{marker}'")
        continue
    lines = text.splitlines(keepends=True)
    img_md = f"\n![{title}](/images/{img})\n\n*{title}*\n\n"
    lines.insert(idx, img_md)
    new_text = "".join(lines)
    with open(mdx_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"✅ {rel:60s} <- {img}")

print("\n完成。")
