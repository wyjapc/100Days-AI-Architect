#!/usr/bin/env python3
"""
本地执行 PM Agent 脚本
用于测试完整流程（包括真实的 LLM 调用和 GitHub Issue 创建）
"""

import os
import sys
from pathlib import Path

def main():
    print("=" * 60)
    print("PM Agent 本地执行")
    print("=" * 60)
    
    # 检查 API Key
    openai_key = os.getenv('OPENAI_API_KEY')
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    
    if not openai_key and not anthropic_key:
        print("\n⚠️  未检测到 API Key 环境变量")
        print("\n请选择一个选项:")
        print("1. 输入 OpenAI API Key")
        print("2. 输入 Anthropic API Key")
        print("3. 退出")
        
        choice = input("\n请选择 (1/2/3): ").strip()
        
        if choice == '1':
            api_key = input("请输入 OpenAI API Key: ").strip()
            if api_key:
                os.environ['OPENAI_API_KEY'] = api_key
                print("✅ OpenAI API Key 已设置")
        elif choice == '2':
            api_key = input("请输入 Anthropic API Key: ").strip()
            if api_key:
                os.environ['ANTHROPIC_API_KEY'] = api_key
                print("✅ Anthropic API Key 已设置")
        else:
            print("退出")
            return 0
    else:
        if openai_key:
            print("✅ 检测到 OPENAI_API_KEY")
        if anthropic_key:
            print("✅ 检测到 ANTHROPIC_API_KEY")
    
    # 检查 GitHub Token
    gh_token = os.getenv('GH_TOKEN')
    if not gh_token:
        print("\n⚠️  未检测到 GH_TOKEN 环境变量")
        print("如果要创建 GitHub Issue，需要提供 GitHub Personal Access Token")
        print("可以在这里创建: https://github.com/settings/tokens")
        
        create_issue = input("\n是否要创建 GitHub Issue? (y/n): ").strip().lower()
        
        if create_issue == 'y':
            gh_token = input("请输入 GitHub Token: ").strip()
            if gh_token:
                os.environ['GH_TOKEN'] = gh_token
                repo = input("请输入仓库名称 (格式: username/repo): ").strip()
                if repo:
                    os.environ['GITHUB_REPOSITORY'] = repo
                    print("✅ GitHub 配置已设置")
        else:
            print("⏭️  跳过 GitHub Issue 创建，仅测试 LLM 调用")
    else:
        print("✅ 检测到 GH_TOKEN")
        if not os.getenv('GITHUB_REPOSITORY'):
            os.environ['GITHUB_REPOSITORY'] = 'wyjapc/100Days-AI-Architect'
    
    # 执行主脚本
    print("\n" + "=" * 60)
    print("开始执行 PM Agent...")
    print("=" * 60 + "\n")
    
    # 导入并执行主脚本
    sys.path.insert(0, str(Path(__file__).parent))
    from pm_agent_init import main as pm_main
    
    return pm_main()

if __name__ == '__main__':
    sys.exit(main())
