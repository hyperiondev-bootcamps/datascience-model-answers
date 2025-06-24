"""
Module to generate a registration form for students.

Prompts the user to enter the number of students registering,
then prompts for each student's ID number and writes it to the
file 'reg_form.txt' with placeholder dots.

"""

# Prompt the user to enter the number of students registering
num_of_students = int(input("How many students are registering: "))

# Open the file 'reg_form.txt' in write mode with UTF-8 encoding
with open("reg_form.txt", "w", encoding="utf-8") as file:
    # Iterate through each student using a range loop
    for index in range(num_of_students):
        # Prompt the user to enter the student ID number
        student_id = int(input("Enter student ID number: "))

        # Write the student ID number to the file with dots to sign.
        file.write(f"{student_id} ................\n")
