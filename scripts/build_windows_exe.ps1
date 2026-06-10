$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$PythonExe = "C:\Users\23913\.conda\envs\homework2\python.exe"
$ModelSource = "D:\homework_yibai\_shared_runtime_assets\clip-vit-base-patch32-pytorch"
$DistRoot = Join-Path $ProjectRoot "release\windows"
$BuildRoot = Join-Path $ProjectRoot "build"
$SpecPath = Join-Path $ProjectRoot "homework_nan_windows.spec"

if (-not (Test-Path $PythonExe)) {
    throw "Python executable not found: $PythonExe"
}

if (-not (Test-Path $ModelSource)) {
    throw "Model assets not found: $ModelSource"
}

New-Item -ItemType Directory -Force -Path $DistRoot | Out-Null
New-Item -ItemType Directory -Force -Path $BuildRoot | Out-Null

Push-Location $ProjectRoot
try {
    & $PythonExe -m PyInstaller `
        --noconfirm `
        --clean `
        --onedir `
        --name "homework_nan_windows" `
        --distpath $DistRoot `
        --workpath $BuildRoot `
        --specpath $ProjectRoot `
        --paths (Join-Path $ProjectRoot "src") `
        --add-data "$ProjectRoot\data;data" `
        --add-data "$ProjectRoot\artifacts;artifacts" `
        --add-data "$ModelSource;models\clip-vit-base-patch32" `
        --collect-all gradio `
        --collect-all gradio_client `
        --collect-all groovy `
        --collect-all safehttpx `
        --collect-all sklearn `
        --collect-all transformers `
        --collect-all tokenizers `
        src\demo_app.py
}
finally {
    Pop-Location
}

Write-Host "Windows executable package created under $DistRoot"
