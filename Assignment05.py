# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Blaise Konzel>,<05/18>, <Updating functionality and adding json capability>
# ---------------------------------------------------------------------------------------- #

import json

#created a function to handle errors on names containing numbers
def isletters(x):
    while x.isalpha() == False:
        x = input('The requested string cannot contain numbers, please input only characters: ')
    return(x) 

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
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str, str] = []  # one row of student data 
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try: 
    file = open(FILE_NAME)
    students = json.load(file)
#error handling for empty json file
except json.JSONDecodeError:
    print('\n!!!!!!JSONDecodeError!!!!!! Please make sure file is populated with data.')
#error handling for file abscent from folder
except FileNotFoundError:
    print('\n!!!!FileNotFoundError!!!!!! Please make sure file is in correct working directory.')
# error for everything else
except Exception as e: 
    print(f'Unexpected error occured... {e}' )

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        
        student_first_name = isletters(input("Please enter the student's first name: "))
        student_last_name = isletters(input("Please enter the student's last name: "))
        course_name = input("Please enter the name of the course: ")
        # format data as dictionary
        student_data: dict[str, str] = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName":  course_name}
        #append dictionary to list of dictionaries
        students.append(student_data)
        print(f"\nYou have registered {student_data['FirstName']} {student_data['LastName']} for {student_data['CourseName']}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}.")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        #open json with 'as' clause... automatically closes when finished
        try: 
            file = open(FILE_NAME, 'w')
        except Exception as e:
            print('An error occured saving data to the file.')
            print(e, e.__doc__)
        try: 
            json.dump(students, file, indent=2)
            print(f"The following data was saved to {FILE_NAME}!\n")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}.")
            continue
        except Exception as e:
            print('An error occured saving data to the file.')
            print(e, e.__doc__)   
        finally:
                file.close()
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")

#%%

            
    
