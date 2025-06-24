"""Practical Task 2 model answers"""

# Informative message to the user
print("Please enter 3 different integers. ")

# Get numbers used for the calculations
first_number = int(input("Your first integer: "))
second_number = int(input("Your second integer: "))
third_number = int(input("Your third integer: "))

# Declare variable since it is reused in the calculations twice - Efficient approach
total_sum = first_number + second_number + third_number

# Perform calculations and display the results
print(f"The sum of all 3 numbers is: {total_sum}")
print(f"The first number minus the second number is: {first_number - second_number}")
print(f"The third number multiplied by the first number is: {third_number * first_number}")
print(f"The sum of all three numbers divided by the third number is: {total_sum / third_number}")
