# The number of rows for the pattern.
rows = 10

# Check if 'rows' is an even, positive integer greater than zero.
if (rows // 2) * 2 == rows and rows > 0:
    # Initialise Variables
    count = 0
    asterisk = "*"
    half = rows//2

    for index in range(1, rows):
        # Increment the half of the pattern
        if index <= half:
            count += 1

        # Decrement the half of the pattern
        else:
            count -= 1

        # Print asterisks
        print(asterisk * count)

else:
    # If an invalid number has been entered print an error message.
    print("Invalid input.Please enter an even positive integer for 'rows.")