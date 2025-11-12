# --- Vending Machine Functions ---
# These functions will operate on the main 'items' list and 'balance'

def display_items(items_list):
    """
    - prints a statement of each item in the vending machine
    """
    print("Available Items:")
    # Use a 'for' loop with 'enumerate' to get both the index (i) and the item
    # for i, item in enumerate(items_list):
    #   Inside the loop, print the item string using your get_item_string() helper
    #   Remember to pass (i + 1) as the index so it's 1-based for the user
    pass


def insert_money(amount, current_balance):
    """
    - Check to see if the amount is positive ( > 0)
    - Add that amount to the balance of the vending machine
    - return a new balance
    - also handle a print message if they input an invalid amount
    """
    # Check if amount is positive
    # If so:
    #   Calculate a new_balance = current_balance + amount
    #   Print a message showing the amount added and the new_balance
    #   Return the new_balance
    # If not positive:
    #   Print f"That is not a valid amount"
    #   Return the current_balance unchanged
    pass


def select_item(index, items_list, current_balance):
    """
    - Handles the item selection and purchase logic.
    - Returns the new balance (0 if purchase is successful, otherwise the original balance).
    """
    # User sees 1-based index, list is 0-based.
    # Convert to a 0-based item_index (index - 1)

    # Check if the 0-based item_index is valid (within the bounds of items_list)
    # if 0 <= item_index < len(items_list):

    #   If valid, get the current_item from items_list

    #   Get the item's name and price using your helper functions

    #   Check if the item is available (using is_available helper)

    #   Check if the current_balance is sufficient (>= item's price)

    #   **Purchasing Logic**
    #   if not is_available(current_item):
    #       print(f"Sorry, {item_name} is out of stock.")
    #   elif current_balance < item_price:
    #       print(f"Insufficient funds. {item_name} costs ${item_price:.2f}.")
    #   else:
    #       # If all checks pass, purchase the item:
    #       # 1. Call your purchase() helper on the current_item
    #       # 2. Calculate the change (current_balance - item_price)
    #       # 3. Print the dispensing message: f"Dispensing {item_name}. Change returned: ${change:.2f}"
    #       # 4. Return 0 (to reset the balance)

    #   **Error Handling**
    # else: (if the index was invalid)
    #   print("Invalid selection. Please try again.")

    # If any check failed, return the balance unchanged
    # return current_balance
    pass