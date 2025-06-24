def mine_sweeper(grid):
    # Check if the grid is empty or has irregular dimensions
    if not grid or not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Invalid grid: Empty or irregular dimensions")

    # Loop through each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            mines = 0
            if grid[row][col] == "-":
                # Check neighbouring cells for mines

                # Check east
                if col + 1 < len(grid[row]):
                    if grid[row][col + 1] == "#":
                        mines += 1
                # Check west
                if col - 1 >= 0:
                    if grid[row][col - 1] == "#":
                        mines += 1
                # Check north
                if row - 1 >= 0:
                    if grid[row - 1][col] == "#":
                        mines += 1
                # Check northeast
                if row - 1 >= 0 and col + 1 < len(grid[row]):
                    if grid[row - 1][col + 1] == "#":
                        mines += 1
                # Check northwest
                if row - 1 >= 0 and col - 1 >= 0:
                    if grid[row - 1][col - 1] == "#":
                        mines += 1
                # Check south
                if row + 1 < len(grid):
                    if grid[row + 1][col] == "#":
                        mines += 1
                # Check southeast
                if row + 1 < len(grid) and col + 1 < len(grid[row]):
                    if grid[row + 1][col + 1] == "#":
                        mines += 1
                # Check southwest
                if row + 1 < len(grid) and col - 1 >= 0:
                    if grid[row + 1][col - 1] == "#":
                        mines += 1
                # Update the cell value with the number of neighboring mines
                grid[row][col] = mines
    # Return the modified grid
    return grid


# Define a function to print the grid in a formatted manner
def print_grid(input_grid):
    # Check if the input grid is valid
    if not input_grid:
        print("Invalid grid: Empty")
        return
    # Print the grid
    print("[", end="")
    for i in range(len(input_grid)):
        print("", input_grid[i], end="")
        # Add a comma after each sublist except for the last one
        if i != len(input_grid) - 1:
            print(",")
        else:
            print(end="")
    print(" ]")


# Define a grid for testing
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
]

try:
    # Print the output of mine_sweeper function
    print("\nExpected Output : \n")
    print(mine_sweeper(grid))

    # Example usage of print_grid function
    print("\nExpected Output in a Grid Format : \n")
    print_grid(mine_sweeper(grid))
except ValueError as ve:
    print(f"Error Found while running your program: {ve}")
