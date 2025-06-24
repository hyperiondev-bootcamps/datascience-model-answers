# Prompt the user to enter their name and convert it to lowercase
name = input("Enter your name: ").lower()

# Initialize an empty list to store incorrect names
incorrect_names = []

# Continue the loop until the user enters the correct name 'john'
while name != 'john':
    # Add the incorrect name to the list
    incorrect_names.append(name)
    # Prompt the user to enter their name again and convert it to lowercase
    name = input("Enter your name: ").lower()

# Print the list of incorrect names
print(f'Incorrect names: {incorrect_names}')
