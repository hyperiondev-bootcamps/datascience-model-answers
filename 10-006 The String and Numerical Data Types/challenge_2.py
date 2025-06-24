# Take the name of the user's favorite restaurant
string_fav = input("Enter the name of your favorite restaurant: ")

# Take the user's favorite number
int_fav = int(input("Enter your favorite number: "))

# Print out the user's favorite restaurant and number
print("Your favorite restaurant is:", string_fav)
print("Your favorite number is:", int_fav)

# Try to cast string_fav to an integer

int(string_fav)

'''When you try to cast string_fav to an integer using int(),
if string_fav contains characters that cannot be converted
to an integer, a ValueError will be raised.
This is because integers can only represent numerical values,
and if the string contains alphabetic characters,
it cannot be converted to an integer'''