import math_funcc as m
import pytest
import sys

#How to skip a test @pytest.mark.skip(reason= "do not run number add test")
@pytest.mark.skipif(sys.version_info < (3, 3), reason= "do not run number add test")
def test_add():
    assert m.add(2, 4) == 6
    assert m.add(8) == 10
    assert m.add(1) == 3

@pytest.mark.number
def test_product():
    assert m.product(2, 4) == 8
    assert m.product(5) == 10
    assert m.product(12) == 24

@pytest.mark.strings
def test_add_string():
    result = m.add('Hello', ' World')
    list2 = ['IA1', 'IA2', 'IO7']
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldlo' not in result
    assert 'IO7' in list2