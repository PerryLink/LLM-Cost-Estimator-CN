"""工具函数模块"""
import json
from pathlib import Path
from typing import Dict


def load_models() -> Dict:
    """加载模型定价数据"""
    models_file = Path(__file__).parent / 'data' / 'models.json'
    with open(models_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def format_currency(amount: float) -> str:
    """格式化货币显示"""
    return f"¥{amount:.4f}"


def calculate_percentage_diff(value: float, baseline: float) -> str:
    """计算百分比差异"""
    if baseline == 0:
        return "N/A"

    if value == baseline:
        return "基准"

    diff_percent = ((value - baseline) / baseline) * 100
    return f"+{diff_percent:.1f}%"
