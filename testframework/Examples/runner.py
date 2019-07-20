import unittest
import HtmlTestRunner

from testframework.Examples.unittests.test_sum_unittest import TestSum

def suite():
    SanityTestSuite = unittest.TestSuite()
    SanityTestSuite.addTest(TestSum('test_sum1'))
    SanityTestSuite.addTest(TestSum(''))    

    # SmokeTestSuite = unittest.TestSuite()
    # SmokeTestSuite.addTest(TestSum("test_sum1"))
    # SmokeTestSuite.addTest(TestSum("test_sum_tuple2"))
    return suite

if __name__ == "__main__":
    suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(suite())


