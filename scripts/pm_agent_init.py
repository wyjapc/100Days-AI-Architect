#!/usr/bin/env python3
"""
PM Agent - 自动化任务生成引擎
每日自动读取 tracker 配置，调用 LLM 生成任务，并创建 GitHub Issue
"""

import os
import json
import sys
from datetime import datetime
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

def call_llm(system_prompt, user_message):
    """调用 LLM API 生成任务清单"""
    # 优先使用 OpenAI (更便宜快速的 GPT-3.5)
    openai_key = os.getenv('OPENAI_API_KEY')
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    
    if openai_key:
        return call_openai(system_prompt, user_message, openai_key)
    elif anthropic_key:
        return call_anthropic(system_prompt, user_message, anthropic_key)
    else:
        raise ValueError("未找到 API Key。请设置 OPENAI_API_KEY 或 ANTHROPIC_API_KEY 环境变量")

def call_openai(system_prompt, user_message, api_key):
    """调用 OpenAI API"""
    import requests
    
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
        }
    )
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

def call_anthropic(system_prompt, user_message, api_key):
    """调用 Anthropic API"""
    import requests
    
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
        }
    )
    response.raise_for_status()
    return response.json()['content'][0]['text']

def create_github_issue(title, body):
    """通过 GitHub API 创建 Issue"""
    import requests
    
    token = os.getenv('GH_TOKEN')
    repo = os.getenv('GITHUB_REPOSITORY')  # 格式: owner/repo
    
    if not token or not repo:
        raise ValueError("未找到 GH_TOKEN 或 GITHUB_REPOSITORY 环境变量")
    
    response = requests.post(
        f'https://api.github.com/repos/{repo}/issues',
        headers={
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        },
        json={
            'title': title,
            'body': body,
            'labels': ['daily-task', 'auto-generated']
        }
    )
    response.raise_for_status()
    return response.json()

def main():
    """主执行流程"""
    try:
        # 1. 加载配置和提示词
        template = load_template()
        system_prompt = load_system_prompt()
        
        # 2. 构建用户消息
        user_message = f"""
请为以下配置生成今日任务清单：

```json
{json.dumps(template, ensure_ascii=False, indent=2)}
```

请生成 3-5 个具体的、可执行的任务项。
"""
        
        # 3. 调用 LLM 生成任务
        print("正在调用 LLM 生成任务清单...")
        task_content = call_llm(system_prompt, user_message)
        print(f"任务生成成功:\n{task_content}\n")
        
        # 4. 创建 GitHub Issue
        issue_title = f"Day {template['day']} - {template['date']} 任务看板"
        print(f"正在创建 GitHub Issue: {issue_title}")
        issue = create_github_issue(issue_title, task_content)
        
        print(f"✅ Issue 创建成功: {issue['html_url']}")
        return 0
        
    except Exception as e:
        print(f"❌ 执行失败: {str(e)}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
