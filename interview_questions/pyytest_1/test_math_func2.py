"""
Pytest 3 - Parameterizing tests (pytest.mark.parametrize)
"""

import math_funcc as m
import pytest

@pytest.mark.parametrize('num1, num2, result',
            [
                (7, 3 , 10),
                ('Hello', ' World', 'Hello World'),
                (10.5, 25.5, 36)
            ]
            )
def test_add(num1, num2, result):
    assert m.add(num1, num2) == result
