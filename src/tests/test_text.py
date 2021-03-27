from src.main import text
import pytest


@pytest.mark.parametrize('input,expected', [('a', 'aaa'), ('b', 'bbb'), ('c', 'ccc')])
def test_text_xxx(input, expected):
    result = text.text_xxx(input)
    assert result == expected


@pytest.mark.parametrize('input,expected', [('a', 'aaaa'), ('b', 'bbbb'), ('c', 'cccc')])
def test_text_xxxx(input, expected):
    result = text.text_xxxx(input)
    assert result == expected
