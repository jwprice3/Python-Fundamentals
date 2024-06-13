# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: File Processing Classes
# Change Log: (Who, When, What)
#   JP,11JUN24,Created Script
# ------------------------------------------------------------------------------------------ #

import json
import data_classes
#import presentation_classes

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    JP,11JUN24,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        JP,11JUN24,Created Function

        :param file_name: string data with name of file to read from
        :param employees: list of dictionary rows to be filled with file data
        :param employee_type: an reference to the Employee class

        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name=employee["FirstName"]
                    employee_object.last_name=employee["LastName"]
                    employee_object.review_date=employee["ReviewDate"]
                    employee_object.review_rating=employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        JP,11JUN24,Created Function

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            employee_dictionary: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_ratings_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                employee_dictionary.append(employee_ratings_json)

            with open(file_name, "w") as file:
                json.dump(employee_dictionary, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")

    @staticmethod
    def creation_of_json(fileName: str, employee: list):
        """
            This function creates a dictionary if one does not exist for the Professor utilizing the Python Arts script.

            Notes:
                -None
                :param fileName
                :param employee_data
                ChangeLog: (Who, When, What)
                JP,26MAY24,Created function
        """
        try:
            file = open(FILE_NAME, "w")
            employee_data = json.load(file)
            employee_row1: dict = {"FirstName": "Cho", "LastName": "Chang", "ReviewDate": "1979-04-07", "ReviewRating": "4"}
            employee_data: list = [employee_row1]
            file = open("EmployeeRatings.json", "w")
            json.dump(employee_dictionary, file)
            file.close()
        except FileNotFoundError as e:
            print("JSON file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("Prof. Justin will create a JSON for you..")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("JSON document successfully created")
        
        
print("Successfully imported processing classes")