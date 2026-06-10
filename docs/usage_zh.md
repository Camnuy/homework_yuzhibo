# 使用方式

## 运行环境

建议使用 Python 3.11。

先安装依赖：

```powershell
python -m pip install -r requirements.txt
```

## 正常运行步骤

1. 生成 catalog

```powershell
python src/prepare_reference_catalog.py
```

2. 构建检索索引

```powershell
python src/build_reference_index.py
```

3. 启动 demo

```powershell
python src/demo_app.py
```

## demo 使用方法

### 图像查询

1. 打开 `Search By Image`
2. 上传一张图片
3. 点击 `Find Related References`
4. 查看相似参考图和相似度表格

### 文本 brief 查询

1. 打开 `Search By Text Brief`
2. 输入简短创作方向
3. 点击 `Search By Brief`
4. 查看返回的参考图排行
