# 100Days-AI-Architect

100天 AI 架构师成长计划 - 自动化任务追踪系统

## 项目结构

```
/prompts          # Agent 提示词版本控制
/src              # 工程代码
/tracker          # 每日结构化学习记录
/scripts          # 自动化脚本
/.github/workflows # GitHub Actions 自动化流
```

## 快速开始

1. 配置环境变量（在 GitHub Secrets 中设置）：
   - `DEEPSEEK_API_KEY`（推荐）、`OPENAI_API_KEY` 或 `ANTHROPIC_API_KEY`
   - `GH_TOKEN` (GitHub Personal Access Token)

2. 系统将每天自动创建当日任务 Issue

## 数据契约

参见 `/tracker/template.json` 了解每日记录的标准格式。
