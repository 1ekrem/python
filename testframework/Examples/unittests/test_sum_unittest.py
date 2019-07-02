import unittest
'''
unittest requires that:

You put your tests into classes as methods
You use a series of special assertion methods in the unittest.
TestCase class instead of the built-in assert statement
'''
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,3)), 6, "Should be 6")

if __name__ == "__main__":
    unittest.main()