# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: processing classes test
# Change Log: (Who, When, What)
#   JP,11JUN24,Created Script
# ------------------------------------------------------------------------------------------ #

import unittest
import tempfile
import json
from data_classes import Employee
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data_test = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            [{"FirstName": "Cho", "LastName": "Chang", "ReviewDate": "1979-04-07", "ReviewRating": "4"}]
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data_test, data.Employee)

        # Assert that the student_data list contains the expected student objects
        self.assertEqual(len(self.employee_data_test), len(sample_data))
        self.assertEqual(self.employee_data_test[0].first_name, "Cho")
        self.assertEqual(self.employee_data_test[0].last_name, "Chang")
        self.assertEqual(self.employee_data_test[0].review_date, "1979-04-07")
        self.assertEqual(self.employee_data_test[0].review_rating, "4")

    def test_write_data_to_file(self):
        # Create some sample student objects
        sample_data = [
            [{"FirstName": "Gellert", "LastName": "Grindlewald", "ReviewDate": "1882-03-08", "ReviewRating": "4"}]
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, self.employee_data_test, self.Employee)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(self.employee_data_test), len(sample_data))
        self.assertEqual(self.employee_data_test[0].first_name, "Gellert")
        self.assertEqual(self.employee_data_test[0].last_name, "Grindlewald")
        self.assertEqual(self.employee_data_test[0].review_date, "1882-03-08")
        self.assertEqual(self.employee_data_test[0].review_rating, "4")

if __name__ == "__main__":
    unittest.main()
