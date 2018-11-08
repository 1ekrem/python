"""
file name should start with test
test method name should start with test

py.test     test_mod.py                     #run tests in module
py.test     somepath                        #run all tests below somepath
py.test     test_module.py::test_method     # only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("Running demo3 setUp")
    yield
    print("Running demo3 tearDown")

def test_demo3_method_A(setUp):
    print("Running demo3 Method A")
    a = 4
    if a != 4:
        print("a is not equal to 4")


def test_demo3_method_B(setUp):
    print("Running demo3 Method B")

