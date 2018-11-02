import pytest

@pytest.yield_fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")

def test_methodA(setUp):
    print("Running Method A")

def test_methodB(setUp):
    print("Running Method B")