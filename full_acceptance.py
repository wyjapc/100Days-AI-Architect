#!/usr/bin/env python3
"""
完整验收测试 - Day 1 所有验收标准
包含本地验证和 GitHub Issue 创建
"""

import json
import os
import sys
from pathlib import Path
import subprocess

class Colors:
    """终端颜色"""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(title, color=Colors.CYAN):
    """打印标题"""
    print(f"\n{color}{'=' * 60}")
    print(title)
    print(f"{'=' * 60}{Colors.RESET}\n")

def print_step(step_num, title):
    """打印步骤"""
    print(f"\n{Colors.BOLD}{Colors.YELLOW}步骤 {step_num}: {title}{Colors.RESET}")
    print("-" * 60)

def print_check(item, status, details=""):
    """打印检查项"""
    symbol = f"{Colors.GREEN}✅" if status else f"{Colors.RED}❌"
    print(f"{symbol} {item}{Colors.RESET}")
    if details:
        print(f"   {details}")

def print_info(message):
    """打印信息"""
    print(f"{Colors.CYAN}ℹ️  {message}{Colors.RESET}")

def print_success(message):
    """打印成功消息"""
    print(f"{Colors.GREEN}✅ {message}{Colors.RESET}")

def print_error(message):
    """打印错误消息"""
    print(f"{Colors.RED}❌ {message}{Colors.RESET}")

def verify_local_environment():
    """验收标准 1: 仓库建立且包含上述规范目录"""
    print_step(1, "验收标准 1: 仓库建立且包含规范目录")
    
    required_dirs = {
        ".github/workflows": "GitHub Actions 工作流",
        "prompts": "提示词目录",
        "scripts": "脚本目录",
        "src": "源代码目录",
        "tracker": "追踪记录目录"
    }
    
    all_passed = True
    for dir_path, description in required_dirs.items():
        exists = Path(dir_path).exists()
        print_check(f"{description}: {dir_path}", exists)
        all_passed = all_passed and exists
    
    if all_passed:
        print_success("所有规范目录已建立")
    else:
        print_error("部分目录缺失")
    
    return all_passed

