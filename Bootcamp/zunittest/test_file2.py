import unittest
import HtmlTestRunner

from employee import Employee

class TestEmployee2(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("setupClass")
    
    # @classmethod
    # def tearDownClass(cls):
    #     print("tearDownClass")

    def setUp(self):
        print("Setup")
        self.emp_1 = Employee("2Ekrem", "Ersayin", 50000)
        self.emp_2 = Employee("2John", "Brick", 60000)    
    
    def tearDown(self):
        print('tearDown\n')

    def test_email2(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, '2EkremErsayin@email.com')
        self.assertEqual(self.emp_2.email, "2JohnBrick@email.com")

        self.emp_1.fname = '2Kerem'
        self.emp_2.fname = '2Jane'

        self.assertEqual(self.emp_1.email, "2KeremErsayin@email.com")
        self.assertEqual(self.emp_2.email, "2JaneBrick@email.com")

    def test_fullname2(self):
        print("test_fullname")
        self.emp_1 = Employee("Ekrem","Ersayin", 50000)
        self.emp_2 = Employee("John", "Brick", 60000)

        self.assertEqual(self.emp_1.fullname, "Ekrem Ersayin")
        self.assertEqual(self.emp_2.fullname, "John Brick")

        self.emp_1.fname = "Kerem"
        self.emp_2.fname = "Jane"

        self.assertEqual(self.emp_1.fullname, "Kerem Ersayin")
        self.assertEqual(self.emp_2.fullname, "Jane Brick")

    def test_apply_raise2(self):
        print("test_apply_raise")
        self.emp_1 = Employee("Ekrem","Ersayin", 50000)
        self.emp_2 = Employee("John", "Brick", 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

# if __name__ == "__main__":
#     unittest.main(verbosity=2 ,testRunner=HtmlTestRunner.HTMLTestRunner(output="./zunittest/htmlreports"))