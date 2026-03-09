"""核心成本计算逻辑"""
import sys
from typing import List, Dict, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from .utils import format_currency, calculate_percentage_diff

# 修复 Windows 终端编码问题
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

console = Console()


class CostEstimator:
    """LLM 成本估算器"""

    def __init__(self, models: Dict):
        self.models = models

    def calculate_costs(self, input_tokens: int, output_tokens: int) -> List[Dict]:
        """
        计算所有模型的成本

        Args:
            input_tokens: 输入 token 数量
            output_tokens: 输出 token 数量

        Returns:
            排序后的成本列表
        """
        results = []

        for model_id, model_info in self.models.items():
            input_cost = (input_tokens / 1000) * model_info['input_price_per_1k']
            output_cost = (output_tokens / 1000) * model_info['output_price_per_1k']
            total_cost = input_cost + output_cost

            results.append({
                'model_id': model_id,
                'provider': model_info['provider'],
                'model_name': model_info['name'],
                'input_cost': input_cost,
                'output_cost': output_cost,
                'total_cost': total_cost,
            })

        results.sort(key=lambda x: x['total_cost'])

        return results

    def display_results(self, results: List[Dict], top: int = 10, filter_model: Optional[str] = None):
        """
        显示成本对比结果

        Args:
            results: 计算结果列表
            top: 显示前 N 个结果
            filter_model: 过滤特定模型
        """
        if filter_model:
            results = [r for r in results if filter_model.lower() in r['model_name'].lower()]

        table = Table(title="国内 LLM 模型成本对比", show_header=True, header_style="bold magenta")
        table.add_column("排名", style="cyan", justify="center", width=6)
        table.add_column("提供商", style="green")
        table.add_column("模型名称", style="yellow")
        table.add_column("输入成本", justify="right")
        table.add_column("输出成本", justify="right")
        table.add_column("总成本", justify="right", style="bold")
        table.add_column("相比最低", justify="right")

        min_cost = results[0]['total_cost'] if results else 0

        for idx, result in enumerate(results[:top], 1):
            percentage_diff = calculate_percentage_diff(result['total_cost'], min_cost)
            style = "bold green" if idx == 1 else ""

            table.add_row(
                f"#{idx}",
                result['provider'],
                result['model_name'],
                format_currency(result['input_cost']),
                format_currency(result['output_cost']),
                format_currency(result['total_cost']),
                percentage_diff,
                style=style
            )

        console.print()
        console.print(table)
        console.print()

        if len(results) >= 2:
            cheapest = results[0]
            most_expensive = results[-1]
            savings = most_expensive['total_cost'] - cheapest['total_cost']
            savings_percent = ((most_expensive['total_cost'] - cheapest['total_cost']) / most_expensive['total_cost']) * 100

            tip = f"💡 使用 [bold green]{cheapest['model_name']}[/bold green] 相比 [bold red]{most_expensive['model_name']}[/bold red] 可节省 [bold yellow]{format_currency(savings)}[/bold yellow] ({savings_percent:.1f}%)"
            console.print(Panel(tip, style="green", title="省钱提示"))
