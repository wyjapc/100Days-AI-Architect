# 🎬 演示：如何使用 DeepSeek API 运行 PM Agent

## 准备工作

✅ Python 3.13.1 已安装
✅ requests 库已安装
✅ 所有脚本已就绪

## 现在开始测试！

### 选项 1: 使用批处理脚本（推荐）

1. 双击 `run_with_deepseek.bat` 或 `run_with_deepseek.ps1`
2. 输入你的 DeepSeek API Key
3. 等待 AI 生成任务清单
4. 查看结果

### 选项 2: 使用 PowerShell 命令

打开 PowerShell，执行：

\`\`\`powershell
# 设置 API Key
$env:DEEPSEEK_API_KEY="sk-your-key-here"

# 运行测试
python scripts/test_llm_only.py
\`\`\`

### 选项 3: 交互式输入

直接运行脚本，它会提示你输入 API Key：

\`\`\`powershell
python scripts/test_llm_only.py
\`\`\`

## 预期输出

\`\`\`
============================================================
PM Agent - LLM 测试（不创建 GitHub Issue）
============================================================

📄 加载配置...
   Day: 1
   Date: 2026-03-06
   Topic: 搭建自动化追踪系统 MVP

📝 加载系统提示词...
   提示词长度: 462 字符

🚀 调用 LLM API...
🤖 正在调用 DeepSeek API (deepseek-chat)...

============================================================
✅ LLM 响应成功！
============================================================

生成的任务清单:

## Day 1 - 搭建自动化追踪系统 MVP

**日期**: 2026-03-06
**状态**: in-progress

### 今日任务清单

- [ ] 任务 1：完成 GitHub 仓库初始化，建立核心目录结构
- [ ] 任务 2：实现 PM Agent 核心脚本，支持多种 LLM API
- [ ] 任务 3：配置 GitHub Actions Workflow
- [ ] 任务 4：本地测试验证
- [ ] 任务 5：推送代码并触发首次自动化

### 验收标准
...

============================================================

💾 任务清单已保存到: tracker/day-1-output.md
\`\`\`

## 下一步

测试成功后，你可以：

1. 查看生成的文件 `tracker/day-1-output.md`
2. 配置 GitHub Secrets 启用自动化
3. 修改 `tracker/template.json` 自定义明天的任务
4. 运行完整脚本创建 GitHub Issue

## 获取 DeepSeek API Key

如果还没有 API Key：
1. 访问: https://platform.deepseek.com/api_keys
2. 注册账号（支持国内手机号）
3. 创建 API Key
4. 充值少量金额即可开始使用（非常便宜）

---

**准备好了吗？现在就运行 `run_with_deepseek.bat` 开始测试！** 🚀
