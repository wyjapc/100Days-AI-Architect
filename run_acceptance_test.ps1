# 100Days-AI-Architect - Day 1 本地验收测试 (PowerShell)

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "100Days-AI-Architect - Day 1 本地验收测试" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "这个脚本将验证所有 Day 1 验收标准" -ForegroundColor Yellow
Write-Host "不需要 API Key，完全本地执行" -ForegroundColor Yellow
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

python local_acceptance_test.py

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "按任意键退出..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
