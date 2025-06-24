# Pseudocode:

# Convert a float number into an integer.
# Convert an integers into a float.
# Convert an integers into a string.
# Convert a string into an integers.
# Print out the converted numbers and confirm their types.

# Python code:

# Declare the variables
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# Convert num1 into an integer
num1 = int(num1)

# Convert num2 into an float
num2 = float(num2)

# Convert num3 into a string
num3 = str(num3)

# Convert string1 into an integer
string1 = int(string1)

# Print the variables and their types after converting
print(f"{num1} is of {type(num1)}")
print(f"{num2} is of {type(num2)}")
print(f"{num3} is of {type(num3)}")
print(f"{string1} is of {type(string1)}")
