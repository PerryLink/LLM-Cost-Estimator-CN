<div align="center">

# LLM-Cost-Estimator-CN

**A CLI tool for estimating and comparing API costs of mainstream Chinese LLM models.**

*Ported into [dsh-budget](https://github.com/PerryLink/dsh-budget) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

`llm-cost-estimator-cn` loads a built-in price table (CNY per 1K tokens) for seven mainstream Chinese
LLM models, computes the input, output, and total cost for your expected token counts, and ranks the
models by total cost, showing the percentage difference from the cheapest option.

## Features

- Compare API pricing across DeepSeek, 百度文心, 阿里通义, 智谱 GLM, 百川智能, and 月之暗面 Kimi
- Interactive CLI with Rich-formatted terminal output
- Direct token-count input or interactive prompting
- Cost ranking with percentage vs. the cheapest model
- Filter by model-name keyword and show the top-N cheapest models

## Quick start

```bash
pip install llm-cost-estimator-cn
```

## Usage

```bash
# Estimate cost for 1,000,000 input and 100,000 output tokens
llm-cost-estimator-cn --input-tokens 1000000 --output-tokens 100000

# Interactive mode (prompts for token counts)
llm-cost-estimator-cn

# Filter by model-name keyword
llm-cost-estimator-cn -i 1000000 -o 100000 --model deepseek

# Show only the top 5 cheapest models
llm-cost-estimator-cn -i 1000000 -o 100000 --top 5
```

## Supported models

Prices are in CNY per 1K tokens.

| Model | Provider | Input | Output |
|-------|----------|-------|--------|
| `deepseek-chat` | DeepSeek | ¥0.001 | ¥0.002 |
| `ernie-4.0` | 百度 | ¥0.12 | ¥0.12 |
| `qwen-turbo` | 阿里云 | ¥0.008 | ¥0.008 |
| `qwen-plus` | 阿里云 | ¥0.04 | ¥0.04 |
| `glm-4` | 智谱AI | ¥0.1 | ¥0.1 |
| `baichuan2-turbo` | 百川智能 | ¥0.008 | ¥0.008 |
| `moonshot-v1-8k` | 月之暗面 | ¥0.012 | ¥0.012 |

## Development

```bash
pip install -e ".[dev]"
pytest
```

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
