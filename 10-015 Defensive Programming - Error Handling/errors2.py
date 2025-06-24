"""
This example program demonstrates various types of errors and their corrections.

Errors and their types:
1. Syntax Error: Missing quotes around the string 'Lion', causing a syntax error.
2. Logical Error: Incorrect format string. Should correctly map variables to placeholders.
   `{animal}` to `{animal}`, `{animal_type}` to `{animal_type}`, and `{number_of_teeth}` to `{number_of_teeth}`.
   Used f-strings to easily format the strings.
3. Syntax Error: Missing parentheses around `print` statement, causing a syntax error.

"""

# Fixed: Added quotes to make it a string.
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# Fixed: Corrected formatting placeholders.
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."
print(full_spec)