@echo off
chcp 65001 >nul
echo ============================================================
echo PM Agent - 使用 DeepSeek API 本地执行
echo ============================================================
echo.

REM 提示输入 DeepSeek API Key
set /p DEEPSEEK_API_KEY="请输入 DeepSeek API Key: "

if "%DEEPSEEK_API_KEY%"=="" (
    echo 错误: 未输入 API Key
    pause
    exit /b 1
)

echo.
echo ✅ API Key 已设置
echo.
echo 正在执行 PM Agent...
echo ============================================================
echo.

REM 执行脚本
python scripts/test_llm_only.py

echo.
echo ============================================================
pause
