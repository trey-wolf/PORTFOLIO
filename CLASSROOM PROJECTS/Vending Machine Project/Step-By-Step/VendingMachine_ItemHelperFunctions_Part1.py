# --- Item Helper Functions ---
# These functions will act as the "methods" for our item lists.
# They will operate on a single item list, e.g., ["Chips", 2.00, 10]

def get_name(item):
    """Returns the name of the item."""
    # The name is the first element (index 0)
    pass


def get_price(item):
    """Returns the price of the item."""
    # The price is the second element (index 1)
    pass


def get_stock(item):
    """Returns the stock of the item."""
    # The stock is the third element (index 2)
    pass


def is_available(item):
    """Returns True/False if the stock of item is positive ( > 0)."""
    # Use your get_stock() helper function
    # Check if the stock is greater than 0
    pass


def restock(item, amount):
    """
    - If the amount is positive ( > 0) add that amount to the stock of item.
    - Return True if you restocked an item, False otherwise.
    """
    # Check if amount is positive
    # If so, add the amount to the stock (index 2)
    #   and return True
    # Otherwise, return False
    pass


def purchase(item):
    """
    - If the stock is available, reduce the stock by 1.
    - Return True if you purchased an item, False otherwise.
    """
    # Use your is_available() helper function to check
    # If it is available:
    #   Subtract 1 from the stock (index 2)
    #   Return True
    # Otherwise, return False
    pass


def item_tostring(item, index):
    """
    Returns an f-string that outputs the state of any item object in the following way:
    {index}: {item_name}, ${item_price}, (Current stock: {item_stock})
    """
    # Use your get_name, get_price, and get_stock helpers
    # Format the price to 2 decimal places (e.g., f"${item_price:.2f}")
    # Return the formatted string
    pass

# Test the functions
"""
item1 = ["Chips", 2.00, 10]
item2 = ["Water", 1.50, 10]
item3 = ["Candy", 1.00, 0]

print(get_name(item1))
print(get_name(item2))
print(get_name(item3))

print(get_price(item1))
print(get_price(item2))
print(get_price(item3))

print(get_stock(item1))
print(get_stock(item2))
print(get_stock(item3))

print(is_available(item1))
print(is_available(item2))
print(is_available(item3))

item1 = ["Chips", 2.00, 0]
item2 = ["Water", 1.50, 1]
item3 = ["Candy", 1.00, 0]

print(restock(item1, 1))
print(restock(item2, 3))
print(restock(item3, 5))

print(purchase(item1))
print(purchase(item2))
print(purchase(item3))

# Should see the following
# 1: Chips, $2.00, (Current stock: 0)
# 2: Water, $1.50, (Current stock: 3)
# 3: Candy, $1.00, (Current stock: 4)
print(item_tostring(item1, 0))
print(item_tostring(item2, 1))
print(item_tostring(item3, 2))
"""
