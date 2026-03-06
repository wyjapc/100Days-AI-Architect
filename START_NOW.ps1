# 创建 Day 1 任务看板 (PowerShell)

Clear-Host
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🎯 准备创建 Day 1 任务看板" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "这是完成 Day 1 验收标准的最后一步！" -ForegroundColor Yellow
Write-Host ""
Write-Host "按任意键开始..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
Clear-Host

python create_issue_now.py

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "按任意键退出..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
