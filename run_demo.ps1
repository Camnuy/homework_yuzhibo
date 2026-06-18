$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonExe = "C:\Users\23913\.conda\envs\homework2\python.exe"
$DemoUrl = "http://127.0.0.1:7860"

if (-not (Test-Path $PythonExe)) {
    $PythonExe = "python"
}

Push-Location $ProjectRoot
try {
    $process = Start-Process -FilePath $PythonExe -ArgumentList "src/demo_app.py" -WorkingDirectory $ProjectRoot -PassThru
    $opened = $false

    for ($i = 0; $i -lt 30; $i++) {
        Start-Sleep -Seconds 2
        try {
            $response = Invoke-WebRequest -UseBasicParsing $DemoUrl -TimeoutSec 3
            if ($response.StatusCode -ge 200) {
                Start-Process $DemoUrl
                Write-Host "Demo is ready: $DemoUrl"
                $opened = $true
                break
            }
        }
        catch {
        }
    }

    if (-not $opened) {
        Write-Host "Demo may still be starting. Open this URL manually after a short wait:"
        Write-Host $DemoUrl
    }

    Write-Host "Server process id: $($process.Id)"
}
finally {
    Pop-Location
}
