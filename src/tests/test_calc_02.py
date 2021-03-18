from src.main import calc_02
import pytest


@pytest.mark.parametrize('input,expected', [((10, 2), 5), ((4, 2), 2), ((5, 5), 1)])
def test_division(input, expected):
    value_a, value_b = input
    result = calc_02.division(value_a, value_b)
    assert result == expected


@pytest.mark.parametrize('input,expected', [((2, 10), 20), ((3, 2), 6), ((5, 5), 25)])
def test_multiplication(input, expected):
    value_a, value_b = input
    result = calc_02.multiplication(value_a, value_b)
    assert result == expected
