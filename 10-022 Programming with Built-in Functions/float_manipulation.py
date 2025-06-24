''' Import the statistics module to perform statistical calculations'''
import statistics

# Initialize an empty list to store the numbers entered by the user
numbers = []
 
# Prompt the user to enter 10 floating point numbers
for num in range(10):
    number = float(input("Enter a floating point number : "))
    numbers.append(number)  # Add the entered number to the list

# Print the sum of all the numbers entered by the user
print(f"The total of all the numbers is {sum(numbers)}")

# Print the index of the maximum number in the list
print(f"The index of the maximum number is {numbers.index(max(numbers))}")

# Print the index of the minimum number in the list
print(f"The index of the minimum number is {numbers.index(min(numbers))}")

# Print the average of all the numbers using the mean function from the statistics module
print(f"The average of the numbers is {round(statistics.mean(numbers), 2)}")

# Print the median of all the numbers using the median function from the statistics module
print(f"The median of the numbers is {round(statistics.median(numbers), 2)}")
