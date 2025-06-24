"""
The goal of the program is to recursively compute the sum of values in a list
    from the start up to the given index.
"""


def adding_up_to(list_of_integers, index):
    """
    Recursively sum up the values in the list up to and including the
        specified index.

    Args:
        list_of_integers (list of int): A list of integers.
        index (int): The index up to which values should be summed.

    Returns:
        int: The sum of values from the start of the list up to the
            specified index.

    """
    # Base case: check if index is 0 or negative
    if index <= 0:
        return list_of_integers[0]

    # Recursive step: add the current value to the sum of values
    # up to the previous index
    return list_of_integers[index] + adding_up_to(list_of_integers, index - 1)


# Example usage:
# adding_up_to([1, 4, 5, 3, 12, 16], 4) should return 1 + 4 + 5 + 3 + 12 = 25
result = adding_up_to([1, 4, 5, 3, 12, 16], 4)
print(result)  # Output: 25

# adding_up_to([4, 3, 1, 5], 1) should return 4 + 3 = 7
result = adding_up_to([4, 3, 1, 5], 1)
print(result)  # Output: 7
