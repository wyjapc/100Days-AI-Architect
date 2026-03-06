# 创建 Day 1 任务看板 - GitHub Issue (PowerShell)

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "创建 Day 1 任务看板 - GitHub Issue" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "这个脚本将帮助你完成 Day 1 的最后验收标准：" -ForegroundColor Yellow
Write-Host "在 GitHub Issues 中创建由 AI 生成的任务看板" -ForegroundColor Yellow
Write-Host ""
Write-Host "需要准备：" -ForegroundColor Green
Write-Host "1. DeepSeek API Key (推荐) 或 OpenAI/Anthropic API Key"
Write-Host "2. GitHub Personal Access Token"
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

python create_first_issue.py

Write-Host ""
Write-Host "按任意键退出..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
