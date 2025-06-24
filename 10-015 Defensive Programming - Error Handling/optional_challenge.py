"""
This example program demonstrates various types of errors and their corrections.

Errors and their types:
1. Syntax Error: Missing parentheses in print statements
2. Runtime Error: Division by zero
3. Logical Error: Incorrect classification logic for age
"""

# Syntax Error: Missing parentheses in print
# This will raise a syntax error because print statements in Python 3 
# require parentheses.
print("This is a syntax error")

# Runtime Error: Division by zero
# This will raise a runtime error because dividing by zero is 
# mathematically undefined.
value = 10 / 0

# Logical Error: This logic incorrectly classifies 18-year-olds as adults.
# It should be "age <= 18" if we want to classify 18-year-olds as minors.
age = 18
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
