import unittest
import HtmlTestRunner
'''
unittest requires that:

You put your tests into classes as methods
You use a series of special assertion methods in the unittest.
TestCase class instead of the built-in assert statement
'''
class TestSum(unittest.TestCase):

    def test_sum1(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")

    def test_sum_tuple2(self):
        self.assertEqual(sum((1,2,3)), 6, "Should be 6")

# if __name__ == "__main__":
#     unittest.main(verbosity=2, testRunner=HtmlTestRunner.HTMLTestRunner(output="./testframework"))


def suite():
    SanityTestSuite = unittest.TestSuite()
    SanityTestSuite.addTest(TestSum('test_sum1'))

    # SmokeTestSuite = unittest.TestSuite()
    # SmokeTestSuite.addTest(TestSum("test_sum1"))
    # SmokeTestSuite.addTest(TestSum("test_sum_tuple2"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

