# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   JP,13MAT24,Created Script
#   JP,16MAY24,Added Exception
#   JP,22MAY24,Added Classes and Functions
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants and variables
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
#Define the variables
students: list = []  # a table of student data NEEDS TO BE USED
menu_choice: str = '' # Hold the choice made by the user.

# --------SEPARATION OF CONCERNS-------------
#
#   DATA LAYER
#       Class: FileProcessor
#
#   PRESENTATION LAYER
#       Class: IO
#
#   PROCESSING LAYER
#       Create/Read JSON file
#       Execute functions
#       Terminate program
# -------------------------------------------

# ---------DATA LAYER-----------------------
# Define the Data Variables


# Processing --------------------------------------- #

class FileProcessor:
    '''
        A collection of processing layer functions that work with json files

        ChangeLog: (Who, When, What)
        JP,22MAY24,Created Class
    '''
    @staticmethod
    def write_data_to_file(fileName: str, student_data: list):
        """ This function writes data from a list  to a json file

        Notes:
        - Data sent to the student_table parameter will be overwritten.

        ChangeLog: (Who, When, What)
        JP,22MAY24,Created function

        :param fileName: string with the name of the file we are reading
        :param student_table: list of dictionary rows we are adding data to
        :return: list of dictionary rows filled newly added data
        """
        try:
            file = open(fileName, "w")
            json.dump(student_data, file)
        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            file.close()
            print("The following data was saved to file!")
            return student_data


    @staticmethod
    def read_data_from_file(fileName:str, student_data:list):
        """ This function reads data from a json file and then displays the data

        Notes: This data is read from the student_table
        - Data on the file may
        ChangeLog: (Who, When, What)
        JP,22MAY24,Created function

        :param file_name: string with the name of the file we are reading
        :param student_table: list of dictionary rows we are adding data to
        """
        try:
            file = open(fileName, "r")
            student_data = json.load(file)
            for item in students:
                print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, Course: {item['Course']}")
        except FileNotFoundError as e:
            print("JSON file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            json.dump(student_data, file)
            file.close()
        finally:
            IO.output_student_courses(student_data=students)



class IO:
    '''
        A collection of input/output (IO) layer functions that work with json files

        ChangeLog: (Who, When, What)
        JP,22MAY24,Created Class
    '''

    @staticmethod
    def output_error_message(message: str, error: Exception = None):
        """ This function displays and error message when an Exception is reached

        Notes:
        -None
        :param message
        :param error
        ChangeLog: (Who, When, What)
        JP,22MAY24,Created function
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def input_menu_choice():
        """ This function will allow the user to select options 1 - 4 and will raise an exception
        for any other input

        Notes:
        - None
        ChangeLog: (Who, When, What)
        P,22MAY24,Created function
        :return: prompts the user to input accepted an accepted input
        """
        try:

            options = {"1", "2", "3", "4"}
            menu_choice = input("What would you like to do: ")
            if menu_choice not in options:
                raise Exception ("Invalid choice. Please enter a number from 1 through 4.")

        except Exception as e:
                IO.output_error_message(e.__str__())
        finally:
            return menu_choice


    @staticmethod
    def output_menu(menu: str):
        """ This function will display the menu options, the MENU is a global constant

            Notes:
            - None
            ChangeLog: (Who, When, What)
            JP,22MAY24,Created function
            :param menu: str
        """
        global MENU

        print()
        print(MENU)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_student_data(student_data: list):
        """ This function will allow the user to input their first name, last name and course.
            Secondly this adds the newly input data in the student_table. Finally, a message with
            the new data will display to the user what was just added.

            Notes:
            - There are error exceptions if the user inputs numbers when it expects letters
            ChangeLog: (Who, When, What)
            JP,22MAY24,Created function
            :param student_data
        """
        student_first_name: str = ''
        student_last_name: str = ''
        course_name: str = ''

        try:
            # Check that the input does not include numbers
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "Course": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            return student_data

    @staticmethod
    def output_student_courses(student_data:list):
        """ This function will display the current data from student_table which is in JSON format.

            Notes:
            - None
            ChangeLog: (Who, When, What)
            JP,22MAY24,Created function
            :param student_data
        """
        # print("-" * 50)
        # print("\nCurrent registered students:")
        # print(student_data)
        # print("-" * 50)
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["Course"]}')
        print("-" * 50)

#end of class creations

# creates a dictionary if one does not exist for the Professor utilizing the Python Arts script.
'''
This portion is to create a json file, assuming that there has not been a file that
has not been created or a defined pathway. >>>>
'''

try:
     file = open(FILE_NAME, "r")
     student_table = json.load(file)
     for item in students:
         print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, Course: {item['Course']}")
except FileNotFoundError as e:
    print("JSON file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    print("Prof. Justin will create a JSON for you..")
    student_row1: dict = {"FirstName": "First Name", "LastName": "Last Name", "Course": "Course"}
    student_table: list = [student_row1]
    file = open("Enrollments.json", "w")
    json.dump(student_table, file)
    file.close()
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    print("JSON document successfully created")

'''
<<<< This portion is to create a json file, assuming that there has not been a file that
has not been created or a defined pathway.
'''
# Begining the main body of the script

while True:
    IO.output_menu(menu=MENU)

    # Present the menu of choices
    menu_choice=IO.input_menu_choice()
    # Present the menu of choices

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        # Process the data to create and display a custom message

    # Save the data to a file
    elif menu_choice == "3":
            FileProcessor.write_data_to_file(fileName=FILE_NAME, student_data=students)
            IO.output_student_courses(student_data=students)



    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
