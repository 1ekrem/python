import math_funcc as m

def test_add():
    assert m.add(2, 4) == 6
    assert m.add(8) == 10
    assert m.add(1) == 3

def test_product():
    assert m.product(2, 4) == 8
    assert m.product(5) == 10
    assert m.product(12) == 24

def test_add_string():
    result = m.add('Hello', ' World')
    list2 = ['IA1', 'IA2', 'IO7']
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldlo' not in result
    assert 'IO7' in list2