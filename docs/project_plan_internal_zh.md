# EMI Final Project Plan

## 项目名称

**艺术家风格检索与参考板工具**  
Artist Style Retrieval and Reference Board Tool

## 一、项目定位

这个项目的定位是一个**面向创作者的视觉参考检索系统**。

它和分类项目不一样，主问题不是：

- 这张图属于哪一类

而是：

- 这张图和哪些参考作品在视觉上更接近
- 某个创作 brief 更适合匹配哪些参考图

所以这项目的主线应该定义成：

**retrieval / recommendation / reference-board building**

## 二、核心研究问题

建议统一成下面这个版本：

> How can a machine-learning retrieval system help creators find visually related references and build moodboards for a creative brief?

中文可写成：

> 一个机器学习检索系统能否帮助创作者找到视觉上更接近的参考图，并据此构建更有方向感的 moodboard？

## 三、项目目标

最终要完成的不是“分类准确率”，而是：

1. 建立一个可查询的参考图库
2. 让用户能用图像或文本 brief 搜索参考图
3. 返回排序后的候选结果
4. 讨论算法相似性与创作判断之间的关系

当前为了和另一个项目彻底拉开，`homework_nan` 的数据必须保持为**独立艺术家参考库**，不复用 `homework女` 的任何图片。

## 四、最终交付物

按照课程要求，最后应包含：

1. GitHub repo
2. README
3. weblog
4. 数据来源说明
5. 图像索引构建代码
6. 检索评估脚本
7. Gradio demo
8. 3-5 分钟视频

## 五、技术主线

### Stage 1: Reference library preparation

1. 准备一批艺术和设计参考图
2. 记录来源、标题、作者、风格提示词
3. 建立 catalog

当前初版的独立数据路线：

1. `monet`
2. `vangogh`
3. `hokusai`
4. `klimt`

### Stage 2: Embedding index

1. 使用 CLIP 提取图像 embedding
2. 保存参考图库 embedding
3. 建立可复用的索引文件

### Stage 3: Retrieval

1. 支持 image-to-image retrieval
2. 支持 text-to-image retrieval
3. 返回 top-k 排序结果

### Stage 4: Evaluation

1. 用 starter 指标检查相关结果是否排在前面
2. 做若干 query case study
3. 记录成功和失败案例

### Stage 5: Demo

1. 用户上传查询图像
2. 或输入创作 brief
3. 输出检索结果和相似度信息

## 六、与分类项目的区别

这个项目必须在叙事上明确区别于 `homework女`：

### `homework_nan`

- 核心任务：检索和排序
- 输出重点：top-k 参考图
- 项目身份：创意搜索工具

### `homework女`

- 核心任务：风格分类
- 输出重点：标签、置信度、混淆矩阵
- 项目身份：主观审美判断实验

并且两边数据也要完全不同：

- `homework_nan` 使用命名艺术家参考库
- `homework女` 使用自定义视觉风格分类数据集

## 七、推荐展示重点

README 和视频里重点展示：

1. 查询图片
2. 查询 brief
3. 返回的参考图排行
4. 对结果的解释
5. 算法推荐的局限

## 八、批判性反思

这项目很适合写下面这些问题：

1. 图像“相似”到底是视觉相似、文化相似，还是语义相似？
2. 算法是否只是在放大数据集中已有的风格偏好？
3. 如果创作者长期依赖推荐系统，会不会被它反向塑造审美？
4. 机器学习检索是否会让灵感搜索更高效，但也更趋同？

## 九、当前初版完成标准

初版至少要有：

1. 小型参考图库
2. catalog 文件
3. embedding 索引脚本
4. retrieval evaluation 脚本
5. Gradio demo
6. README 和 weblog 草稿

## 十、一句话定位

> This project develops a CLIP-based reference retrieval tool that helps creators search for visually related artworks and build moodboards, while critically reflecting on how algorithmic similarity shapes creative research.