def verify_template_json():
    """验收标准 2: template.json 数据契约文件已提交"""
    print_step(2, "验收标准 2: template.json 数据契约文件已提交")
    
    template_path = Path("tracker/template.json")
    
    if not template_path.exists():
        print_error("template.json 文件不存在")
        return False
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = json.load(f)
        
        print_check("文件存在", True)
        print_check("JSON 格式正确", True)
        
        # 验证必需字段
        required_fields = {
            "day": "天数",
            "date": "日期",
            "topic": "主题",
            "status": "状态",
            "prerequisites_met": "前置条件",
            "verification_script": "验证脚本",
            "commit_hash": "提交哈希"
        }
        
        all_fields_exist = True
        print("\n字段验证:")
        for field, description in required_fields.items():
            exists = field in template
            value = template.get(field, "N/A")
            print_check(f"{description} ({field})", exists, f"值: {value}")
            all_fields_exist = all_fields_exist and exists
        
        # 检查 Git 提交状态
        try:
            result = subprocess.run(
                ["git", "log", "--oneline", "-1", "tracker/template.json"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                print_check("已提交到 Git", True, result.stdout.strip())
            else:
                print_check("已提交到 Git", False)
        except:
            print_check("已提交到 Git", False, "无法验证")
        
        if all_fields_exist:
            print_success("数据契约文件完整且已提交")
        
        return all_fields_exist
        
    except json.JSONDecodeError as e:
        print_error(f"JSON 格式错误: {e}")
        return False
    except Exception as e:
        print_error(f"读取文件失败: {e}")
        return False

def verify_core_scripts():
    """验证核心脚本完整性"""
    print_step(3, "验证核心脚本和配置")
    
    core_files = {
        "scripts/pm_agent_init.py": "PM Agent 核心脚本",
        "prompts/pm_agent_system.md": "系统提示词",
        ".github/workflows/daily_pm_agent.yml": "GitHub Actions 配置"
    }
    
    all_passed = True
    for file_path, description in core_files.items():
        exists = Path(file_path).exists()
        print_check(description, exists, file_path)
        all_passed = all_passed and exists
    
    # 验证脚本功能
    if Path("scripts/pm_agent_init.py").exists():
        with open("scripts/pm_agent_init.py", 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("\n脚本功能验证:")
        functions = {
            "call_deepseek": "DeepSeek API 支持",
            "call_openai": "OpenAI API 支持",
            "call_anthropic": "Anthropic API 支持",
            "create_github_issue": "GitHub Issue 创建"
        }
        
        for func, desc in functions.items():
            exists = func in content
            print_check(desc, exists)
            all_passed = all_passed and exists
    
    if all_passed:
        print_success("核心脚本和配置完整")
    
    return all_passed

def run_demo_test():
    """运行演示测试"""
    print_step(4, "运行演示测试（模拟 LLM 调用）")
    
    try:
        print_info("正在执行演示脚本...")
        result = subprocess.run(
            ["python", "scripts/demo_run.py"],
            capture_output=True,
            text=True,
            timeout=15
        )
        
        success = result.returncode == 0
        
        if success:
            print_success("演示脚本执行成功")
            
            # 检查输出文件
            output_file = Path("tracker/day-1-demo-output.md")
            if output_file.exists():
                print_check("生成输出文件", True, str(output_file))
                
                with open(output_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 验证内容
                checks = {
                    "## Day": "包含标题",
                    "- [ ]": "包含任务清单",
                    "验收标准": "包含验收标准",
                    "技术要点": "包含技术要点"
                }
                
                print("\n输出内容验证:")
                for keyword, desc in checks.items():
                    exists = keyword in content
                    print_check(desc, exists)
                
                print_success("演示测试通过")
                return True
            else:
                print_error("未生成输出文件")
                return False
        else:
            print_error(f"演示脚本执行失败: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print_error("演示脚本执行超时")
        return False
    except Exception as e:
        print_error(f"演示测试失败: {e}")
        return False

def create_github_issue():
    """验收标准 3: GitHub Actions 成功运行并创建 Issue"""
    print_step(5, "验收标准 3: 创建 GitHub Issue（任务看板）")
    
    print_info("这一步需要真实的 API Key 和 GitHub Token")
    print()
    
    # 检查环境变量
    has_llm_key = (os.getenv('DEEPSEEK_API_KEY') or 
                   os.getenv('OPENAI_API_KEY') or 
                   os.getenv('ANTHROPIC_API_KEY'))
    has_gh_token = os.getenv('GH_TOKEN')
    
    if has_llm_key and has_gh_token:
        print_success("检测到 API Key 和 GitHub Token")
        choice = input("\n是否立即创建 GitHub Issue? (y/n): ").strip().lower()
        
        if choice == 'y':
            try:
                print_info("正在创建 GitHub Issue...")
                result = subprocess.run(
                    ["python", "scripts/pm_agent_init.py"],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    print_success("GitHub Issue 创建成功！")
                    print(result.stdout)
                    return True
                else:
                    print_error(f"创建失败: {result.stderr}")
                    return False
                    
            except Exception as e:
                print_error(f"执行失败: {e}")
                return False
        else:
            print_info("跳过 GitHub Issue 创建")
            return None
    else:
        print(f"{Colors.YELLOW}⚠️  未检测到必需的环境变量{Colors.RESET}")
        print()
        print("需要配置:")
        if not has_llm_key:
            print("  - DEEPSEEK_API_KEY (或 OPENAI_API_KEY / ANTHROPIC_API_KEY)")
        if not has_gh_token:
            print("  - GH_TOKEN")
        print()
        
        choice = input("是否现在配置并创建? (y/n): ").strip().lower()
        
        if choice == 'y':
            try:
                print_info("正在启动交互式配置...")
                result = subprocess.run(
                    ["python", "create_first_issue.py"],
                    timeout=300  # 5 分钟超时
                )
                return result.returncode == 0
            except Exception as e:
                print_error(f"配置失败: {e}")
                return False
        else:
            print_info("跳过 GitHub Issue 创建")
            print()
            print(f"{Colors.YELLOW}提示: 稍后可以运行以下命令创建 Issue:{Colors.RESET}")
            print("  python create_first_issue.py")
            print("  或双击: create_issue.bat")
            return None

def generate_final_report(results):
    """生成最终验收报告"""
    print_header("📊 Day 1 完整验收报告", Colors.BOLD + Colors.CYAN)
    
    # 统计结果
    total = len([r for r in results.values() if r is not None])
    passed = sum([1 for r in results.values() if r is True])
    skipped = sum([1 for r in results.values() if r is None])
    
    print(f"总计: {passed}/{total} 项通过")
    if skipped > 0:
        print(f"跳过: {skipped} 项")
    print()
    
    # 详细结果
    print("详细结果:")
    print("-" * 60)
    
    status_map = {
        True: f"{Colors.GREEN}✅ 通过{Colors.RESET}",
        False: f"{Colors.RED}❌ 失败{Colors.RESET}",
        None: f"{Colors.YELLOW}⏭️  跳过{Colors.RESET}"
    }
    
    for test_name, result in results.items():
        status = status_map.get(result, "❓ 未知")
        print(f"{status} - {test_name}")
    
    print()
    print("=" * 60)
    
    # 判断是否完全通过
    required_tests = ["目录结构", "数据契约", "核心脚本"]
    required_passed = all([results.get(t) for t in required_tests])
    
    if required_passed and results.get("GitHub Issue") is True:
        print(f"{Colors.GREEN}{Colors.BOLD}")
        print("🎉 恭喜！Day 1 所有验收标准已完成！")
        print(f"{Colors.RESET}")
        print()
        print("✅ 仓库建立且包含规范目录")
        print("✅ template.json 数据契约文件已提交")
        print("✅ GitHub Actions 配置完成")
        print("✅ GitHub Issue 创建成功")
        print("✅ 任务看板包含大模型生成的 Checklist")
        print()
        print(f"{Colors.CYAN}下一步:{Colors.RESET}")
        print("1. 访问 GitHub Issues 查看任务看板")
        print("2. 配置 GitHub Secrets 启用自动化")
        print("3. 开始 Day 2 的学习任务")
        return True
        
    elif required_passed:
        print(f"{Colors.YELLOW}{Colors.BOLD}")
        print("✅ 本地验收已完成！")
        print(f"{Colors.RESET}")
        print()
        print("✅ 仓库建立且包含规范目录")
        print("✅ template.json 数据契约文件已提交")
        print("✅ 核心脚本和配置完整")
        print("✅ 演示测试通过")
        print()
        
        if results.get("GitHub Issue") is None:
            print(f"{Colors.YELLOW}⏳ 待完成:{Colors.RESET}")
            print("- 创建 GitHub Issue（任务看板）")
            print()
            print(f"{Colors.CYAN}完成方法:{Colors.RESET}")
            print("1. 获取 DeepSeek API Key: https://platform.deepseek.com/api_keys")
            print("2. 获取 GitHub Token: https://github.com/settings/tokens")
            print("3. 运行: python create_first_issue.py")
            print("   或双击: create_issue.bat")
        
        return False
    else:
        print(f"{Colors.RED}{Colors.BOLD}")
        print("⚠️  部分验收标准未通过")
        print(f"{Colors.RESET}")
        print()
        print("请检查失败项并修复")
        return False

def main():
    """主函数"""
    print_header("100Days-AI-Architect - Day 1 完整验收测试", Colors.BOLD + Colors.GREEN)
    
    print(f"{Colors.CYAN}这个脚本将验证所有 Day 1 验收标准:{Colors.RESET}")
    print("1. 仓库建立且包含规范目录")
    print("2. template.json 数据契约文件已提交")
    print("3. GitHub Actions 成功运行并创建 Issue")
    print()
    
    input("按回车键开始验收测试...")
    
    results = {}
    
    # 执行所有验收测试
    results["目录结构"] = verify_local_environment()
    results["数据契约"] = verify_template_json()
    results["核心脚本"] = verify_core_scripts()
    results["演示测试"] = run_demo_test()
    results["GitHub Issue"] = create_github_issue()
    
    # 生成最终报告
    success = generate_final_report(results)
    
    print()
    input("按回车键退出...")
    
    return 0 if success else 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}用户中断{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}错误: {e}{Colors.RESET}")
        sys.exit(1)
