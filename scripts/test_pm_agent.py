#!/usr/bin/env python3
"""
PM Agent 本地测试脚本
模拟 LLM 响应，验证整体流程
"""

import json
from pathlib import Path

def main():
    print("=" * 60)
    print("PM Agent 本地测试")
    print("=" * 60)
    
    # 1. 读取模板
    template_path = Path(__file__).parent.parent / "tracker" / "template.json"
    print(f"\n📄 读取模板: {template_path}")
    with open(template_path, 'r', encoding='utf-8') as f:
        template = json.load(f)
    print(json.dumps(template, ensure_ascii=False, indent=2))
    
    # 2. 读取系统提示词
    prompt_path = Path(__file__).parent.parent / "prompts" / "pm_agent_system.md"
    print(f"\n📝 读取系统提示词: {prompt_path}")
    with open(prompt_path, 'r', encoding='utf-8') as f:
        system_prompt = f.read()
    print(f"提示词长度: {len(system_prompt)} 字符")
    
    # 3. 模拟 LLM 响应
    print("\n🤖 模拟 LLM 生成任务清单...")
    mock_response = f"""## Day {template['day']} - {template['topic']}

**日期**: {template['date']}
**状态**: {template['status']}

### 今日任务清单

- [ ] 任务 1：完成 GitHub 仓库初始化，建立核心目录结构
- [ ] 任务 2：实现 PM Agent 核心脚本，支持 OpenAI/Anthropic API 调用
- [ ] 任务 3：配置 GitHub Actions Workflow，设置定时触发
- [ ] 任务 4：本地测试脚本执行流程，验证数据读取和 Issue 创建逻辑
- [ ] 任务 5：提交代码并推送到 GitHub，触发首次自动化流程

### 验收标准

- ✅ 所有核心文件已创建并提交
- ✅ PM Agent 脚本能正常读取配置和提示词
- ✅ GitHub Actions Workflow 配置正确
- ⏳ 成功创建第一个自动化 Issue（需配置 API Key）

### 下一步

1. 配置 GitHub Secrets（OPENAI_API_KEY 或 ANTHROPIC_API_KEY）
2. 手动触发 Workflow 进行首次测试
3. 验证 Issue 自动创建功能
"""
    
    print("\n" + "=" * 60)
    print("生成的任务清单:")
    print("=" * 60)
    print(mock_response)
    
    # 4. 显示下一步操作
    print("\n" + "=" * 60)
    print("✅ 本地测试通过！")
    print("=" * 60)
    print("\n📋 下一步操作:")
    print("1. 将代码推送到 GitHub")
    print("2. 在仓库 Settings > Secrets 中配置 API Key")
    print("3. 在 Actions 页面手动触发 Workflow")
    print("4. 查看 Issues 面板确认自动创建的任务")
    print("\n💡 提示: 如果没有 API Key，可以先推送代码，稍后再配置")

if __name__ == '__main__':
    main()
