"""核心功能测试"""
import pytest
from llm_cost_estimator_cn.core import CostEstimator
from llm_cost_estimator_cn.utils import load_models, format_currency, calculate_percentage_diff


def test_load_models():
    """测试加载模型数据"""
    models = load_models()
    assert isinstance(models, dict)
    assert len(models) > 0
    assert 'deepseek-chat' in models


def test_format_currency():
    """测试货币格式化"""
    assert format_currency(1.2345) == "¥1.2345"
    assert format_currency(0.001) == "¥0.0010"
    assert format_currency(100) == "¥100.0000"


def test_calculate_percentage_diff():
    """测试百分比差异计算"""
    assert calculate_percentage_diff(100, 100) == "基准"
    assert calculate_percentage_diff(200, 100) == "+100.0%"
    assert calculate_percentage_diff(150, 100) == "+50.0%"
    assert calculate_percentage_diff(100, 0) == "N/A"


def test_cost_estimator_calculate():
    """测试成本计算"""
    models = load_models()
    estimator = CostEstimator(models)

    results = estimator.calculate_costs(1000000, 100000)

    assert len(results) > 0
    assert results[0]['total_cost'] <= results[-1]['total_cost']

    for result in results:
        assert 'model_id' in result
        assert 'provider' in result
        assert 'model_name' in result
        assert 'input_cost' in result
        assert 'output_cost' in result
        assert 'total_cost' in result
        assert result['total_cost'] == result['input_cost'] + result['output_cost']


def test_cost_calculation_accuracy():
    """测试成本计算准确性"""
    models = {
        'test-model': {
            'provider': 'Test',
            'name': 'Test Model',
            'input_price_per_1k': 0.001,
            'output_price_per_1k': 0.002,
            'currency': 'CNY'
        }
    }

    estimator = CostEstimator(models)
    results = estimator.calculate_costs(1000, 1000)

    assert len(results) == 1
    assert results[0]['input_cost'] == 0.001
    assert results[0]['output_cost'] == 0.002
    assert results[0]['total_cost'] == 0.003
