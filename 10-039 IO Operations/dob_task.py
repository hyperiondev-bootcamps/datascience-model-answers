"""
Reads names and dates of birth from 'DOB.txt' and prints them separately.

Opens 'DOB.txt' in read mode with UTF-8 encoding, extracts names and dates of
birth from each line, and prints them in two sections: 'Name' and 'Birthdate'.
Each line in the file is expected to contain a name followed by a date of birth
separated by spaces.

Example file content (DOB.txt):
John Doe 2000-01-01
Jane Smith 1995-12-31

Output:
Name

John Doe
Jane Smith

Birthdate

2000-01-01
1995-12-31
"""

# Open the file 'DOB.txt' in read mode with UTF-8 encoding
with open('DOB.txt', 'r', encoding='utf-8') as file:
    # Initialize empty lists to store names and dates of birth
    names = []
    dates_of_births = []

    # Iterate through each line in the file
    for line in file:
        # Split the line into a list of words
        splitted_lines = line.split()

        # Append the first two words (representing the name)
        names.append(splitted_lines[:2])

        # Append the remaining words (representing the date of birth)
        dates_of_births.append(splitted_lines[2:])

# Print section header for names
print("Name\n")

# Iterate through each name in the 'names' list
for name in names:
    # Join the words in the name list with a space and print
    print(" ".join(name))

# Print section header for dates of birth
print("\nBirthdate\n")

# Iterate through each date of birth in the 'dates_of_births' list
for date_of_birth in dates_of_births:
    # Join the words in the date of birth list with a space and print
    print(" ".join(date_of_birth))
