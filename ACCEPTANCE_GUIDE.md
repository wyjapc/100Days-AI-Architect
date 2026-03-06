# 📋 Day 1 完整验收指南

## 🎯 验收标准

根据任务要求，Day 1 需要完成以下验收标准（DoD - Definition of Done）：

1. ✅ **仓库建立且包含上述规范目录**
   - `.github/workflows` - GitHub Actions 配置
   - `prompts` - 提示词版本控制
   - `scripts` - 自动化脚本
   - `src` - 工程代码
   - `tracker` - 每日结构化学习记录

2. ✅ **template.json 数据契约文件已提交**
   - 包含所有必需字段（day, date, topic, status, etc.）
   - 已提交到 Git 仓库

3. ⏳ **GitHub Actions 成功运行，并且能在仓库的 Issues 面板中看到由 API 自动创建的"Day 1 任务看板"，看板内包含大模型生成的 Checklist**

---

## 🚀 执行完整验收

### 方法 1: 一键验收（推荐）

**Windows:**
```
双击运行: run_full_acceptance.bat
```

**PowerShell:**
```powershell
.\run_full_acceptance.ps1
```

**命令行:**
```bash
python full_acceptance.py
```

### 方法 2: 分步验收

#### 步骤 1: 本地环境验收

```bash
python local_acceptance_test.py
```

这将验证:
- ✅ 目录结构
- ✅ 核心文件
- ✅ 数据契约
- ✅ 脚本功能
- ✅ 文档完整性

#### 步骤 2: 演示测试

```bash
python scripts/demo_run.py
```

验证系统能够:
- 读取配置
- 加载提示词
- 生成任务清单（模拟）
- 保存输出文件

#### 步骤 3: 创建 GitHub Issue

```bash
python create_first_issue.py
```

或双击: `create_issue.bat`

这将:
- 调用真实的 LLM API
- 生成任务清单
- 在 GitHub 创建 Issue

---

## 📊 验收流程

### 完整验收脚本会执行以下步骤:

1. **验证目录结构**
   - 检查所有必需目录是否存在
   - 验证目录结构符合规范

2. **验证数据契约**
   - 检查 `tracker/template.json` 存在
   - 验证 JSON 格式正确
   - 检查所有必需字段
   - 确认已提交到 Git

3. **验证核心脚本**
   - 检查 PM Agent 脚本存在
   - 验证支持多种 LLM API
   - 检查 GitHub Actions 配置
   - 验证系统提示词

4. **运行演示测试**
   - 执行模拟流程
   - 生成示例输出
   - 验证输出格式

5. **创建 GitHub Issue**（可选）
   - 提示输入 API Key
   - 调用真实 LLM API
   - 创建 GitHub Issue
   - 验证任务看板

6. **生成验收报告**
   - 统计通过/失败项
   - 显示详细结果
   - 给出下一步建议

---

## 🔑 准备工作

### 如果要完成第 3 项验收标准，需要:

#### 1. DeepSeek API Key（推荐）

**获取步骤:**
1. 访问: https://platform.deepseek.com/
2. 注册/登录
3. 进入 API Keys: https://platform.deepseek.com/api_keys
4. 创建新密钥
5. 复制 Key（sk-开头）
6. 充值 ¥10（足够用很久）

**成本:** ¥1/百万 tokens，100 天总成本 < ¥1

#### 2. GitHub Personal Access Token

**获取步骤:**
1. 访问: https://github.com/settings/tokens
2. Generate new token (classic)
3. 名称: `100Days-AI-Architect`
4. 权限: 勾选 `repo`
5. Generate token
6. 复制 Token（ghp-开头）

---

## 📈 预期结果

### 本地验收通过

```
============================================================
📊 Day 1 完整验收报告
============================================================

总计: 4/4 项通过

详细结果:
------------------------------------------------------------
✅ 通过 - 目录结构
✅ 通过 - 数据契约
✅ 通过 - 核心脚本
✅ 通过 - 演示测试
⏭️  跳过 - GitHub Issue

============================================================

✅ 本地验收已完成！

✅ 仓库建立且包含规范目录
✅ template.json 数据契约文件已提交
✅ 核心脚本和配置完整
✅ 演示测试通过

⏳ 待完成:
- 创建 GitHub Issue（任务看板）
```

### 完整验收通过

```
============================================================
📊 Day 1 完整验收报告
============================================================

总计: 5/5 项通过

详细结果:
------------------------------------------------------------
✅ 通过 - 目录结构
✅ 通过 - 数据契约
✅ 通过 - 核心脚本
✅ 通过 - 演示测试
✅ 通过 - GitHub Issue

============================================================

🎉 恭喜！Day 1 所有验收标准已完成！

✅ 仓库建立且包含规范目录
✅ template.json 数据契约文件已提交
✅ GitHub Actions 配置完成
✅ GitHub Issue 创建成功
✅ 任务看板包含大模型生成的 Checklist

下一步:
1. 访问 GitHub Issues 查看任务看板
2. 配置 GitHub Secrets 启用自动化
3. 开始 Day 2 的学习任务
```

### GitHub Issue 示例

访问: https://github.com/wyjapc/100Days-AI-Architect/issues

你会看到:

**标题:** Day 1 - 2026-03-06 任务看板

**标签:** `daily-task`, `auto-generated`

**内容:**
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

## ❓ 常见问题

### Q: 可以只做本地验收吗？

A: 可以！运行 `python local_acceptance_test.py` 即可完成本地验收。GitHub Issue 创建是可选的。

### Q: 没有 API Key 怎么办？

A: 可以先完成本地验收，稍后再创建 GitHub Issue。或者使用演示模式查看效果。

### Q: API Key 配置失败？

A: 检查:
- Key 格式正确（sk-开头）
- 账户有余额
- 网络连接正常

### Q: GitHub Token 权限不足？

A: 确保 Token 有 `repo` 权限，可以重新生成。

### Q: 验收脚本执行失败？

A: 检查:
- Python 版本（3.7+）
- requests 库已安装
- 在项目根目录执行

---

## 🎊 完成后

### 验收标准检查清单

- [ ] 运行完整验收脚本
- [ ] 本地验收全部通过
- [ ] 演示测试成功
- [ ] （可选）创建 GitHub Issue
- [ ] 查看验收报告

### 下一步行动

1. **如果本地验收通过但未创建 Issue:**
   - 获取 DeepSeek API Key
   - 获取 GitHub Token
   - 运行 `create_first_issue.py`

2. **如果完全验收通过:**
   - 访问 GitHub Issues 查看任务看板
   - 配置 GitHub Secrets 启用自动化
   - 准备 Day 2 的学习任务

3. **配置自动化（可选）:**
   - 在 GitHub Secrets 添加 `DEEPSEEK_API_KEY`
   - 手动触发 GitHub Actions
   - 验证自动创建 Issue

---

## 📚 相关文档

- `COMPLETE_DAY1.md` - 完成 Day 1 指南
- `CREATE_ISSUE_GUIDE.md` - Issue 创建详细指南
- `PROJECT_STATUS.md` - 项目状态报告
- `SUMMARY.md` - Day 1 总结

---

## 🚀 立即开始

**准备好了吗？**

```bash
# 方法 1: 双击运行
run_full_acceptance.bat

# 方法 2: 命令行
python full_acceptance.py

# 方法 3: 仅本地验收
python local_acceptance_test.py
```

**开始你的 Day 1 完整验收！** 🎉
