print("Practical Task 1: Part 1: alternating letters to upper and lowercase")

original_string = input("Enter a sentence: ")

# This program alternates each character into upper and lowercase in a sentence.

# Create an empty string
modified_string = ""

# Iterate over the indexes
for num in range(len(original_string)):
    # Convert letter to lowercase if index is even
    if num % 2 == 0:
        modified_string += original_string[num].upper()
    # Convert letter to uppercase if index is odd
    else:
        modified_string += original_string[num].lower()
# Print the modified string
print(modified_string)


print("Practical Task 1: Part 2: alternating words to upper and lowercase")

original_string = input("Enter a sentence: ")


# This program alternates each word into lower and uppercase in a sentence.

# Split the original string into words
words_list = original_string.split()

# Create an empty list
new_words_list = []

# Use for loops with enumerate to easily get the index and word from words_list
for index, word in enumerate(words_list):
    if index % 2 == 0:
        # Convert word to lowercase if index is even
        word = word.lower()
        # Add it to your new_word_list
        new_words_list.append(word)
    else:
        # Convert word to uppercase if index is odd
        word = word.upper()
        # Add it to your new_word_list
        new_words_list.append(word)

# Turn the new_words_list into a string
modified_string2 = " ".join(new_words_list)

# Print the modified string
print(modified_string2)
