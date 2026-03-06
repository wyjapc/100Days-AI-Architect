@echo off
chcp 65001 >nul
echo ============================================================
echo 创建 Day 1 任务看板 - GitHub Issue
echo ============================================================
echo.
echo 这个脚本将帮助你完成 Day 1 的最后验收标准：
echo 在 GitHub Issues 中创建由 AI 生成的任务看板
echo.
echo 需要准备：
echo 1. DeepSeek API Key (推荐) 或 OpenAI/Anthropic API Key
echo 2. GitHub Personal Access Token
echo.
echo ============================================================
echo.

python create_first_issue.py

echo.
pause
