"""Model answer"""


def merge_sort_by_length(strings):
    """
    Sort a list of strings by their length using the merge sort algorithm.

    Args:
        strings (list): A list of strings to be sorted.

    Returns:
        list: The list of strings sorted by length in descending order.
    """

    # Get the length of the input list
    strings_length = len(strings)

    # Create temporary storage for merging
    temporary_storage = [None] * strings_length

    # Initialise the size of subsections to 1
    size_of_subsections = 1

    # Iterate until the size of subsections is less than the length of the list
    while size_of_subsections < strings_length:
        # Iterate over the list in steps of size_of_subsections * 2
        for i in range(0, strings_length, size_of_subsections * 2):
            # Determine the start and end indices of the two subsections
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, strings_length
            )
            second_section_start, second_section_end = first_section_end, min(
                first_section_end + size_of_subsections, strings_length
            )

            # Define the sections to merge
            sections = (first_section_start, first_section_end), (
                second_section_start,
                second_section_end,
            )

            # Call the merge function to merge the subsections
            merge_by_length(strings, sections, temporary_storage)

        # Double the size of subsections for the next iteration
        size_of_subsections *= 2

    # Return the sorted list
    return strings


def merge_by_length(strings, sections, temporary_storage):
    """
    Merges two sections of a list based on the length of the strings.

    Args:
        strings (list): The list of strings to be merged.
        sections (tuple): A tuple containing the start and end
            indices of the two stings.
        temporary_storage (list): Temporary storage for the merged strings.
    """

    # Unpack the sections tuple to get the start and end indices
    # of each section.
    (first_section_start, first_section_end), (
        second_section_start,
        second_section_end,
    ) = sections

    # Initialise indices for the two sections and temporary storage
    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    # Loop until both sections have been fully merged
    while left_index < first_section_end or right_index < second_section_end:
        # Check if both sections still have elements to compare
        if left_index < first_section_end and right_index < second_section_end:
            # Compare string lengths and place the longer one
            # into temporary storage
            if len(strings[left_index]) > len(strings[right_index]):
                temporary_storage[temp_index] = strings[left_index]
                left_index += 1
            else:
                temporary_storage[temp_index] = strings[right_index]
                right_index += 1
            temp_index += 1

        # If section 1 still has elements left to merge
        elif left_index < first_section_end:
            for i in range(left_index, first_section_end):
                temporary_storage[temp_index] = strings[left_index]
                left_index += 1
                temp_index += 1

        # If section 2 still has elements left to merge
        else:
            for i in range(right_index, second_section_end):
                temporary_storage[temp_index] = strings[right_index]
                right_index += 1
                temp_index += 1

    # Copy sorted elements from temporary storage back to the original list
    for i in range(temp_index):
        strings[first_section_start + i] = temporary_storage[i]


# Example usage and results
list_1 = [
    "banana",
    "apple",
    "cherry",
    "blueberry",
    "pineapple",
    "orange",
    "kiwi",
    "mango",
    "grape",
    "watermelon",
]

list_2 = [
    "notebook",
    "pencil",
    "paper",
    "eraser",
    "sharpener",
    "calculator",
    "folder",
    "backpack",
    "highlighter",
    "stapler",
]

list_3 = [
    "Python",
    "Java",
    "JavaScript",
    "C++",
    "Ruby",
    "Swift",
    "Go",
    "Rust",
    "Kotlin",
    "TypeScript",
]

sorted_list_1 = merge_sort_by_length(list_1)
sorted_list_2 = merge_sort_by_length(list_2)
sorted_list_3 = merge_sort_by_length(list_3)

print(sorted_list_1)
print(sorted_list_2)
print(sorted_list_3)
