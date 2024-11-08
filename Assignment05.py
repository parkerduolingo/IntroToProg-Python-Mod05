# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Parker Henry, 11/7/24, Created Initial Program)
#   RRoot,1/1/2030,Created Script
#   Parker Henry, 11/7/24, Created Initial Program
# ------------------------------------------------------------------------------------------ #

#Make sure my program can support JSON files
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = '' # Holds the data to be put into enrollments.json
student_data: dict = {}  # one row of student data in the form of a dictionary
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file_obj = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

# When the program starts, read the file data into a list of dictionaries and extract the data from the file
try:
    file_obj = open(FILE_NAME, "r")
    json_data = json.load(file_obj)
    for row in json_data:
        # Transform the data from the file
        student_data = {"FirstName":row["FirstName"],"LastName":row["LastName"],"CourseName":row["CourseName"]}
        # Load it into our collection (list of dictionaries)
        students.append(student_data)
except FileNotFoundError as e:
    print(f"Uh oh! This file doesn't seem to exist. Let's create a file called {FILE_NAME}.")
    file_obj=open(FILE_NAME, "w")
except Exception as e:
    print("Oh no! There was an error.\nHere's the error code:")
    print(e, e.__doc__)
finally:
    file_obj.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('Inputs can only contain alphabetical characters.')
            student_last_name = input("Enter the student's last name: ")
            if not student_first_name.isalpha():
                raise ValueError('Inputs can only contain alphabetical characters.')
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name}
            students.append(student_data)
            print(f"\nYou have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print("User entered invalid information. Continuing...")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("\nThis is the current data:\n")
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file_obj = open(FILE_NAME, "w")
            json.dump(students,file_obj)
            print(f"\nThe following data was saved to {FILE_NAME}!\n")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        except Exception as e:
            print("Oh no! There was an error.\nHere's the error code:")
            print(e, e.__doc__)
        finally:
            print("\nClosing file")
            file_obj.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
