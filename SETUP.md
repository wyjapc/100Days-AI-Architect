# 配置指南

## 1. 配置 GitHub Secrets

在仓库的 Settings > Secrets and variables > Actions 中添加：

### 必需配置（三选一）

**选项 A: 使用 DeepSeek（推荐，最便宜）**
- `DEEPSEEK_API_KEY`: 你的 DeepSeek API Key
- 获取地址: https://platform.deepseek.com/api_keys

**选项 B: 使用 OpenAI**
- `OPENAI_API_KEY`: 你的 OpenAI API Key

**选项 C: 使用 Anthropic Claude**
- `ANTHROPIC_API_KEY`: 你的 Anthropic API Key

### 自动配置

- `GITHUB_TOKEN`: 无需手动配置，GitHub Actions 自动提供

## 2. 手动测试

本地测试脚本：

```bash
# 设置环境变量（Windows CMD）
set DEEPSEEK_API_KEY=your-key-here
set GH_TOKEN=your-github-token
set GITHUB_REPOSITORY=username/100Days-AI-Architect

# 或使用 PowerShell
$env:DEEPSEEK_API_KEY="your-key-here"
$env:GH_TOKEN="your-github-token"
$env:GITHUB_REPOSITORY="username/100Days-AI-Architect"

# 安装依赖
pip install -r scripts/requirements.txt

# 运行脚本
python scripts/pm_agent_init.py
```

## 3. 手动触发 Workflow

在 GitHub 仓库页面：
1. 进入 Actions 标签页
2. 选择 "Daily PM Agent - 自动任务生成"
3. 点击 "Run workflow" 按钮
4. 查看 Issues 面板确认任务已创建

## 4. 定时执行

Workflow 已配置为每天 UTC 00:00（北京时间 08:00）自动执行。

## 5. 自定义配置

修改 `tracker/template.json` 中的字段来自定义当天的任务主题和参数。
