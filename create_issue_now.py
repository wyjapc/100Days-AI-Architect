#!/usr/bin/env python3
"""
立即创建 GitHub Issue - 交互式引导
"""

import os
import sys
from pathlib import Path

print("=" * 60)
print("🎯 创建 Day 1 任务看板 - GitHub Issue")
print("=" * 60)
print()
print("这是 Day 1 的最后验收标准！")
print()
print("需要准备:")
print("1. DeepSeek API Key (推荐) 或 OpenAI/Anthropic API Key")
print("2. GitHub Personal Access Token")
print()
print("=" * 60)
print()

# 步骤 1: 获取 LLM API Key
print("步骤 1/3: 配置 LLM API Key")
print("-" * 60)
print()
print("选择 LLM 提供商:")
print("1. DeepSeek (推荐，最便宜: ¥1/百万 tokens)")
print("2. OpenAI (GPT-3.5)")
print("3. Anthropic (Claude)")
print("4. 我已经设置了环境变量")
print()

choice = input("请选择 (1/2/3/4): ").strip()

if choice == '1':
    print()
    print("📝 获取 DeepSeek API Key:")
    print("   1. 访问: https://platform.deepseek.com/api_keys")
    print("   2. 注册/登录")
    print("   3. 创建 API Key")
    print("   4. 复制 Key (sk-开头)")
    print()
    api_key = input("请输入 DeepSeek API Key: ").strip()
    if api_key:
        os.environ['DEEPSEEK_API_KEY'] = api_key
        print("✅ DeepSeek API Key 已设置")
    else:
        print("❌ 未输入 API Key，退出")
        sys.exit(1)
        
elif choice == '2':
    print()
    api_key = input("请输入 OpenAI API Key: ").strip()
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
        print("✅ OpenAI API Key 已设置")
    else:
        print("❌ 未输入 API Key，退出")
        sys.exit(1)
        
elif choice == '3':
    print()
    api_key = input("请输入 Anthropic API Key: ").strip()
    if api_key:
        os.environ['ANTHROPIC_API_KEY'] = api_key
        print("✅ Anthropic API Key 已设置")
    else:
        print("❌ 未输入 API Key，退出")
        sys.exit(1)
        
elif choice == '4':
    has_key = (os.getenv('DEEPSEEK_API_KEY') or 
               os.getenv('OPENAI_API_KEY') or 
               os.getenv('ANTHROPIC_API_KEY'))
    if has_key:
        print("✅ 检测到环境变量中的 API Key")
    else:
        print("❌ 未检测到 API Key，请重新选择")
        sys.exit(1)
else:
    print("❌ 无效选择，退出")
    sys.exit(1)

print()

# 步骤 2: 获取 GitHub Token
print("步骤 2/3: 配置 GitHub Token")
print("-" * 60)
print()
print("📝 获取 GitHub Personal Access Token:")
print("   1. 访问: https://github.com/settings/tokens")
print("   2. Generate new token (classic)")
print("   3. 勾选 'repo' 权限")
print("   4. 复制 Token (ghp-开头)")
print()

gh_token = os.getenv('GH_TOKEN')
if not gh_token:
    gh_token = input("请输入 GitHub Token (或按回车跳过): ").strip()
    if gh_token:
        os.environ['GH_TOKEN'] = gh_token
        print("✅ GitHub Token 已设置")
    else:
        print("⚠️  未设置 GitHub Token，将仅测试 LLM 调用")
        print()
        choice = input("是否继续? (y/n): ").strip().lower()
        if choice != 'y':
            print("退出")
            sys.exit(0)
else:
    print("✅ 检测到环境变量中的 GitHub Token")

print()

# 步骤 3: 设置仓库
if gh_token:
    print("步骤 3/3: 配置仓库信息")
    print("-" * 60)
    print()
    
    repo = os.getenv('GITHUB_REPOSITORY')
    if not repo:
        default_repo = 'wyjapc/100Days-AI-Architect'
        repo_input = input(f"请输入仓库名称 (默认: {default_repo}): ").strip()
        repo = repo_input if repo_input else default_repo
        os.environ['GITHUB_REPOSITORY'] = repo
    
    print(f"✅ 仓库: {repo}")
    print()

# 执行脚本
print("=" * 60)
print("🚀 开始创建 GitHub Issue...")
print("=" * 60)
print()

try:
    # 导入并执行主脚本
    sys.path.insert(0, str(Path(__file__).parent / 'scripts'))
    
    if gh_token:
        # 完整模式：创建 GitHub Issue
        from pm_agent_init import main as pm_main
        result = pm_main()
        
        if result == 0:
            print()
            print("=" * 60)
            print("🎉 成功！GitHub Issue 已创建！")
            print("=" * 60)
            print()
            print("✅ Day 1 所有验收标准已完成！")
            print()
            print("验收标准检查清单:")
            print("✅ 1. 仓库建立且包含规范目录")
            print("✅ 2. template.json 数据契约文件已提交")
            print("✅ 3. GitHub Issue 创建成功，包含 AI 生成的 Checklist")
            print()
            print("📝 查看你的任务看板:")
            print(f"   https://github.com/{repo}/issues")
            print()
            print("🎊 恭喜！你的 100 天 AI 架构师自动化追踪系统已完全就绪！")
            print()
    else:
        # 测试模式：仅测试 LLM 调用
        from test_llm_only import main as test_main
        result = test_main()
        
        if result == 0:
            print()
            print("=" * 60)
            print("✅ LLM 测试成功！")
            print("=" * 60)
            print()
            print("任务清单已生成并保存到本地")
            print("如需创建 GitHub Issue，请配置 GitHub Token 后重新运行")
            print()
    
    sys.exit(result)
    
except KeyboardInterrupt:
    print("\n\n⚠️  用户中断")
    sys.exit(1)
except Exception as e:
    print(f"\n\n❌ 错误: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
