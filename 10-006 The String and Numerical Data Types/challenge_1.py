import math

# Ask the user to enter the lengths of all three sides of a triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Calculate the semi-perimeter (s)
s = (side1 + side2 + side3) / 2

# Calculate the area of the triangle using Heron's formula
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Print out the area
print(f"The area of the triangle is: {area}")
