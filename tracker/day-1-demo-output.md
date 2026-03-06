## Day 1 - 搭建自动化追踪系统 MVP

**日期**: 2026-03-06
**状态**: in-progress
**提交**: 3911f83

### 今日任务清单

- [ ] **任务 1**: 完成 GitHub 仓库初始化
  - 建立核心目录结构 (prompts, src, tracker, scripts, .github/workflows)
  - 创建 README 和配置文档
  - 初始化 Git 仓库并推送到 GitHub

- [ ] **任务 2**: 实现 PM Agent 核心脚本
  - 开发 pm_agent_init.py 支持多种 LLM API
  - 实现 DeepSeek/OpenAI/Anthropic 三种接口
  - 添加错误处理和日志输出

- [ ] **任务 3**: 配置 GitHub Actions 自动化流
  - 创建 daily_pm_agent.yml workflow
  - 设置定时触发 (每天 08:00)
  - 配置环境变量和 Secrets

- [ ] **任务 4**: 本地测试验证
  - 测试 LLM API 调用功能
  - 验证任务清单生成质量
  - 测试 GitHub Issue 创建功能

- [ ] **任务 5**: 文档完善和推送
  - 编写快速开始指南
  - 创建测试说明文档
  - 提交代码并推送到 GitHub

### 验收标准

- ✅ 所有核心文件已创建并提交
- ✅ PM Agent 脚本能正常读取配置和提示词
- ✅ 支持 DeepSeek API 调用
- ✅ GitHub Actions Workflow 配置正确
- ⏳ 成功创建第一个自动化 Issue（需配置 API Key）

### 技术要点

- **数据契约**: 使用 JSON 格式定义每日任务结构
- **API 集成**: 支持多种 LLM 提供商，优先使用最便宜的选项
- **自动化**: GitHub Actions 定时触发，无需人工干预
- **可扩展**: 模块化设计，易于添加新功能

### 下一步计划

1. 配置 GitHub Secrets 中的 API Key
2. 手动触发 Workflow 进行首次测试
3. 验证 Issue 自动创建功能
4. 开始 Day 2 的学习任务
