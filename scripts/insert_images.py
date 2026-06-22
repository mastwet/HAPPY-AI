"""把精选图片插入对应章节 mdx。"""
import os
import re

BASE = r"C:\Users\Administrator\Documents\HAPPY-AI\content\docs"

# 章节 -> (mdx 路径, [(图片, 插入位置标记, 标题)])
# 插入位置标记：在包含该文本的最近标题之后插入
INSERTS = [
    # 02 线性代数
    ("foundations/02-linear-algebra/index.mdx", "02-matrix-decomp.png", "矩阵分解示意", "## 特征值与特征向量"),
    ("foundations/02-linear-algebra/index.mdx", "02-svd.png",            "SVD 分解示意", "## 奇异值分解 (SVD)"),

    # 03 概率统计
    ("foundations/03-probability-stats/index.mdx", "03-distribution.png", "常见概率分布", "## 常见概率分布"),
    ("foundations/03-probability-stats/index.mdx", "03-bayes.png",        "贝叶斯推断示意", "## 贝叶斯定理"),

    # 06 线性回归
    ("foundations/06-linear-regression/index.mdx", "06-linear-fit.png",   "线性回归拟合示意", "## 线性回归模型"),
    ("foundations/06-linear-regression/index.mdx", "06-residual.png",     "残差示意", "## 损失函数"),

    # 08 梯度下降
    ("foundations/08-gradient-descent/index.mdx", "08-loss-surface.png",  "损失函数曲面示意", "## 梯度下降的直观理解"),
    ("foundations/08-gradient-descent/index.mdx", "08-gd-path.png",       "梯度下降路径示意", "## 梯度下降算法"),

    # 09 模型评估
    ("foundations/09-model-evaluation/index.mdx", "09-roc.png",            "ROC 曲线示意", "## ROC 与 AUC"),

    # 10 过拟合
    ("foundations/10-overfitting-regularization/index.mdx", "10-bias-variance.png", "偏差-方差分解示意", "## 偏差-方差权衡"),
    ("foundations/10-overfitting-regularization/index.mdx", "10-overfit.png",       "过拟合 vs 欠拟合", "## 过拟合与欠拟合"),

    # 11 神经网络
    ("deep-learning/11-neural-networks/index.mdx", "11-mlp.png",          "MLP 结构示意", "## 神经网络与逻辑回归的关系"),
    ("deep-learning/11-neural-networks/index.mdx", "11-perceptron.png",   "感知机结构",   "## 感知机（Perceptron）"),

    # 13 激活函数
    ("deep-learning/13-activation-functions/index.mdx", "13-activation-curves.png", "激活函数曲线对比", "## 常见激活函数对比"),

    # 14 CNN
    ("deep-learning/14-cnn/index.mdx", "14-network-arch.png", "网络架构示意", "## 卷积运算"),
]


def find_insertion_point(text, marker):
    """找到 marker 标题所在行，在该标题的下一个 ## 之前插入"""
    lines = text.splitlines(keepends=True)
    marker_idx = None
    for i, line in enumerate(lines):
        if line.strip() == marker.strip() or line.strip().startswith(marker.strip()):
            marker_idx = i
            break
    if marker_idx is None:
        return None
    # 找 marker 之后的下一个 ## 标题位置
    insert_idx = None
    for j in range(marker_idx + 1, len(lines)):
        if lines[j].startswith("## "):
            insert_idx = j
            break
    if insert_idx is None:
        insert_idx = len(lines)
    return insert_idx


def make_image_md(filename, title):
    return f"\n![{title}](/images/{filename})\n\n*{title}*\n\n"


for rel, img, title, marker in INSERTS:
    mdx_path = os.path.join(BASE, rel)
    if not os.path.exists(mdx_path):
        print(f"❌ MISS: {mdx_path}")
        continue
    with open(mdx_path, "r", encoding="utf-8") as f:
        text = f.read()
    # 防重复
    if f"/images/{img}" in text:
        print(f"⏭️  SKIP (already inserted): {rel} <- {img}")
        continue
    idx = find_insertion_point(text, marker)
    if idx is None:
        print(f"❌ MARKER NOT FOUND: {rel} <- marker='{marker}'")
        continue
    lines = text.splitlines(keepends=True)
    # MDX 风格插入：使用普通 markdown 图片 + 居中段落
    img_md = f"\n![{title}](/images/{img})\n\n*{title}*\n\n"
    lines.insert(idx, img_md)
    new_text = "".join(lines)
    with open(mdx_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"✅ {rel:60s} <- {img}")

print("\n完成。")
