import unittest
import HtmlTestRunner

class TestingFramework(unittest.TestCase):

    def setUp(self):
        print("setUp - Expected to be - 1 ")
    
    def test_1(self):
        x=5
        y=6
        if x !=y:
            print("{} NOT EQUALS {}".format(x,y))
        self.assertNotEqual(x,y)
    
    def test_2(self):
        fname = "Ekrem"
        lname = "Ersay"
        age = 28
        self.assertNotEqual(fname, lname, msg="This is expected to be the first name {} and the last name is {}".format(fname, lname))
        self.assertEqual(age, 28)

    def test_3(self):
        x="Hello"
        y="hellO"
        self.assertEqual(x.lower(),y.lower(), msg="Upper/Lower case issue")

    def tearDown(self):
        print("tearDown - Expected to be last one - 5")


def suite():
    smokeTestSuite = unittest.TestSuite()
    smokeTestSuite.addTest(TestingFramework("test_1"))
    smokeTestSuite.addTest(TestingFramework("test_2"))

    # sanityTestSuite = unittest.TestSuite()
    # sanityTestSuite.addTest(TestingFramework("test_1"))
    # sanityTestSuite.addTest(TestingFramework("test_2"))
    # sanityTestSuite.addTest(TestingFramework("test_3"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./testframework/Examples/unittest"))