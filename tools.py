"""
AI Disaster Tools - AI灾难恢复工具
支持备份策略、恢复计划、业务连续性
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDisasterTools:
    """
    AI灾难恢复工具
    支持：备份、恢复、连续性
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_backup_strategy(self, systems: List[str], rpo: str) -> Dict:
        """设计备份策略"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        systems_text = ", ".join(systems)

        prompt = f"""请设计备份策略：

系统：{systems_text}
RPO：{rpo}

请返回JSON格式：
{{
    "backup_types": ["备份类型"],
    "schedule": "备份计划",
    "retention": "保留策略",
    "storage": "存储方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"backup": content}

    def generate_recovery_plan(self, disaster_type: str, systems: List[str]) -> str:
        """生成恢复计划"""
        if not self.client:
            return "LLM客户端未配置"

        systems_text = "\n".join(f"- {s}" for s in systems)

        prompt = f"""请为{disaster_type}生成恢复计划：

受影响系统：
{systems_text}

要求：
1. 详细步骤
2. 优先级排序
3. 预计时间"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_business_continuity(self, organization: str) -> Dict:
        """设计业务连续性计划"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{organization}设计业务连续性计划：

请返回JSON格式：
{{
    "critical_functions": ["关键功能"],
    "recovery_priorities": ["恢复优先级"],
    "communication_plan": "沟通计划",
    "alternate_sites": ["备用站点"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"bcp": content}

    def generate_dr_test_plan(self, systems: List[str]) -> Dict:
        """生成DR测试计划"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        systems_text = ", ".join(systems)

        prompt = f"""请生成灾难恢复测试计划：

系统：{systems_text}

请返回JSON格式：
{{
    "test_types": ["测试类型"],
    "schedule": "测试计划",
    "scenarios": ["测试场景"],
    "success_criteria": ["成功标准"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"test_plan": content}

    def estimate_recovery_time(self, systems: List[str], scenarios: List[str]) -> Dict:
        """估算恢复时间"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        systems_text = ", ".join(systems)
        scenarios_text = ", ".join(scenarios)

        prompt = f"""请估算恢复时间：

系统：{systems_text}
场景：{scenarios_text}

请返回JSON格式：
{{
    "estimates": [
        {{"scenario": "场景", "rto": "恢复时间", "rpo": "恢复点"}}
    ],
    "bottlenecks": ["瓶颈"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"estimates": content}

    def generate_backup_script(self, source: str, destination: str, tool: str = "rsync") -> str:
        """生成备份脚本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{tool}备份脚本：

源：{source}
目标：{destination}

要求：
1. 完整脚本
2. 错误处理
3. 日志记录"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIDisasterTools:
    """创建灾难恢复工具"""
    return AIDisasterTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Disaster Tools")
    print()

    # 测试
    backup = tools.design_backup_strategy(["数据库", "文件服务器"], "1小时")
    print(json.dumps(backup, ensure_ascii=False, indent=2))
