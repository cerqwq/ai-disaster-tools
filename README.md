# 🔄 AI Disaster Tools

AI灾难恢复工具，支持备份策略、恢复计划、业务连续性。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 备份策略设计
- 📝 恢复计划生成
- 🏢 业务连续性计划
- 🧪 DR测试计划
- ⏱️ 恢复时间估算
- 💻 备份脚本生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_disaster_tools import create_tools

tools = create_tools()

# 备份策略
backup = tools.design_backup_strategy(["数据库", "文件服务器"], "1小时")

# 恢复计划
recovery = tools.generate_recovery_plan("硬件故障", systems)

# 业务连续性
bcp = tools.design_business_continuity("科技公司")

# DR测试计划
test = tools.generate_dr_test_plan(systems)

# 恢复时间估算
estimates = tools.estimate_recovery_time(systems, scenarios)

# 备份脚本
script = tools.generate_backup_script("/data", "/backup", "rsync")
```

## 📁 项目结构

```
ai-disaster-tools/
├── tools.py       # 灾难恢复工具核心
└── README.md
```

## 📄 许可证

MIT License
