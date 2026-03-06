#!/usr/bin/env python3
"""
演示运行 - 展示完整流程（使用模拟数据）
"""

import json
from pathlib import Path
import time

def main():
    print("=" * 60)
    print("PM Agent 演示运行")
    print("=" * 60)
    print("\n这是一个演示，展示完整的执行流程\n")
    
    # 1. 读取模板
    print("步骤 1/5: 读取任务模板")
    print("-" * 60)
    template_path = Path(__file__).parent.parent / "tracker" / "template.json"
    with open(template_path, 'r', encoding='utf-8') as f:
        template = json.load(f)
    
    print(f"✅ Day: {template['day']}")
    print(f"✅ Date: {template['date']}")
    print(f"✅ Topic: {template['topic']}")
    print(f"✅ Status: {template['status']}")
    time.sleep(1)
    
    # 2. 读取系统提示词
    print("\n步骤 2/5: 读取系统提示词")
    print("-" * 60)
    prompt_path = Path(__file__).parent.parent / "prompts" / "pm_agent_system.md"
    with open(prompt_path, 'r', encoding='utf-8') as f:
        system_prompt = f.read()
    print(f"✅ 提示词长度: {len(system_prompt)} 字符")
    print(f"✅ 提示词文件: {prompt_path.name}")
    time.sleep(1)
    
    # 3. 模拟 LLM 调用
    print("\n步骤 3/5: 调用 LLM API")
    print("-" * 60)
    print("🤖 正在调用 DeepSeek API (deepseek-chat)...")
    print("   API 地址: https://api.deepseek.com/v1/chat/completions")
    print("   模型: deepseek-chat")
    print("   Temperature: 0.7")
    time.sleep(2)
    
    # 模拟生成的任务清单
    mock_response = f"""## Day {template['day']} - {template['topic']}

**日期**: {template['date']}
**状态**: {template['status']}
**提交**: {template['commit_hash']}

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
"""
    
    print("✅ LLM 响应成功！")
    time.sleep(1)
    
    # 4. 显示生成的内容
    print("\n步骤 4/5: 生成的任务清单")
    print("=" * 60)
    print(mock_response)
    print("=" * 60)
    time.sleep(1)
    
    # 5. 保存结果
    print("\n步骤 5/5: 保存结果")
    print("-" * 60)
    output_path = Path(__file__).parent.parent / f"tracker/day-{template['day']}-demo-output.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(mock_response)
    print(f"✅ 任务清单已保存到: {output_path}")
    
    # 总结
    print("\n" + "=" * 60)
    print("🎉 演示完成！")
    print("=" * 60)
    print("\n📊 执行摘要:")
    print(f"   - 读取配置: ✅")
    print(f"   - 加载提示词: ✅")
    print(f"   - 调用 LLM: ✅ (模拟)")
    print(f"   - 生成任务: ✅")
    print(f"   - 保存结果: ✅")
    
    print("\n💡 使用真实 API:")
    print("   1. 获取 DeepSeek API Key: https://platform.deepseek.com/api_keys")
    print("   2. 运行: python scripts/test_llm_only.py")
    print("   3. 或双击: run_with_deepseek.bat")
    
    print("\n📝 查看生成的文件:")
    print(f"   {output_path}")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
