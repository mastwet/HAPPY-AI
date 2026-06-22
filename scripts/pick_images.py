"""把精选的原书图片复制到 HAPPY-AI/public/images/ 下，按章节命名。"""
import shutil
import os
import json

# 精选清单：(源路径, 目标文件名, 章节, 用途描述)
PICK = [
    # 02 线性代数
    (r"F:\datawhale_books\math-for-ai\docs\attachments\10.4.png",  "02-matrix-decomp.png",   "02 线性代数", "矩阵分解/特征向量示意"),
    (r"F:\datawhale_books\math-for-ai\docs\attachments\10.5.png",  "02-svd.png",             "02 线性代数", "SVD 分解示意"),
    # 03 概率统计
    (r"F:\datawhale_books\math-for-ai\docs\attachments\6.8.png",   "03-distribution.png",    "03 概率统计", "概率分布示意"),
    (r"F:\datawhale_books\math-for-ai\docs\attachments\6.9.png",   "03-bayes.png",           "03 概率统计", "贝叶斯推断示意"),
    # 06 线性回归
    (r"F:\datawhale_books\math-for-ai\docs\ch2\attachments\2-1.png", "06-linear-fit.png",   "06 线性回归", "线性回归拟合示意"),
    (r"F:\datawhale_books\math-for-ai\docs\ch2\attachments\2-2.png", "06-residual.png",     "06 线性回归", "残差/误差示意"),
    # 08 梯度下降
    (r"F:\datawhale_books\statistical-learning-method-solutions-manual\docs\images\25-1.png", "08-loss-surface.png",  "08 梯度下降", "损失函数曲面"),
    (r"F:\datawhale_books\statistical-learning-method-solutions-manual\docs\images\25-4.png", "08-gd-path.png",       "08 梯度下降", "梯度下降路径"),
    # 09 模型评估
    (r"F:\datawhale_books\statistical-learning-method-solutions-manual\docs\chapter06\output_25_0.png", "09-roc.png",   "09 模型评估", "ROC 曲线"),
    # 10 过拟合
    (r"F:\datawhale_books\math-for-ai\docs\attachments\8.5.png",   "10-bias-variance.png",   "10 过拟合",   "偏差-方差示意"),
    (r"F:\datawhale_books\math-for-ai\docs\attachments\8.6.png",   "10-overfit.png",         "10 过拟合",   "过拟合/欠拟合"),
    # 11 神经网络
    (r"F:\datawhale_books\easy-rl\docs\img\ch13\13.1.png",          "11-mlp.png",            "11 神经网络", "MLP 结构示意"),
    (r"F:\datawhale_books\easy-rl\docs\img\ch13\13.2.png",          "11-perceptron.png",     "11 神经网络", "感知机结构"),
    # 14 CNN
    (r"F:\datawhale_books\learn-nlp-with-transformers\docs\篇章1-前言\pictures\0-1-transformer-arc.png", "14-network-arch.png", "14 CNN", "网络架构示意"),
    # 13 激活函数
    (r"F:\datawhale_books\statistical-learning-method-solutions-manual\docs\images\25-6.png", "13-activation-curves.png", "13 激活函数", "激活函数曲线对比"),
]

DEST_DIR = r"C:\Users\Administrator\Documents\HAPPY-AI\public\images"
os.makedirs(DEST_DIR, exist_ok=True)

log = []
for src, dst_name, ch, desc in PICK:
    if not os.path.exists(src):
        log.append(f"❌ MISS: {src}")
        continue
    dst = os.path.join(DEST_DIR, dst_name)
    shutil.copy2(src, dst)
    size_kb = os.path.getsize(dst) / 1024
    log.append(f"✅ {ch:14s} {dst_name:30s} {size_kb:6.1f}KB  {desc}")

for line in log:
    print(line)

# 写出 manifest
manifest_path = os.path.join(DEST_DIR, "_manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump([{"src": s, "dst": d, "ch": c, "desc": desc} for s, d, c, desc in PICK], f, ensure_ascii=False, indent=2)
print(f"\nmanifest: {manifest_path}")
