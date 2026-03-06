# 📝 创建第一个 GitHub Issue - 完整指南

## 🎯 目标

完成 Day 1 的最后验收标准：
- 在 GitHub Issues 面板中看到由 API 自动创建的"Day 1 任务看板"
- 看板内包含大模型生成的 Checklist

---

## 📋 准备工作

### 1. 获取 DeepSeek API Key（推荐）

**步骤**:
1. 访问: https://platform.deepseek.com/
2. 注册/登录账号（支持国内手机号）
3. 进入 API Keys 页面: https://platform.deepseek.com/api_keys
4. 点击"创建新密钥"
5. 复制生成的 Key（格式: sk-...）
6. 充值少量金额（¥10 足够用很久）

**为什么选择 DeepSeek?**
- 价格最便宜: ¥1/百万 tokens
- 质量优秀: 媲美 GPT-3.5
- 国内访问: 速度快，无需代理
- 100 天总成本: < ¥1

### 2. 获取 GitHub Personal Access Token

**步骤**:
1. 访问: https://github.com/settings/tokens
2. 点击 "Generate new token" → "Generate new token (classic)"
3. 设置名称: `100Days-AI-Architect`
4. 选择权限: 勾选 `repo` (完整仓库访问)
5. 点击 "Generate token"
6. 复制生成的 Token（格式: ghp_...）
7. ⚠️ 保存好 Token，离开页面后无法再次查看

**权限说明**:
- `repo`: 需要此权限来创建 Issues
- 其他权限: 不需要

---

## 🚀 执行方式

### 方式 1: 使用批处理脚本（最简单）

**Windows CMD:**
```cmd
双击运行: create_issue.bat
```

**PowerShell:**
```powershell
右键 create_issue.ps1 → "使用 PowerShell 运行"
```

**交互流程**:
1. 脚本会提示输入 DeepSeek API Key
2. 输入 GitHub Token
3. 确认仓库名称（默认: wyjapc/100Days-AI-Architect）
4. 等待执行完成
5. 查看生成的 Issue 链接

---

### 方式 2: 使用 Python 脚本

```powershell
python create_first_issue.py
```

按照提示输入所需信息。

---

### 方式 3: 使用环境变量（高级）

**设置环境变量**:
```powershell
# PowerShell
$env:DEEPSEEK_API_KEY="sk-your-key-here"
$env:GH_TOKEN="ghp-your-token-here"
$env:GITHUB_REPOSITORY="wyjapc/100Days-AI-Architect"

# 运行脚本
python scripts/pm_agent_init.py
```

**Windows CMD**:
```cmd
set DEEPSEEK_API_KEY=sk-your-key-here
set GH_TOKEN=ghp-your-token-here
set GITHUB_REPOSITORY=wyjapc/100Days-AI-Architect

python scripts/pm_agent_init.py
```

---

## 📊 执行流程

脚本会按以下步骤执行：

1. **检查环境配置**
   - 验证 API Key
   - 验证 GitHub Token
   - 确认仓库名称

2. **读取配置**
   - 加载 `tracker/template.json`
   - 加载 `prompts/pm_agent_system.md`

3. **调用 LLM API**
   - 发送请求到 DeepSeek API
   - 生成任务清单

4. **创建 GitHub Issue**
   - 使用 GitHub REST API
   - 创建标题: "Day 1 - 2026-03-06 任务看板"
   - 添加标签: `daily-task`, `auto-generated`

5. **显示结果**
   - 输出 Issue URL
   - 确认创建成功

---

## ✅ 预期结果

### 终端输出示例

