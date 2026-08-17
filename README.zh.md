<div align="center">

# LLM-Cost-Estimator-CN

**估算并对比国内主流大模型 API 成本的命令行工具。**

*已移植到 [dsh-budget](https://github.com/PerryLink/dsh-budget) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

`llm-cost-estimator-cn` 加载内置的国内主流大模型价格表（人民币 / 1K tokens，共 7 款模型），根据你预期
的输入与输出 token 数量计算输入、输出和总成本，并按总成本排序，同时显示与最便宜模型的差距百分比。

## 特性

- 对比 DeepSeek、百度文心、阿里通义、智谱 GLM、百川智能、月之暗面 Kimi 的 API 定价
- 基于 Rich 的美观交互式终端界面
- 支持直接输入 token 数量或交互式输入
- 成本排序，并显示与最低价的差距百分比
- 支持按模型名称关键词过滤、只显示前 N 个最便宜的模型

## 快速开始

```bash
pip install llm-cost-estimator-cn
```

## 使用方法

```bash
# 估算 1,000,000 输入 token、100,000 输出 token 的成本
llm-cost-estimator-cn --input-tokens 1000000 --output-tokens 100000

# 交互式模式（自动提示输入 token 数量）
llm-cost-estimator-cn

# 按模型名称关键词过滤
llm-cost-estimator-cn -i 1000000 -o 100000 --model deepseek

# 只显示前 5 个最便宜的模型
llm-cost-estimator-cn -i 1000000 -o 100000 --top 5
```

## 支持的模型

价格为人民币 / 1K tokens。

| 模型 | 提供商 | 输入 | 输出 |
|------|--------|------|------|
| `deepseek-chat` | DeepSeek | ¥0.001 | ¥0.002 |
| `ernie-4.0` | 百度 | ¥0.12 | ¥0.12 |
| `qwen-turbo` | 阿里云 | ¥0.008 | ¥0.008 |
| `qwen-plus` | 阿里云 | ¥0.04 | ¥0.04 |
| `glm-4` | 智谱AI | ¥0.1 | ¥0.1 |
| `baichuan2-turbo` | 百川智能 | ¥0.008 | ¥0.008 |
| `moonshot-v1-8k` | 月之暗面 | ¥0.012 | ¥0.012 |

## 开发

```bash
pip install -e ".[dev]"
pytest
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
