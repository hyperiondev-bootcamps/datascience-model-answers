
def perform_calculation():
    """
    Prompts the user for numbers, operator, performs the calculation, and handles errors.
    """
    while True:  # Loop until valid input is received
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            if operator not in ['+', '-', '*', '/']:
                raise ValueError("Invalid operator!")

            # Make computations based on the operator.
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero!")
                result = num1 / num2

            # Record the calculation in equations.txt
            with open('equations.txt', 'a+', encoding='utf-8') as file:
                file.write(f"{num1} {operator} {num2} = {round(result, 2)}\n")
                print("\nYour results have been successfully stored in equations.txt")
            break  # Exit the loop after successful operation

        # Handle Exceptions.
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")


def print_previous_equations():
    """
    Reads and displays previous equations from equations.txt. Handles file errors.
    """
    try:
        with open('equations.txt', 'r', encoding='utf-8') as file:
            equations = file.readlines()
        # Print equations if there is something in the file. 
        if equations:
            print("\nPrevious equations:")
            for equation in equations:
                print(equation.strip())
        else:
            print("\nNo previous equations found.")
    except FileNotFoundError:
        print("No previous equations found.")


def calc_app():
    """
    Presents the calculator menu, handles user choices, and exits when necessary.
    """
    while True:
        print("\nWelcome to the Calculator App!")
        print("1. Perform Calculation")
        print("2. Print Previous Equations")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        # Call functions based on user choice.
        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_previous_equations()
        elif choice == '3':
            break  # Exit the loop, ending the program
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# Start the app
calc_app()
