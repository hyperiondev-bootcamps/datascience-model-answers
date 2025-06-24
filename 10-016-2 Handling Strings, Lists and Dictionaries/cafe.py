"""
This program calculates the total value of the stock in a cafe.
It uses lists of menu items, a dictionary of stock quantities,
and a dictionary of item prices to compute the total stock value.
It also handles mismatches between stock and price dictionaries
by ensuring that each item is properly accounted for before calculation.
"""

# List of items on the menu
menu = [
    "espresso",
    "macchiato",
    "cappuccino",
    "croissant",
    "pastries",
    "sandwich",
    "cookie",
    "muffin",
    "brownie",
]

# Dictionary with the item and its quantity in stock
stock = {
    "espresso": 400,
    "macchiato": 200,
    "cappuccino": 200,
    "croissant": 100,
    "pastries": 100,
    "sandwich": 100,
    "cookie": 100,
    "muffin": 100,
    "brownie": 100,
}

# Dictionary with the item and its unitary price
price = {
    "espresso": 1.00,
    "macchiato": 1.50,
    "cappuccino": 2.00,
    "croissant": 1.00,
    "pastries": 1.50,
    "sandwich": 2.00,
    "cookie": 1.00,
    "muffin": 1.50,
    "brownie": 2.00,
}

# Initialize total_stock to 0
total_stock = 0

# Calculate the total value of the stock for items in the menu
for item in menu:
    # Calculate the value per item by multiplying quantity by price
    value_per_item = stock[item] * price[item]
    # Add the value to total_stock
    total_stock += value_per_item

# Print the total stock value for menu items
print(f"The total value of the stock is £ {total_stock:.2f}.")

# This approach handles mismatches between stock and price dictionaries.
print("\nHandling mismatches between stock and price dictionaries")

# Updated list to demonstrate how to handle cases if a menu item does not
# have a price or stock amount.
mismatch_menu = [
    "espresso",
    "macchiato",
    "cappuccino",
    "croissant",
    "pastries",
    "sandwich",
    "cookie",
    "muffin",
    "brownie",
    "cake",  # 'cake' is only defined within the 'mismatch_menu' list.
]

# Initialize total_stock to 0
total_stock = 0

# Calculate the total value of the stock, handling mismatches
for item in mismatch_menu:
    if item in price and item in stock:
        # Calculate the value per item by multiplying quantity by price
        value_per_item = stock[item] * price[item]
        # Add the value to total_stock
        total_stock += value_per_item
    else:
        print(f"Price and stock for '{item}' is not defined.")

# Print the total stock value for mismatch menu items
print(f"The total value of the stock is £ {total_stock:.2f}.")
