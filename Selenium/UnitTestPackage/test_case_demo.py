import unittest

class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print("setUp Method")

    def test_method_A(self):
        print("Running method-A")
    
    def test_method_B(self):
        print("Running method-B")
    
    def tearDown(self): # Cleans up any initialized values by the setUp method.
        print("tearDown Method")

if __name__ == '__main__' :
    unittest.main(verbosity=1)

"""
What is verbosity:
You only have 3 different levels:

0 (quiet): you just get the total numbers 
            of tests executed and the global result
1 (default): you get the same plus a dot for every successful test 
            or a F for every failure
2 (verbose): you get the help string of every test and the result
You can use command line args rather than the verbosity argument: 
--quiet and --verbose which would do something similar to passing 0 or 2 to the runner.
"""