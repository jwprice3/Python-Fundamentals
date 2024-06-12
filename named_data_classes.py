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
    - JP, 11JUN24: Created the class.
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
    
class Employee(Person):
    """
    A class representing employee data.

    Properties:
    - employee_first_name (str): The person's first name.
    - employee_last_name(str): The person's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    - JP, 11JUN24: Created the class..
    """

    def __init__(self, employee_first_name: str = "", employee_last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):

        super().__init__(employee_first_namet_name=employee_first_name,employee_last_name=employee_last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    def __str__(self):
        return f"{self.employee_first_name},{self.employee_last_name},{self.review_date},{self.__review_rating}"