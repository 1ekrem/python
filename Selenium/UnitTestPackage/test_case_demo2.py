import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("I will only run once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("setUp Method")

    def test_method_A(self):
        print("Running method-A")
    
    def test_method_B(self):
        print("Running method-B")
    
    def tearDown(self): # Cleans up any initialized values by the setUp method.
        print("tearDown Method")
    
    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will only run once after all tests")
        print("*#" * 30)

if __name__ == '__main__' :
    unittest.main(verbosity=0)
