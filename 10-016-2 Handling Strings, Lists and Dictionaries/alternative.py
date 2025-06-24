"""
This script contains two practical tasks that manipulate strings by
alternating the case of letters and words.

Part 1: Alternates the case of each letter in the given string,
starting with uppercase for the first letter.

Part 2: Alternates the case of each word in the given string,
starting with lowercase for the first word.
"""

print("Practical Task 1: Part 1: alternating letters to upper and lowercase")

original_string = input("Enter a sentence: ")

# Create an empty string to hold the modified string.
modified_string = ""

# Iterate over the indexes of the original string.
for i in range(len(original_string)):
    # Convert letter to uppercase if index is even.
    if i % 2 == 0:
        modified_string += original_string[i].upper()
    # Convert letter to lowercase if index is odd.
    else:
        modified_string += original_string[i].lower()

# Print the modified string with alternating letter cases.
print(modified_string)


print("\nPractical Task 1: Part 2: alternating words to upper and lowercase")

# This program alternates the case of each word in a sentence.

# Split the original string into a list of words.
words_list = original_string.split()

# Create an empty list to hold the modified words.
new_words_list = []

# Use a for loop with enumerate to easily get the index and word.
for index, word in enumerate(words_list):
    if index % 2 == 0:
        # Convert word to lowercase if index is even.
        word = word.lower()
    else:
        # Convert word to uppercase if index is odd.
        word = word.upper()

    # Add the modified word to the new_words_list.
    new_words_list.append(word)

# Join the list of modified words into a single string.
modified_string2 = " ".join(new_words_list)

# Print the modified string with alternating word cases.
print(modified_string2)