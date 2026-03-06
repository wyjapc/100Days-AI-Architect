@echo off
chcp 65001 >nul
title 创建 Day 1 任务看板
cls
echo.
echo ============================================================
echo 🎯 准备创建 Day 1 任务看板
echo ============================================================
echo.
echo 这是完成 Day 1 验收标准的最后一步！
echo.
echo 按任意键开始...
pause >nul
cls

python create_issue_now.py

echo.
echo ============================================================
pause
