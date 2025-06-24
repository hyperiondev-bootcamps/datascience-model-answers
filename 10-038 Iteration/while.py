# Initialise variables to store the sum and count of numbers entered
total = 0
count = 0

# Continuously ask the user to enter a number
while True:
    # Get user input
    num = input("Enter a number (enter -1 to stop): ")

    # Check if the input is '-1', if so, break out of the loop
    if num == '-1':
        break

    # Check if the input consists of digits (positive or negative integer)
    if not num.lstrip('-').isdigit():
        print("Invalid input! Please enter a real number.")
        continue

    # Convert the input to a float
    num = float(num)

    # Increment the count and add the number to the total
    count += 1
    total += num

# Check if any numbers were entered (excluding -1)
if count > 0:
    # Calculate the average
    average = total / count
    print(f"The average of the numbers entered is: {average}")
else:
    print("No numbers entered.")
