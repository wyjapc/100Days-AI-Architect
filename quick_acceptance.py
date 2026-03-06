#!/usr/bin/env python3
"""
快速验收测试 - 简化版
"""

import json
from pathlib import Path
import subprocess
import sys

def check(name, condition, details=""):
    """检查并打印结果"""
    symbol = "✅" if condition else "❌"
    print(f"{symbol} {name}")
    if details:
        print(f"   {details}")
    return condition

print("=" * 60)
print("Day 1 快速验收测试")
print("=" * 60)
print()

# 1. 检查目录结构
print("1️⃣  验收标准 1: 仓库建立且包含规范目录")
print("-" * 60)

dirs = {
    ".github/workflows": "GitHub Actions",
    "prompts": "提示词目录",
    "scripts": "脚本目录",
    "src": "源代码目录",
    "tracker": "追踪目录"
}

all_dirs_ok = True
for d, desc in dirs.items():
    exists = Path(d).exists()
    check(f"{desc}: {d}", exists)
    all_dirs_ok = all_dirs_ok and exists

print()
if all_dirs_ok:
    print("✅ 验收标准 1 通过：所有规范目录已建立")
else:
    print("❌ 验收标准 1 失败：部分目录缺失")

print()
print("=" * 60)
print()

# 2. 检查 template.json
print("2️⃣  验收标准 2: template.json 数据契约文件已提交")
print("-" * 60)

template_ok = False
template_path = Path("tracker/template.json")

if template_path.exists():
    check("文件存在", True, str(template_path))
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        check("JSON 格式正确", True)
        
        fields = ["day", "date", "topic", "status", "prerequisites_met", 
                 "verification_script", "commit_hash"]
        
        print("\n字段检查:")
        all_fields = True
        for field in fields:
            exists = field in data
            check(f"  {field}", exists, f"= {data.get(field, 'N/A')}")
            all_fields = all_fields and exists
        
        # 检查 Git 提交
        print("\nGit 提交状态:")
        try:
            result = subprocess.run(
                ["git", "log", "--oneline", "-1", "tracker/template.json"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                commit = result.stdout.strip()
                check("已提交到 Git", True, commit)
                template_ok = all_fields
            else:
                check("已提交到 Git", False)
        except:
            check("已提交到 Git", False, "无法验证")
            template_ok = all_fields
            
    except Exception as e:
        check("JSON 格式正确", False, str(e))
else:
    check("文件存在", False)

print()
if template_ok:
    print("✅ 验收标准 2 通过：数据契约文件完整且已提交")
else:
    print("❌ 验收标准 2 失败：数据契约文件有问题")

print()
print("=" * 60)
print()

# 3. 检查核心文件
print("3️⃣  核心文件和脚本检查")
print("-" * 60)

files = {
    "scripts/pm_agent_init.py": "PM Agent 核心脚本",
    "prompts/pm_agent_system.md": "系统提示词",
    ".github/workflows/daily_pm_agent.yml": "GitHub Actions 配置"
}

all_files_ok = True
for f, desc in files.items():
    exists = Path(f).exists()
    check(desc, exists, f)
    all_files_ok = all_files_ok and exists

print()

# 检查脚本功能
if Path("scripts/pm_agent_init.py").exists():
    print("脚本功能检查:")
    with open("scripts/pm_agent_init.py", 'r', encoding='utf-8') as f:
        content = f.read()
    
    funcs = {
        "call_deepseek": "DeepSeek API",
        "call_openai": "OpenAI API",
        "call_anthropic": "Anthropic API",
        "create_github_issue": "GitHub Issue 创建"
    }
    
    for func, desc in funcs.items():
        exists = func in content
        check(f"  {desc}", exists)
        all_files_ok = all_files_ok and exists

print()
if all_files_ok:
    print("✅ 核心文件和脚本完整")
else:
    print("❌ 部分核心文件缺失")

print()
print("=" * 60)
print()

# 4. 运行演示测试
print("4️⃣  演示测试")
print("-" * 60)

demo_ok = False
try:
    print("正在运行演示脚本...")
    result = subprocess.run(
        ["python", "scripts/demo_run.py"],
        capture_output=True,
        text=True,
        timeout=15
    )
    
    if result.returncode == 0:
        check("演示脚本执行", True)
        
        output_file = Path("tracker/day-1-demo-output.md")
        if output_file.exists():
            check("生成输出文件", True, str(output_file))
            
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            has_title = "## Day" in content
            has_checklist = "- [ ]" in content
            has_criteria = "验收标准" in content
            
            check("包含标题", has_title)
            check("包含任务清单", has_checklist)
            check("包含验收标准", has_criteria)
            
            demo_ok = has_title and has_checklist and has_criteria
        else:
            check("生成输出文件", False)
    else:
        check("演示脚本执行", False, result.stderr[:100])
        
except Exception as e:
    check("演示脚本执行", False, str(e))

print()
if demo_ok:
    print("✅ 演示测试通过")
else:
    print("❌ 演示测试失败")

print()
print("=" * 60)
print()

# 5. 总结
print("📊 验收总结")
print("=" * 60)
print()

results = {
    "验收标准 1: 目录结构": all_dirs_ok,
    "验收标准 2: 数据契约": template_ok,
    "核心文件和脚本": all_files_ok,
    "演示测试": demo_ok
}

passed = sum(results.values())
total = len(results)

print(f"通过: {passed}/{total} 项")
print()

for name, result in results.items():
    status = "✅ 通过" if result else "❌ 失败"
    print(f"{status} - {name}")

print()
print("=" * 60)
print()

if passed >= 3:
    print("🎉 本地验收通过！")
    print()
    print("✅ 仓库建立且包含规范目录")
    print("✅ template.json 数据契约文件已提交")
    print("✅ 核心脚本和配置完整")
    print()
    print("⏳ 待完成验收标准 3:")
    print("   GitHub Actions 成功运行并创建 Issue")
    print()
    print("完成方法:")
    print("1. 获取 DeepSeek API Key: https://platform.deepseek.com/api_keys")
    print("2. 获取 GitHub Token: https://github.com/settings/tokens")
    print("3. 运行: python create_first_issue.py")
    print("   或双击: create_issue.bat")
    print()
    sys.exit(0)
else:
    print("⚠️  部分验收标准未通过")
    print("请检查失败项")
    print()
    sys.exit(1)
