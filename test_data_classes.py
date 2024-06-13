# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: Data classes test
# Change Log: (Who, When, What)
#   JP,11JUN24,Created Script
# ------------------------------------------------------------------------------------------ #

import unittest
from data_classes import Person

class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("Harry", "Potter")
        self.assertEqual(person.first_name, "Harry")
        self.assertEqual(person.last_name, "Potter")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Hagrid")
        with self.assertRaises(ValueError):
            person = Person("Ronald", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("Hermoine", "Granger")
        self.assertEqual(str(person), "Hermoine,Granger")

if __name__ == '__main__':
    unittest.main()
