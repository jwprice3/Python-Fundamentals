# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: test presentation classes
# Change Log: (Who, When, What)
#   JP,11JUN24,Created Script
# ------------------------------------------------------------------------------------------ #


import unittest
from unittest.mock import patch
from presentation_classes import IO

class TestIO(unittest.TestCase):
    def setUp(self):
        self.student_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('presentation_classes.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    # def test_input_student_data(self):
    #     # Simulate user input for student data
    #     with patch('builtins.input', side_effect=['John', 'Doe', '3.5']):
    #         IO.input_student_data(self.student_data)
    #         self.assertEqual(len(self.student_data), 1)
    #         self.assertEqual(self.student_data[0].first_name, 'John')
    #         self.assertEqual(self.student_data[0].last_name, 'Doe')
    #         self.assertEqual(self.student_data[0].gpa, 3.5)

    #     # Simulate invalid GPA input (not a float)
    #     with patch('builtins.input', side_effect=['Alice', 'Smith', 'invalid']):
    #         IO.input_student_data(self.student_data)
    #         self.assertEqual(len(self.student_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()