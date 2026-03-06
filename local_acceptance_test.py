#!/usr/bin/env python3
"""
本地验收测试 - Day 1 验收标准检查
不需要 API Key，验证所有核心功能
"""

import json
import os
from pathlib import Path
import sys

def print_header(title):
    """打印标题"""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def print_check(item, status, details=""):
    """打印检查项"""
    symbol = "✅" if status else "❌"
    print(f"{symbol} {item}")
    if details:
        print(f"   {details}")

def check_directory_structure():
    """检查目录结构"""
    print_header("1. 检查目录结构")
    
    required_dirs = [
        ".github/workflows",
        "prompts",
        "scripts",
        "src",
        "tracker"
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        exists = Path(dir_path).exists()
        print_check(f"目录: {dir_path}", exists)
        all_exist = all_exist and exists
    
    return all_exist

def check_core_files():
    """检查核心文件"""
    print_header("2. 检查核心文件")
    
    required_files = {
        "tracker/template.json": "数据契约模板",
        "prompts/pm_agent_system.md": "PM Agent 系统提示词",
        "scripts/pm_agent_init.py": "PM Agent 核心脚本",
        "scripts/test_llm_only.py": "LLM 测试脚本",
        ".github/workflows/daily_pm_agent.yml": "GitHub Actions 配置",
        "README.md": "项目说明",
        ".gitignore": "Git 忽略配置"
    }
    
    all_exist = True
    for file_path, description in required_files.items():
        exists = Path(file_path).exists()
        print_check(f"{description}: {file_path}", exists)
        all_exist = all_exist and exists
    
    return all_exist

def check_template_json():
    """检查 template.json 数据契约"""
    print_header("3. 检查数据契约 (template.json)")
    
    template_path = Path("tracker/template.json")
    
    if not template_path.exists():
        print_check("文件存在", False)
        return False
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = json.load(f)
        
        print_check("文件存在", True)
        print_check("JSON 格式正确", True)
        
        # 检查必需字段
        required_fields = ["day", "date", "topic", "status", "prerequisites_met", 
                          "verification_script", "commit_hash"]
        
        all_fields_exist = True
        for field in required_fields:
            exists = field in template
            print_check(f"字段: {field}", exists, f"值: {template.get(field, 'N/A')}")
            all_fields_exist = all_fields_exist and exists
        
        return all_fields_exist
        
    except json.JSONDecodeError as e:
        print_check("JSON 格式正确", False, f"错误: {e}")
        return False
    except Exception as e:
        print_check("读取文件", False, f"错误: {e}")
        return False

def check_pm_agent_script():
    """检查 PM Agent 脚本"""
    print_header("4. 检查 PM Agent 脚本")
    
    script_path = Path("scripts/pm_agent_init.py")
    
    if not script_path.exists():
        print_check("脚本存在", False)
        return False
    
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print_check("脚本存在", True)
        
        # 检查关键函数
        checks = {
            "load_template": "加载模板函数",
            "load_system_prompt": "加载提示词函数",
            "call_deepseek": "DeepSeek API 调用",
            "call_openai": "OpenAI API 调用",
            "call_anthropic": "Anthropic API 调用",
            "create_github_issue": "创建 GitHub Issue 函数",
            "def main": "主函数"
        }
        
        all_exist = True
        for keyword, description in checks.items():
            exists = keyword in content
            print_check(description, exists)
            all_exist = all_exist and exists
        
        return all_exist
        
    except Exception as e:
        print_check("读取脚本", False, f"错误: {e}")
        return False

def check_github_actions():
    """检查 GitHub Actions 配置"""
    print_header("5. 检查 GitHub Actions 配置")
    
    workflow_path = Path(".github/workflows/daily_pm_agent.yml")
    
    if not workflow_path.exists():
        print_check("Workflow 文件存在", False)
        return False
    
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print_check("Workflow 文件存在", True)
        
        # 检查关键配置
        checks = {
            "schedule:": "定时触发配置",
            "cron:": "Cron 表达式",
            "workflow_dispatch:": "手动触发支持",
            "DEEPSEEK_API_KEY": "DeepSeek API Key 配置",
            "OPENAI_API_KEY": "OpenAI API Key 配置",
            "ANTHROPIC_API_KEY": "Anthropic API Key 配置",
            "GH_TOKEN": "GitHub Token 配置",
            "python scripts/pm_agent_init.py": "执行脚本命令"
        }
        
        all_exist = True
        for keyword, description in checks.items():
            exists = keyword in content
            print_check(description, exists)
            all_exist = all_exist and exists
        
        return all_exist
        
    except Exception as e:
        print_check("读取 Workflow", False, f"错误: {e}")
        return False

def test_script_execution():
    """测试脚本执行（模拟模式）"""
    print_header("6. 测试脚本执行能力")
    
    try:
        # 测试导入
        sys.path.insert(0, str(Path(__file__).parent / 'scripts'))
        
        print_check("Python 环境", True, f"版本: {sys.version.split()[0]}")
        
        # 检查依赖
        try:
            import requests
            print_check("requests 库", True, f"版本: {requests.__version__}")
        except ImportError:
            print_check("requests 库", False, "需要安装: pip install requests")
            return False
        
        # 测试读取配置
        from pathlib import Path
        import json
        
        template_path = Path("tracker/template.json")
        with open(template_path, 'r', encoding='utf-8') as f:
            template = json.load(f)
        print_check("读取 template.json", True, f"Day {template['day']}")
        
        # 测试读取提示词
        prompt_path = Path("prompts/pm_agent_system.md")
        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompt = f.read()
        print_check("读取系统提示词", True, f"长度: {len(prompt)} 字符")
        
        return True
        
    except Exception as e:
        print_check("脚本执行测试", False, f"错误: {e}")
        return False

def check_documentation():
    """检查文档完整性"""
    print_header("7. 检查文档完整性")
    
    docs = {
        "README.md": "项目说明",
        "SETUP.md": "配置指南",
        "QUICKSTART.md": "快速启动",
        "START_HERE.md": "开始指南",
        "DEMO.md": "演示说明",
        "TEST_DEEPSEEK.md": "DeepSeek 测试",
        "CREATE_ISSUE_GUIDE.md": "Issue 创建指南",
        "COMPLETE_DAY1.md": "完成 Day 1 指南",
        "PROJECT_STATUS.md": "项目状态",
        "SUMMARY.md": "总结文档"
    }
    
    all_exist = True
    for doc, description in docs.items():
        exists = Path(doc).exists()
        print_check(description, exists, doc)
        all_exist = all_exist and exists
    
    return all_exist

def check_helper_scripts():
    """检查辅助脚本"""
    print_header("8. 检查辅助脚本和工具")
    
    scripts = {
        "scripts/test_pm_agent.py": "本地测试脚本",
        "scripts/test_llm_only.py": "LLM 测试脚本",
        "scripts/demo_run.py": "演示脚本",
        "run_with_deepseek.bat": "Windows 批处理",
        "run_with_deepseek.ps1": "PowerShell 脚本",
        "create_first_issue.py": "创建 Issue 脚本",
        "create_issue.bat": "创建 Issue 批处理",
        "create_issue.ps1": "创建 Issue PowerShell"
    }
    
    all_exist = True
    for script, description in scripts.items():
        exists = Path(script).exists()
        print_check(description, exists, script)
        all_exist = all_exist and exists
    
    return all_exist

def run_demo_test():
    """运行演示测试"""
    print_header("9. 运行演示测试")
    
    try:
        print("正在运行演示脚本...")
        import subprocess
        result = subprocess.run(
            ["python", "scripts/demo_run.py"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        success = result.returncode == 0
        print_check("演示脚本执行", success)
        
        if success:
            # 检查输出文件
            output_file = Path("tracker/day-1-demo-output.md")
            if output_file.exists():
                print_check("生成输出文件", True, str(output_file))
                with open(output_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    has_checklist = "- [ ]" in content
                    print_check("包含任务清单", has_checklist)
            else:
                print_check("生成输出文件", False)
        
        return success
        
    except subprocess.TimeoutExpired:
        print_check("演示脚本执行", False, "超时")
        return False
    except Exception as e:
        print_check("演示脚本执行", False, f"错误: {e}")
        return False

def generate_report(results):
    """生成验收报告"""
    print_header("📊 验收报告")
    
    total = len(results)
    passed = sum(results.values())
    percentage = (passed / total * 100) if total > 0 else 0
    
    print(f"\n总计: {passed}/{total} 项通过 ({percentage:.1f}%)")
    print()
    
    for test_name, result in results.items():
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{status} - {test_name}")
    
    print()
    
    if passed == total:
        print("🎉 恭喜！所有验收标准已通过！")
        print()
        print("Day 1 MVP 已完全完成，系统就绪！")
        print()
        print("下一步:")
        print("1. 获取 DeepSeek API Key 进行真实测试")
        print("2. 运行 create_first_issue.py 创建 GitHub Issue")
        print("3. 配置 GitHub Secrets 启用自动化")
        return True
    else:
        print("⚠️  部分验收标准未通过，请检查失败项。")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("100Days-AI-Architect - Day 1 本地验收测试")
    print("=" * 60)
    print()
    print("这个脚本将验证所有 Day 1 验收标准")
    print("不需要 API Key，完全本地执行")
    print()
    
    results = {}
    
    # 执行所有检查
    results["目录结构"] = check_directory_structure()
    results["核心文件"] = check_core_files()
    results["数据契约"] = check_template_json()
    results["PM Agent 脚本"] = check_pm_agent_script()
    results["GitHub Actions"] = check_github_actions()
    results["脚本执行能力"] = test_script_execution()
    results["文档完整性"] = check_documentation()
    results["辅助工具"] = check_helper_scripts()
    results["演示测试"] = run_demo_test()
    
    # 生成报告
    success = generate_report(results)
    
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())
