#!/usr/bin/env python3
"""
测试完整流程 - 展示每一步
"""

print("=" * 60)
print("🎯 创建 Day 1 任务看板 - 流程演示")
print("=" * 60)
print()
print("这个脚本将展示完整的执行流程")
print()

# 步骤 1
print("步骤 1/5: 读取配置")
print("-" * 60)

import json
from pathlib import Path

template_path = Path("tracker/template.json")
with open(template_path, 'r', encoding='utf-8') as f:
    template = json.load(f)

print(f"✅ Day: {template['day']}")
print(f"✅ Date: {template['date']}")
print(f"✅ Topic: {template['topic']}")
print(f"✅ Status: {template['status']}")
print()

# 步骤 2
print("步骤 2/5: 读取系统提示词")
print("-" * 60)

prompt_path = Path("prompts/pm_agent_system.md")
with open(prompt_path, 'r', encoding='utf-8') as f:
    prompt = f.read()

print(f"✅ 提示词长度: {len(prompt)} 字符")
print(f"✅ 文件: {prompt_path}")
print()

# 步骤 3
print("步骤 3/5: 准备 API 调用")
print("-" * 60)
print()
print("需要的信息:")
print("1. LLM API Key (DeepSeek/OpenAI/Anthropic)")
print("2. GitHub Personal Access Token")
print()
print("API 调用流程:")
print("  → 发送系统提示词和用户消息到 LLM")
print("  → LLM 生成任务清单")
print("  → 返回 Markdown 格式的内容")
print()

# 步骤 4
print("步骤 4/5: 创建 GitHub Issue")
print("-" * 60)
print()
print("Issue 创建流程:")
print("  → 使用 GitHub REST API")
print("  → POST /repos/{owner}/{repo}/issues")
print("  → 标题: Day 1 - 2026-03-06 任务看板")
print("  → 标签: daily-task, auto-generated")
print("  → 内容: LLM 生成的任务清单")
print()

# 步骤 5
print("步骤 5/5: 验证结果")
print("-" * 60)
print()
print("验证项:")
print("  ✅ Issue 创建成功")
print("  ✅ 包含任务清单 (- [ ] 格式)")
print("  ✅ 包含验收标准")
print("  ✅ 包含技术要点")
print()

print("=" * 60)
print("📋 准备执行真实流程")
print("=" * 60)
print()
print("现在你可以:")
print()
print("1. 双击运行: START_NOW.bat")
print("   → 会提示你输入 API Key 和 Token")
print("   → 自动完成所有步骤")
print()
print("2. 或者手动设置环境变量后运行:")
print()
print("   Windows CMD:")
print("   set DEEPSEEK_API_KEY=sk-your-key")
print("   set GH_TOKEN=ghp-your-token")
print("   set GITHUB_REPOSITORY=wyjapc/100Days-AI-Architect")
print("   python scripts/pm_agent_init.py")
print()
print("   PowerShell:")
print("   $env:DEEPSEEK_API_KEY='sk-your-key'")
print("   $env:GH_TOKEN='ghp-your-token'")
print("   $env:GITHUB_REPOSITORY='wyjapc/100Days-AI-Architect'")
print("   python scripts/pm_agent_init.py")
print()
print("=" * 60)
print()
print("💡 提示:")
print("- DeepSeek API Key: https://platform.deepseek.com/api_keys")
print("- GitHub Token: https://github.com/settings/tokens")
print()
print("准备好后，运行 START_NOW.bat 开始！")
print()
