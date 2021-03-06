import unittest
import HtmlTestRunner

class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("-" * 30)
        print("Class 1 -> class level setUp")
        print("-" * 30)

    def setUp(self):
        print("Class 1 -> setUp")

    def test_class1_method_A(self):
        print("Running class 1 -> method-A")
    
    def test_class1_method_B(self):
        print("Running class 1 -> method-B")
    
    def tearDown(self): # Cleans up any initialized values by the setUp method.
        print("Class 1 -> tearDown")
    
    @classmethod
    def tearDownClass(cls):
        print("-" * 30)
        print("I will only run once after all tests")
        print("-" * 30)

if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports"))

