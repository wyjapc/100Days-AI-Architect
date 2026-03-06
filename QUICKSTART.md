# 快速启动指南

## 🎯 当前状态

✅ 项目结构已搭建完成
✅ PM Agent 核心脚本已实现
✅ GitHub Actions 自动化流已配置
✅ 本地测试已通过

## 🚀 立即开始

### 步骤 1: 推送到 GitHub

```bash
# 如果还没有关联远程仓库
git remote add origin https://github.com/你的用户名/100Days-AI-Architect.git

# 推送代码
git push -u origin main
```

### 步骤 2: 配置 API Key（二选一）

在 GitHub 仓库页面：
1. 进入 Settings > Secrets and variables > Actions
2. 点击 "New repository secret"
3. 添加以下任一密钥：

**选项 A - OpenAI (推荐，更便宜)**
- Name: `OPENAI_API_KEY`
- Value: 你的 OpenAI API Key

**选项 B - Anthropic Claude**
- Name: `ANTHROPIC_API_KEY`
- Value: 你的 Anthropic API Key

### 步骤 3: 手动触发首次测试

1. 进入仓库的 Actions 标签页
2. 选择 "Daily PM Agent - 自动任务生成"
3. 点击 "Run workflow" 按钮
4. 等待执行完成（约 10-30 秒）

### 步骤 4: 查看结果

进入 Issues 标签页，你应该能看到：
- 标题：`Day 1 - 2026-03-06 任务看板`
- 标签：`daily-task`, `auto-generated`
- 内容：由 AI 生成的今日任务清单

## 📅 自动化执行

配置完成后，系统将：
- 每天北京时间 08:00 自动执行
- 自动读取 `tracker/template.json` 配置
- 调用 LLM 生成任务清单
- 自动创建 GitHub Issue

## 🔧 本地测试

如果想在本地测试（不创建真实 Issue）：

```bash
# 安装依赖
pip install -r scripts/requirements.txt

# 运行测试脚本
python scripts/test_pm_agent.py
```

## 📝 自定义任务

修改 `tracker/template.json` 来自定义每天的任务：

```json
{
  "day": 2,
  "date": "2026-03-07",
  "topic": "你的学习主题",
  "status": "pending",
  ...
}
```

## ❓ 常见问题

**Q: 没有 API Key 怎么办？**
A: 可以先推送代码，稍后再配置。或者使用测试脚本进行本地验证。

**Q: 如何修改执行时间？**
A: 编辑 `.github/workflows/daily_pm_agent.yml` 中的 cron 表达式。

**Q: 支持哪些 LLM？**
A: 目前支持 OpenAI (GPT-3.5) 和 Anthropic (Claude-3-Haiku)。

## 🎉 完成！

你的 100 天 AI 架构师成长计划自动化系统已经就绪！
