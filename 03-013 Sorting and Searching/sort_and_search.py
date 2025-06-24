"""Model answer"""


def linear_search(numbers, target):
    """
    Perform linear search to find the target number in the list.

    Args:
        numbers (list of int): The list of integers to search.
        target (int): The number to find in the list.

    Returns:
        int: The index of the target number if found, otherwise -1.
    """
    for index, number in enumerate(numbers):
        if number == target:
            # Return the index if the target is found
            return index
    # Return -1 if the target is not found
    return -1


def insertion_sort(numbers):
    """
    Sort the list of integers in ascending order using insertion sort.

    Args:
        numbers (list of int): The list of integers to sort.

    Returns:
        None: Modifies the list in place.
    """
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


def binary_search(sorted_numbers, target):
    """
    Perform binary search to find the target number in a sorted list.

    Args:
        sorted_numbers (list of int): The sorted list of integers to search.
        target (int): The number to find in the list.

    Returns:
        int: The index of the target number if found, otherwise -1.
    """
    left = 0
    right = len(sorted_numbers) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_numbers[mid] == target:
            return mid
        elif sorted_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
TARGET_NUMBER = 9

# Comment regarding reason for selected algorithm on list.
"""
On the given list, the linear search algorithm is the best option to find
the target number because the list is unsorted.
The binary search algorithm would have been the better option
if the given list was sorted.
"""

# Linear search section
print("Unsorted numbers:", numbers)
linear_index = linear_search(numbers, TARGET_NUMBER)

if linear_index != -1:
    print(
        f"The number {TARGET_NUMBER} was found at index "
        f"{linear_index} using linear search."
    )
else:
    print(f"The number {TARGET_NUMBER} was not found using linear search.")

# Sort the numbers using insertion sort
insertion_sort(numbers)
print("\nSorted numbers:", numbers)

# Binary search section
binary_index = binary_search(numbers, TARGET_NUMBER)

if binary_index != -1:
    print(
        f"The number {TARGET_NUMBER} was found at index "
        f"{binary_index} using binary search."
    )
else:
    print(f"The number {TARGET_NUMBER} was not found using binary search.")

# Additional comment explaining the use of binary search
"""
The binary search algorithm is best utilized in scenarios
where data is already sorted.
For example, searching for a word in a dictionary
allows starting from the middle and deciding to look
forward or backward based on the word being searched for.
"""
