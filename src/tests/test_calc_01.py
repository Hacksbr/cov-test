from src.main import calc_01
import pytest


@pytest.mark.parametrize('input,expected', [((2, 10), 12), ((3, 2), 5), ((5, 5), 10)])
def test_sum(input, expected):
    value_a, value_b = input
    result = calc_01.sum(value_a, value_b)
    assert result == expected


@pytest.mark.parametrize('input,expected', [((3, 2), 1), ((10, 5), 5), ((17, 7), 10)])
def test_subtraction(input, expected):
    value_a, value_b = input
    result = calc_01.subtraction(value_a, value_b)
    assert result == expected
