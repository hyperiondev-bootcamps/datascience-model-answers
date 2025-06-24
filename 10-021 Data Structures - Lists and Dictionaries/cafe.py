# This program calculates the total value of the stock of my Cafe

# List of items on the menu
menu = ['espresso',
        'macchiato',
        'cappuccino',
        'croissant',
        'pastries',
        'sandwich',
        'cookie',
        'muffin',
        'brownie']

# Dictionary with the item and its quantity on stock
stock = {'espresso': 400,
         'macchiato': 200,
         'cappuccino': 200,
         'croissant': 100,
         'pastries': 100,
         'sandwich': 100,
         'cookie': 100,
         'muffin': 100,
         'brownie': 100, }

# Dictionary with the item and its unitary price
price = {'espresso': 1.00,
         'macchiato': 1.50,
         'cappuccino': 2.00,
         'croissant': 1.00,
         'pastries': 1.50,
         'sandwich': 2.00,
         'cookie': 1.00,
         'muffin': 1.50,
         'brownie': 2.00}

# Setting total_stock = 0
total_stock = 0

# Iterate over my stock dictionary
for item, value in stock.items():
    # Getting the value per item
    value_per_item = (stock[item] * price[item])
    # Add this value to my variable total_stock
    total_stock += value_per_item

# Print the total stock
print(f"The total value of the stock is £ {total_stock:.2f}.")


print("Handling mismatches between stock and price dictionaries")

# Dictionary with the item and its quantity on stock
stock = {'espresso': 400,
         'macchiato': 200,
         'cappuccino': 200,
         'croissant': 100,
         'pastries': 100,
         'sandwich': 100,
         'cookie': 100,
         'muffin': 100,
         'brownie': 100,
         'cake': 100}  # add 'cake' only to stock


# Setting total_stock = 0
total_stock = 0

# Iterate over my stock dictionary
for item, value in stock.items():
    # if-else to handle mismatches between price and stock
    if item in price:
        # Getting the value per item
        value_per_item = (stock[item] * price[item])
        # Add this value to my variable total_stock
        total_stock += value_per_item
    else:
        print(f"Price for {item} is not defined.")

# Print the total stock
print(f"The total value of the stock is £ {total_stock:.2f}.")
