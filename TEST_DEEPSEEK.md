# DeepSeek API 测试指南

## 🚀 快速开始

### 方法 1: 使用批处理脚本（推荐）

双击运行 `run_with_deepseek.bat` 或 `run_with_deepseek.ps1`，按提示输入 API Key。

### 方法 2: 命令行执行

**Windows CMD:**
```cmd
set DEEPSEEK_API_KEY=sk-your-key-here
python scripts/test_llm_only.py
```

**PowerShell:**
```powershell
$env:DEEPSEEK_API_KEY="sk-your-key-here"
python scripts/test_llm_only.py
```

## 📋 获取 DeepSeek API Key

1. 访问: https://platform.deepseek.com/
2. 注册/登录账号
3. 进入 API Keys 页面: https://platform.deepseek.com/api_keys
4. 创建新的 API Key
5. 复制 Key（格式: sk-...）

## 💰 价格优势

DeepSeek 是目前最便宜的高质量 LLM API：
- deepseek-chat: ¥1/百万 tokens（输入）
- 比 GPT-3.5 便宜约 10 倍
- 比 Claude 便宜约 50 倍

## ✅ 测试流程

脚本会：
1. 读取 `tracker/template.json` 配置
2. 读取 `prompts/pm_agent_system.md` 提示词
3. 调用 DeepSeek API 生成任务清单
4. 显示生成的内容
5. 保存到 `tracker/day-1-output.md`

## 🔍 验证结果

执行成功后，检查：
- 终端输出的任务清单
- `tracker/day-1-output.md` 文件内容

## ❓ 常见问题

**Q: API Key 无效？**
A: 确认 Key 格式正确（sk-开头），且账户有余额。

**Q: 网络连接失败？**
A: 检查网络连接，DeepSeek API 地址: https://api.deepseek.com

**Q: 想要创建 GitHub Issue？**
A: 使用 `python scripts/pm_agent_init.py`，需额外配置 GH_TOKEN。
