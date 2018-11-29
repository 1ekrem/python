import pytest

def gtzero(number):
    return number >= 0

def test_greater_than_zero():
    assert gtzero(5) is True
    # assert gtzero(-1) is True
    assert gtzero(3) is True
    assert gtzero(2) is True
    # assert gtzero(-5) is True
