"""Practical Task 1 model answers"""

# Get sentence to manipulate
str_manip = input("Enter a sentence:\n")

# Display the length of the sentence and print it
print(len(str_manip))

# Find the last character in the sentence
last_letter = str_manip[-1]

# Replace every occurrence of the last letter in str_manip with "@"
print(str_manip.replace(last_letter, "@"))

# Print the last 3 characters backwards
print(str_manip[-1:-4:-1])

# A 5-letter word made up of the first 3 letters and the last 2 letters
print(str_manip[:3] + str_manip[-2:])
