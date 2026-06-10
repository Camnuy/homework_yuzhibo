# 使用技术

这个项目当前使用的主要技术包括：

## 核心模型

1. `CLIP`
   - 用于图像和文本 embedding
   - 支持 image-to-image 和 text-to-image retrieval

## Python 库

1. `transformers`
2. `torch`
3. `pandas`
4. `numpy`
5. `Pillow`
6. `gradio`
7. `joblib`

## 系统结构

1. 数据层：独立艺术家参考图库
2. 模型层：CLIP embedding
3. 检索层：余弦相似度排序
4. 界面层：Gradio

## 输出形式

1. 参考图 catalog
2. 索引 bundle
3. 检索评估报告
4. 可交互 demo
