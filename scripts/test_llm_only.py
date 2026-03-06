#!/usr/bin/env python3
"""
仅测试 LLM 调用（不创建 GitHub Issue）
用于快速验证 API Key 和 LLM 响应
"""

import os
import json
import sys
from pathlib import Path

def load_template():
    """加载每日任务模板"""
    template_path = Path(__file__).parent.parent / "tracker" / "template.json"
    with open(template_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_system_prompt():
    """加载 PM Agent 系统提示词"""
    prompt_path = Path(__file__).parent.parent / "prompts" / "pm_agent_system.md"
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

def call_deepseek(system_prompt, user_message, api_key):
    """调用 DeepSeek API"""
    import requests
    
    print("🤖 正在调用 DeepSeek API (deepseek-chat)...")
    response = requests.post(
        'https://api.deepseek.com/v1/chat/completions',
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'deepseek-chat',
            'messages': [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7
        },
        timeout=30
    )
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

def call_openai(system_prompt, user_message, api_key):
    """调用 OpenAI API"""
    import requests
    
    print("🤖 正在调用 OpenAI API (gpt-3.5-turbo)...")
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_message}
            ],
            'temperature': 0.7
        },
        timeout=30
    )
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

def call_anthropic(system_prompt, user_message, api_key):
    """调用 Anthropic API"""
    import requests
    
    print("🤖 正在调用 Anthropic API (claude-3-haiku)...")
    response = requests.post(
        'https://api.anthropic.com/v1/messages',
        headers={
            'x-api-key': api_key,
            'anthropic-version': '2023-06-01',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'claude-3-haiku-20240307',
            'max_tokens': 1024,
            'system': system_prompt,
            'messages': [
                {'role': 'user', 'content': user_message}
            ]
        },
        timeout=30
    )
    response.raise_for_status()
    return response.json()['content'][0]['text']

def main():
    print("=" * 60)
    print("PM Agent - LLM 测试（不创建 GitHub Issue）")
    print("=" * 60)
    
    # 检查 API Key
    deepseek_key = os.getenv('DEEPSEEK_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    
    if not deepseek_key and not openai_key and not anthropic_key:
        print("\n⚠️  未检测到 API Key 环境变量")
        print("\n请选择一个选项:")
        print("1. 输入 DeepSeek API Key (推荐，最便宜)")
        print("2. 输入 OpenAI API Key")
        print("3. 输入 Anthropic API Key")
        print("4. 退出")
        
        choice = input("\n请选择 (1/2/3/4): ").strip()
        
        if choice == '1':
            deepseek_key = input("请输入 DeepSeek API Key: ").strip()
            if not deepseek_key:
                print("❌ 未输入 API Key")
                return 1
        elif choice == '2':
            openai_key = input("请输入 OpenAI API Key: ").strip()
            if not openai_key:
                print("❌ 未输入 API Key")
                return 1
        elif choice == '3':
            anthropic_key = input("请输入 Anthropic API Key: ").strip()
            if not anthropic_key:
                print("❌ 未输入 API Key")
                return 1
        else:
            print("退出")
            return 0
    
    try:
        # 1. 加载配置
        print("\n📄 加载配置...")
        template = load_template()
        print(f"   Day: {template['day']}")
        print(f"   Date: {template['date']}")
        print(f"   Topic: {template['topic']}")
        
        # 2. 加载提示词
        print("\n📝 加载系统提示词...")
        system_prompt = load_system_prompt()
        print(f"   提示词长度: {len(system_prompt)} 字符")
        
        # 3. 构建用户消息
        user_message = f"""
请为以下配置生成今日任务清单：

```json
{json.dumps(template, ensure_ascii=False, indent=2)}
```

请生成 3-5 个具体的、可执行的任务项。
"""
        
        # 4. 调用 LLM
        print("\n🚀 调用 LLM API...")
        if deepseek_key:
            task_content = call_deepseek(system_prompt, user_message, deepseek_key)
        elif openai_key:
            task_content = call_openai(system_prompt, user_message, openai_key)
        else:
            task_content = call_anthropic(system_prompt, user_message, anthropic_key)
        
        # 5. 显示结果
        print("\n" + "=" * 60)
        print("✅ LLM 响应成功！")
        print("=" * 60)
        print("\n生成的任务清单:\n")
        print(task_content)
        print("\n" + "=" * 60)
        
        # 6. 保存到文件
        output_path = Path(__file__).parent.parent / f"tracker/day-{template['day']}-output.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(task_content)
        print(f"\n💾 任务清单已保存到: {output_path}")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ 执行失败: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
