# ------------------------------------------------------------------------------------------ #
# Title: named data classes
# Desc: classes for People and employee
# Change Log: (Who, When, What)
#   JP,11JUN24,Created Script
# ------------------------------------------------------------------------------------------ #

class Person:
    """
    A class representing person data.

    Properties:
    - employee_first_name (str): The person's first name.
    - employee_last_name(str): The person's last name.

    ChangeLog:
    - RRoot, 1.1.2030: Created the class.
    """

    def __init__(self, employee_first_name: str = "", employee_last_name: str = ""):
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name

    @property
    def employee_first_name(self):
        return self.__employee_first_name.title()

    @employee_first_name.setter
    def employee_first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__employee_first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    def employee_last_name(self):
        return self.__employee_last_name.title()

    @employee_last_name.setter
    def employee_last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__employee_last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f"{self.employee_first_name},{self.employee_last_name}"