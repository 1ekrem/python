# from unittest import TestLoader, TestSuite
import unittest
import HtmlTestRunner
import datetime
from test_file import TestEmployee
from test_file2 import TestEmployee2

if __name__ == "__main__":
    
    loader = unittest.TestLoader()
    
    suite = unittest.TestSuite((
                    loader.loadTestsFromTestCase(TestEmployee),
                    loader.loadTestsFromTestCase(TestEmployee2)
                    ))

    unittest.main(verbosity=2 ,testRunner=HtmlTestRunner.HTMLTestRunner(output="./Bootcamp/zunittest/htmlreports"))