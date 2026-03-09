"""命令行接口模块"""
import click
from rich.console import Console
from .core import CostEstimator
from .utils import load_models

console = Console()


@click.command()
@click.option('--input-tokens', '-i', type=int, help='输入 token 数量')
@click.option('--output-tokens', '-o', type=int, help='输出 token 数量')
@click.option('--model', '-m', help='指定模型名称（可选）')
@click.option('--top', '-t', type=int, default=10, help='显示前 N 个最便宜的模型')
def main(input_tokens, output_tokens, model, top):
    """国内主流 LLM 模型成本估算工具"""

    if not input_tokens or not output_tokens:
        input_tokens = click.prompt('请输入预计的输入 token 数量', type=int)
        output_tokens = click.prompt('请输入预计的输出 token 数量', type=int)

    models = load_models()
    estimator = CostEstimator(models)
    results = estimator.calculate_costs(input_tokens, output_tokens)
    estimator.display_results(results, top=top, filter_model=model)


if __name__ == '__main__':
    main()
