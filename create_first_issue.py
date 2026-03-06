#!/usr/bin/env python3
"""
创建第一个 GitHub Issue
完成 Day 1 的最后验收标准
"""

import os
import sys

def main():
    print("=" * 60)
    print("创建 Day 1 任务看板 - GitHub Issue")
    print("=" * 60)
    print()
    
    # 检查环境
    print("📋 检查环境配置...")
    
    # 1. 检查 LLM API Key
    deepseek_key = os.getenv('DEEPSEEK_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    
    has_llm_key = deepseek_key or openai_key or anthropic_key
    
    if not has_llm_key:
        print("⚠️  未检测到 LLM API Key")
        print()
        print("请选择一个选项:")
        print("1. 输入 DeepSeek API Key (推荐)")
        print("2. 输入 OpenAI API Key")
        print("3. 输入 Anthropic API Key")
        print("4. 退出")
        print()
        
        choice = input("请选择 (1/2/3/4): ").strip()
        
        if choice == '1':
            key = input("请输入 DeepSeek API Key: ").strip()
            if key:
                os.environ['DEEPSEEK_API_KEY'] = key
                print("✅ DeepSeek API Key 已设置")
            else:
                print("❌ 未输入有效的 Key")
                return 1
        elif choice == '2':
            key = input("请输入 OpenAI API Key: ").strip()
            if key:
                os.environ['OPENAI_API_KEY'] = key
                print("✅ OpenAI API Key 已设置")
            else:
                print("❌ 未输入有效的 Key")
                return 1
        elif choice == '3':
            key = input("请输入 Anthropic API Key: ").strip()
            if key:
                os.environ['ANTHROPIC_API_KEY'] = key
                print("✅ Anthropic API Key 已设置")
            else:
                print("❌ 未输入有效的 Key")
                return 1
        else:
            print("退出")
            return 0
    else:
        if deepseek_key:
            print("✅ 检测到 DEEPSEEK_API_KEY")
        elif openai_key:
            print("✅ 检测到 OPENAI_API_KEY")
        elif anthropic_key:
            print("✅ 检测到 ANTHROPIC_API_KEY")
    
    print()
    
    # 2. 检查 GitHub Token
    gh_token = os.getenv('GH_TOKEN')
    
    if not gh_token:
        print("⚠️  未检测到 GH_TOKEN")
        print()
        print("需要 GitHub Personal Access Token 来创建 Issue")
        print("获取地址: https://github.com/settings/tokens")
        print()
        print("权限要求: repo (完整仓库访问)")
        print()
        
        token = input("请输入 GitHub Token (或按回车跳过): ").strip()
        
        if token:
            os.environ['GH_TOKEN'] = token
            print("✅ GitHub Token 已设置")
        else:
            print("⏭️  跳过 GitHub Issue 创建")
            print("   将仅测试 LLM 调用")
            print()
            
            # 只运行 LLM 测试
            from pathlib import Path
            sys.path.insert(0, str(Path(__file__).parent / 'scripts'))
            from test_llm_only import main as test_main
            return test_main()
    else:
        print("✅ 检测到 GH_TOKEN")
    
    # 3. 设置仓库名称
    repo = os.getenv('GITHUB_REPOSITORY')
    if not repo:
        print()
        default_repo = 'wyjapc/100Days-AI-Architect'
        repo_input = input(f"请输入仓库名称 (默认: {default_repo}): ").strip()
        repo = repo_input if repo_input else default_repo
        os.environ['GITHUB_REPOSITORY'] = repo
        print(f"✅ 仓库设置为: {repo}")
    else:
        print(f"✅ 仓库: {repo}")
    
    print()
    print("=" * 60)
    print("开始创建 Issue...")
    print("=" * 60)
    print()
    
    # 4. 执行主脚本
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent / 'scripts'))
    from pm_agent_init import main as pm_main
    
    result = pm_main()
    
    if result == 0:
        print()
        print("=" * 60)
        print("🎉 成功！")
        print("=" * 60)
        print()
        print(f"请访问查看创建的 Issue:")
        print(f"https://github.com/{repo}/issues")
        print()
        print("✅ Day 1 验收标准已完成！")
    
    return result

if __name__ == '__main__':
    sys.exit(main())
