import unittest

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("-" * 30)
        print("Class 1 -> class level setUp")
        print("-" * 30)

    def setUp(self):
        print("Class 2 -> setUp")

    def test_class2_method_A(self):
        print("Running class 2 -> method-A")
    
    def test_class2_method_B(self):
        print("Running class 2 -> method-B")
    
    def tearDown(self): # Cleans up any initialized values by the setUp method.
        print("Class 2 -> tearDown")
    
    @classmethod
    def tearDownClass(cls):
        print("-" * 30)
        print("I will only run once after all tests")
        print("-" * 30)

if __name__ == '__main__' :
    unittest.main(verbosity=0)