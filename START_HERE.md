# 🎯 立即开始测试

## 最快的测试方法（使用 DeepSeek API）

### 步骤 1: 获取 DeepSeek API Key（2 分钟）

1. 访问: https://platform.deepseek.com/api_keys
2. 注册/登录
3. 创建 API Key
4. 复制 Key（格式: sk-...）

💰 DeepSeek 价格: ¥1/百万 tokens，是最便宜的选择！

### 步骤 2: 运行测试（1 分钟）

**方法 A - 双击运行（最简单）:**
- Windows: 双击 `run_with_deepseek.bat`
- PowerShell: 右键 `run_with_deepseek.ps1` → "使用 PowerShell 运行"

**方法 B - 命令行:**
```powershell
$env:DEEPSEEK_API_KEY="你的-API-Key"
python scripts/test_llm_only.py
```

### 步骤 3: 查看结果

- 终端会显示 AI 生成的任务清单
- 结果保存在 `tracker/day-1-output.md`

---

## 📊 当前项目状态

✅ 代码已推送到 GitHub
✅ 支持 DeepSeek/OpenAI/Anthropic 三种 API
✅ 本地测试脚本已就绪
✅ GitHub Actions 自动化已配置

---

## 🚀 完整功能测试（可选）

如果想测试完整的 GitHub Issue 自动创建功能：

1. 获取 GitHub Token: https://github.com/settings/tokens
2. 运行完整脚本:
```powershell
$env:DEEPSEEK_API_KEY="你的-DeepSeek-Key"
$env:GH_TOKEN="你的-GitHub-Token"
$env:GITHUB_REPOSITORY="wyjapc/100Days-AI-Architect"
python scripts/pm_agent_init.py
```

---

## 📚 更多文档

- `TEST_DEEPSEEK.md` - DeepSeek 详细测试指南
- `QUICKSTART.md` - 快速启动指南
- `SETUP.md` - 完整配置说明
- `NEXT_STEPS.md` - GitHub 配置步骤

---

## ❓ 需要帮助？

遇到问题？检查：
1. Python 是否已安装（`python --version`）
2. requests 库是否已安装（`pip install requests`）
3. API Key 格式是否正确（sk-开头）
4. 网络连接是否正常
