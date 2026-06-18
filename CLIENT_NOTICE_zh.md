# 客户先看

这个 GitHub 仓库是**代码和文档版本**，不是直接双击就能使用的成品程序，也不是静态网站。

## 先说明白三件事

1. `publication` 不是图片文件夹  
   - 里面放的是项目说明文档
   - 目前只有 `.md` 文本说明文件

2. 这个仓库里没有现成网站  
   - 不存在可以直接双击打开的 `index.html`
   - 页面界面来自本地运行的 Gradio demo

3. 这个仓库也没有附带完整运行资源  
   - 没有上传本地数据集
   - 没有上传模型运行资源
   - 没有上传 Windows 可执行包

## 如果你想运行 demo

需要在本地 Python 环境中执行：

```powershell
python -m pip install -r requirements.txt
python src/prepare_reference_catalog.py
python src/build_reference_index.py
python src/demo_app.py
```

然后浏览器才会打开本地 demo 页面。

## 如果你只是想直接使用

那应该拿到的是：

1. Windows 可执行压缩包，或
2. 已经打包好的本地交付版本

而不是当前这个纯 GitHub 代码仓库。
