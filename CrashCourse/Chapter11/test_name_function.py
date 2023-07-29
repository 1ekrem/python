import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""
    
    def test_first_last_name(self):
        """Do name like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('Ekrem', 'Ersayin')
        self.assertEqual(formatted_name, 'Ekrem Ersayin')
        
unittest.main()