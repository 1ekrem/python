import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not True")

        b= False
        self.assertFalse(b,"b is not False")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a,b,"'a' is not equal to 'b'")

    def test_assertNotEqual(self):
        x="Test"
        y="Test"
        self.assertNotEqual(x,y,"x is equal to Y")

if __name__ == '__main__':
    unittest.main(verbosity=2)