# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: This assignment is the Employee Rating
# Change Log: (Who, When, What)
#   JP,11JUN24,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
FILE_NAME: str = "EmployeeRatings.json"
# Define the Data Constants and variables
MENU: str = '''
------------ Employee Ratings -----------
  Select from the following menu:  
    1. Enter new employee rating data.
    2. Show current employee rating data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
#Define the variables
employees: list = []  # a table of se
menu_choice: str = '' # Hold the choice made by the user.

# --------SEPARATION OF CONCERNS-------------
#   OBJECT LAYER
#       Class: Person
#       Class: Employee
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

# ---------Object LAYER-----------------------
# Define the Data Variables


# Processing --------------------------------------- #
