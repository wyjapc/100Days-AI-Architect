# PM Agent - 使用 DeepSeek API 本地执行 (PowerShell)

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "PM Agent - 使用 DeepSeek API 本地执行" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# 提示输入 DeepSeek API Key
$apiKey = Read-Host "请输入 DeepSeek API Key"

if ([string]::IsNullOrWhiteSpace($apiKey)) {
    Write-Host "错误: 未输入 API Key" -ForegroundColor Red
    exit 1
}

# 设置环境变量
$env:DEEPSEEK_API_KEY = $apiKey

Write-Host ""
Write-Host "✅ API Key 已设置" -ForegroundColor Green
Write-Host ""
Write-Host "正在执行 PM Agent..." -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# 执行脚本
python scripts/test_llm_only.py

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "按任意键退出..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
