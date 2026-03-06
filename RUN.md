# 🚀 执行 Day 1 验收

## 当前状态

✅ 仓库建立且包含规范目录
✅ template.json 数据契约文件已提交
⏳ 创建 GitHub Issue（最后一步）

## 执行方法

### 方法 1: 使用环境变量（推荐）

**PowerShell:**
```powershell
$env:DEEPSEEK_API_KEY = "sk-your-key"
$env:GH_TOKEN = "ghp-your-token"
$env:GITHUB_REPOSITORY = "wyjapc/100Days-AI-Architect"
python scripts/pm_agent_init.py
```

**CMD:**
```cmd
set DEEPSEEK_API_KEY=sk-your-key
set GH_TOKEN=ghp-your-token
set GITHUB_REPOSITORY=wyjapc/100Days-AI-Architect
python scripts/pm_agent_init.py
```

### 方法 2: 直接运行（需要配置环境变量）

```bash
python scripts/pm_agent_init.py
```

## 需要准备

1. **DeepSeek API Key**: https://platform.deepseek.com/api_keys
2. **GitHub Token**: https://github.com/settings/tokens（勾选 repo 权限）

## 执行后

访问: https://github.com/wyjapc/100Days-AI-Architect/issues

你会看到由 AI 生成的 "Day 1 任务看板"。
