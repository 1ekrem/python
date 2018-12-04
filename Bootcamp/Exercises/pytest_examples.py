import pytest

def gtzero(number):
    return number >= 0

def test_tc1():
    assert gtzero(5) is True

def test_tc2():
    assert gtzero(-1) is True

def test_tc3():
    assert gtzero(3) is True

def test_tc4():
    assert gtzero(2) is True

def test_tc5():    
    assert gtzero(-5) is False

def test_tc6():
    assert 1 == 1