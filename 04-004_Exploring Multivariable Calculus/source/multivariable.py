
"""Calculate the gradient of a two-variable mathematical function."""

import sympy as sp


# Define the symbolic variables used in the function.
x, y = sp.symbols("x y")


def calculate_gradient(expression):
    """Calculate and display the gradient of a multivariable function.

    Args:
        expression (str): A mathematical expression containing
            the variables x and y.

    Returns:
        None: The calculated gradient vector is printed.
    """
    # Convert the user's input into a SymPy expression.
    f = sp.sympify(expression)

    # Calculate the partial derivative with respect to x.
    # The variable y is treated as a constant.
    df_dx = sp.diff(f, x)

    # Calculate the partial derivative with respect to y.
    # The variable x is treated as a constant.
    df_dy = sp.diff(f, y)

    # Combine the partial derivatives into a gradient vector.
    gradient = (df_dx, df_dy)

    # Display the original function and its gradient vector.
    print(
        f"The gradient vector of the function f = {f} "
        f"is ∇f = {gradient}."
    )


# Request a mathematical expression from the user.
user_input = input("Enter a two-term multivariable function: ")

# Pass the user's expression to the gradient function.
calculate_gradient(user_input)
