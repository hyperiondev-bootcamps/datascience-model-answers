"""
This example program is meant to demonstrate errors.
"""

# Syntax Error: This error was returned because the string statement 
# was not enclosed in parentheses.
print("Welcome to the error program")

# Syntax Error: There was an unexpected or unnecessary indentation, and
# the newline character was not enclosed in parentheses.
print("\n")

# Syntax Error: Due to unexpected indentation.
# Runtime Error: Due to using the '==' instead of '='
# Fixed by unindenting and using the assignment operator
# instead of the equality operator.
age_Str = "24 years old"

# Runtime Error: ValueError returned as "years old"
# cannot be converted to an integer.
# Fixed: Extracted the numerical part of the string and converted to int.
age = int(age_Str[:-9])

# Syntax Error: Due to unexpected indentation.
# Runtime Error: can only concatenate strings to strings, 
# not integers to strings.
# Fixed: Concatenated strings correctly, and converted age to string.
print("I'm " + str(age) + " years old.")

years_from_now = 3  # Fixed: Removed quotes to assign an integer value.

# Runtime Error: can only concatenate strings to strings,
# not integers to strings.
# Fixed: Concatenated strings correctly, and converted total_years to string.
total_years = age + years_from_now
print("The total number of years: " + str(total_years))

# Syntax Error: total_years was incorrectly defined.
# Fixed: Corrected variable name from 'total' to 'total_years'.

# Syntax Error: the string statement must be enclosed in parentheses.
# Runtime Error: TypeError (cannot concatenate strings and integers).
# Logical Error: 6 months was not added to the total months.
# Fixed: Concatenated strings correctly, and converted total_months to string
# and also added 6 months.
total_months = total_years * 12
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")
