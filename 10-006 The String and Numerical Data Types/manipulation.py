# Ask the user to enter a sentence
str_manip = input("Please enter a sentence: ")

# Calculate and display the length of str_manip
length_of_str = len(str_manip)
print(f"The length of your sentence is: {length_of_str}")

# Find the last letter in str_manip and replace every occurrence
# of this letter with '@'
last_letter = str_manip[-1]
str_replaced = str_manip.replace(last_letter, "@")
print(f"Sentence after replacing '{last_letter}' with '@': {str_replaced}")

# Print the last 3 characters in str_manip backwards
last_three_reversed = str_manip[-3:][::-1]
print(f"The last three characters in reverse are: {last_three_reversed}")

# Create a five-letter word using the first three and the last two
# characters of str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]
print(f"The new five-letter word is: {five_letter_word}")
