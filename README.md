# llm-cost-estimator-cn

> A CLI tool for estimating and comparing API costs of mainstream Chinese LLM models

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-llm--cost--estimator--cn-orange)](https://pypi.org/project/llm-cost-estimator-cn/)

---

## Features

- Compare API pricing across mainstream Chinese LLM providers (DeepSeek, Qwen, ERNIE, GLM, Kimi, Baichuan, etc.)
- Interactive CLI with beautiful terminal output powered by Rich
- Supports direct token count input or interactive prompting
- Real-time cost ranking with percentage comparison to the cheapest option
- Filter results by model name keyword
- Show top-N cheapest models

## Quick Start

**Install from PyPI:**

```bash
pip install llm-cost-estimator-cn
```

**Install from source:**

```bash
git clone https://github.com/PerryLink/llm-cost-estimator-cn.git
cd llm-cost-estimator-cn
pip install -e .
```

## Usage

**Basic usage:**

```bash
llm-cost-estimator-cn --input-tokens 1000000 --output-tokens 100000
```

**Interactive mode (prompts for token counts):**

```bash
llm-cost-estimator-cn
```

**Filter by model name keyword:**

```bash
llm-cost-estimator-cn -i 1000000 -o 100000 --model deepseek
```

**Show top N cheapest models:**

```bash
llm-cost-estimator-cn -i 1000000 -o 100000 --top 5
```

**Example output:**

```
                    国内 LLM 模型成本对比
┏━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃ 排名 ┃ 提供商 ┃ 模型名称      ┃ 输入成本 ┃ 输出成本 ┃ 总成本   ┃ 相比最低 ┃
┡━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│  #1  │DeepSeek│DeepSeek Chat  │  ¥1.0000 │  ¥2.0000 │  ¥3.0000 │   基准   │
│  #2  │阿里云  │通义千问 Turbo │  ¥8.0000 │  ¥8.0000 │ ¥16.0000 │ +433.3%  │
│  #3  │百川智能│百川2-Turbo    │  ¥8.0000 │  ¥8.0000 │ ¥16.0000 │ +433.3%  │
└──────┴────────┴───────────────┴──────────┴──────────┴──────────┴──────────┘

╭─────────────────────────── 省钱提示 ───────────────────────────╮
│ 💡 使用 DeepSeek Chat 相比 文心一言 4.0 可节省 ¥117.0000 (97.5%) │
╰────────────────────────────────────────────────────────────────╯
```

## Project Structure

```
llm-cost-estimator-cn/
├── src/
│   └── llm_cost_estimator_cn/
│       ├── __init__.py       # Package entry, version
│       ├── __main__.py       # python -m support
│       ├── cli.py            # Click CLI definition
│       ├── core.py           # Cost calculation logic
│       ├── utils.py          # Helper utilities
│       └── data/             # Model pricing data
├── tests/
│   └── test_core.py          # Unit tests
├── pyproject.toml            # Build configuration
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## Tech Stack

| Component | Library |
|-----------|---------|
| CLI framework | [Click](https://click.palletsprojects.com/) |
| Terminal UI | [Rich](https://github.com/Textualize/rich) |
| Build system | [setuptools](https://setuptools.pypa.io/) |
| Testing | [pytest](https://pytest.org/) |
| Linting | [Ruff](https://github.com/astral-sh/ruff) |
| Formatting | [Black](https://github.com/psf/black) |

## License

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

---

# llm-cost-estimator-cn

> 国内主流 LLM 模型 API 成本估算与对比命令行工具

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![PyPI](https://img.shields.io/badge/pypi-llm--cost--estimator--cn-orange)](https://pypi.org/project/llm-cost-estimator-cn/)

---

## 核心特性

- 对比国内主流 LLM 提供商的 API 定价（DeepSeek、通义千问、文心一言、智谱 GLM、Kimi、百川等）
- 基于 Rich 库的美观终端界面
- 支持直接输入 token 数量或交互式输入
- 实时成本排序，并显示与最低价的差距百分比
- 支持按模型名称关键词过滤
- 支持只显示前 N 个最便宜的模型

## 快速开始

**从 PyPI 安装：**

```bash
pip install llm-cost-estimator-cn
```

**从源码安装：**

```bash
git clone https://github.com/PerryLink/llm-cost-estimator-cn.git
cd llm-cost-estimator-cn
pip install -e .
```

## 使用指南

**基本用法：**

```bash
llm-cost-estimator-cn --input-tokens 1000000 --output-tokens 100000
```

**交互式模式（自动提示输入 token 数量）：**

```bash
llm-cost-estimator-cn
```

**按模型名称关键词过滤：**

```bash
llm-cost-estimator-cn -i 1000000 -o 100000 --model deepseek
```

**只显示前 N 个最便宜的模型：**

```bash
llm-cost-estimator-cn -i 1000000 -o 100000 --top 5
```

## 项目结构

```
llm-cost-estimator-cn/
├── src/
│   └── llm_cost_estimator_cn/
│       ├── __init__.py       # 包入口，版本号
│       ├── __main__.py       # 支持 python -m 运行
│       ├── cli.py            # Click CLI 定义
│       ├── core.py           # 成本计算核心逻辑
│       ├── utils.py          # 辅助工具函数
│       └── data/             # 模型定价数据
├── tests/
│   └── test_core.py          # 单元测试
├── pyproject.toml            # 构建配置
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## 技术栈

| 组件 | 库 |
|------|----|
| CLI 框架 | [Click](https://click.palletsprojects.com/) |
| 终端 UI | [Rich](https://github.com/Textualize/rich) |
| 构建系统 | [setuptools](https://setuptools.pypa.io/) |
| 测试 | [pytest](https://pytest.org/) |
| 代码检查 | [Ruff](https://github.com/astral-sh/ruff) |
| 代码格式化 | [Black](https://github.com/psf/black) |

## 许可证

版权所有 2026 Chance Dean (novelnexusai@outlook.com)

本项目基于 Apache License 2.0 授权，详见 [LICENSE](LICENSE) 文件。
