"""
The goal of the program is to recursively find and return the largest number
    from a given list of integers.
"""


def largest_number(numbers):
    """
    Find the largest number in the list using recursion.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        int: The largest number found in the list.

    """
    # Base case: if the list has only one element, return that element
    if len(numbers) == 1:
        return numbers[0]
    else:
        # Recursive step: find the largest element in the rest of the list
        max_in_remaining = largest_number(numbers[1:])

        # Compare the first element with the largest element in the
        # rest of the list
        if numbers[0] > max_in_remaining:
            return numbers[0]
        else:
            return max_in_remaining


# Example usage:
# largest_number([1, 4, 5, 3]) should return 5
print(largest_number([1, 4, 5, 3]))  # Output: 5

# largest_number([3, 1, 6, 8, 2, 4, 5]) should return 8
print(largest_number([3, 1, 6, 8, 2, 4, 5]))  # Output: 8