```
============================================================
创建 Day 1 任务看板 - GitHub Issue
============================================================

📋 检查环境配置...
✅ 检测到 DEEPSEEK_API_KEY
✅ 检测到 GH_TOKEN
✅ 仓库: wyjapc/100Days-AI-Architect

============================================================
开始创建 Issue...
============================================================

正在调用 LLM 生成任务清单...
🤖 正在调用 DeepSeek API (deepseek-chat)...
任务生成成功:
## Day 1 - 搭建自动化追踪系统 MVP
...

正在创建 GitHub Issue: Day 1 - 2026-03-06 任务看板
✅ Issue 创建成功: https://github.com/wyjapc/100Days-AI-Architect/issues/1

============================================================
🎉 成功！
============================================================

请访问查看创建的 Issue:
https://github.com/wyjapc/100Days-AI-Architect/issues

✅ Day 1 验收标准已完成！
```

### GitHub Issue 示例

**标题**: Day 1 - 2026-03-06 任务看板

**标签**: `daily-task`, `auto-generated`

**内容**:
```markdown
## Day 1 - 搭建自动化追踪系统 MVP

**日期**: 2026-03-06
**状态**: in-progress

### 今日任务清单

- [ ] 任务 1：完成 GitHub 仓库初始化
- [ ] 任务 2：实现 PM Agent 核心脚本
- [ ] 任务 3：配置 GitHub Actions Workflow
- [ ] 任务 4：本地测试验证
- [ ] 任务 5：文档完善和推送

### 验收标准
...
```

---

## 🔍 验证步骤

1. **访问 Issues 页面**
   ```
   https://github.com/wyjapc/100Days-AI-Architect/issues
   ```

2. **检查 Issue**
   - ✅ 标题包含 "Day 1" 和日期
   - ✅ 有 `daily-task` 和 `auto-generated` 标签
   - ✅ 内容包含任务清单
   - ✅ 任务清单有 checkbox 格式

3. **测试交互**
   - 可以勾选完成的任务
   - 可以添加评论
   - 可以关闭 Issue

---

## ❓ 常见问题

### Q: API Key 无效？

**检查**:
- Key 格式正确（sk-开头）
- 账户有余额
- 网络连接正常

**解决**:
```powershell
# 测试 API 连接
python scripts/test_llm_only.py
```

### Q: GitHub Token 无效？

**检查**:
- Token 格式正确（ghp-开头）
- 权限包含 `repo`
- Token 未过期

**解决**:
重新生成 Token: https://github.com/settings/tokens

### Q: 403 Forbidden 错误？

**原因**: Token 权限不足

**解决**: 确保 Token 有 `repo` 权限

### Q: 404 Not Found 错误？

**原因**: 仓库名称错误

**解决**: 检查 `GITHUB_REPOSITORY` 格式（username/repo）

### Q: 网络连接超时？

**检查**:
- 网络连接
- 防火墙设置
- 代理配置

**解决**:
```powershell
# 测试网络连接
curl https://api.deepseek.com
curl https://api.github.com
```

---

## 🎊 完成后

### 验收标准检查清单

- [x] 仓库建立且包含规范目录
- [x] template.json 数据契约文件已提交
- [ ] GitHub Actions 成功运行 ← 现在完成这个
- [ ] 在 Issues 面板看到"Day 1 任务看板" ← 现在完成这个
- [ ] 看板内包含大模型生成的 Checklist ← 现在完成这个

### 下一步

1. **配置 GitHub Secrets**
   - 访问: https://github.com/wyjapc/100Days-AI-Architect/settings/secrets/actions
   - 添加 `DEEPSEEK_API_KEY`
   - 这样 GitHub Actions 就能自动运行了

2. **测试自动化**
   - 访问: https://github.com/wyjapc/100Days-AI-Architect/actions
   - 手动触发 "Daily PM Agent - 自动任务生成"
   - 验证自动创建 Issue

3. **开始 Day 2**
   - 更新 `tracker/template.json`
   - 设置新的学习主题
   - 让系统自动生成明天的任务

---

## 💡 提示

- 第一次运行可能需要 10-30 秒
- DeepSeek API 响应通常很快（1-3 秒）
- Issue 创建是即时的
- 可以多次运行脚本（会创建多个 Issue）

---

**准备好了吗？运行 `create_issue.bat` 或 `create_issue.ps1` 开始！** 🚀
