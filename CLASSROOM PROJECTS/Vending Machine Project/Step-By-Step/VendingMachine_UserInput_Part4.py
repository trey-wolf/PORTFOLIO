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


def get_item_string(item, index):
    """
    Returns an f-string that outputs the state of any item object in the following way:
    {index}: {item_name}, ${item_price}, (Current stock: {item_stock})
    """
    # Use your get_name, get_price, and get_stock helpers
    # Format the price to 2 decimal places (e.g., f"${price:.2f}")
    # Return the formatted string
    pass


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


# --- Admin Menu Helper Functions ---

def admin_restock_item(items_list):
    """Handles the logic for restocking an item."""
    # --- RESTOCK LOGIC ---
    # Display all items (call display_items(items_list))
    # Wrap in a try/except ValueError block
    # Ask which item number to restock (1-based index)
    # Validate the index using error handling
    # Ask how many to add (as an int)
    # Call the restock() helper function
    # Print success/failure message
    pass


def admin_add_item(items_list):
    """Handles the logic for adding a new item."""
    # --- ADD NEW ITEM LOGIC ---
    # Wrap in a try/except ValueError block
    # Prompt for a new item 'name' (string)
    # Prompt for a new item 'price' (float)
    # Prompt for a new item 'stock' (int)
    # Create the new item list: new_item = [name, price, stock]
    # Append it to the main list: items_list.append(new_item)
    # Print a success message
    # Handle the ValueError (e.g., if price/stock is not a number)
    pass


def admin_remove_item(items_list):
    """Handles the logic for removing an item."""
    # --- REMOVE ITEM LOGIC ---
    # Display all items (call display_items(items_list))
    # Wrap in a try/except ValueError block
    # Ask which item number to remove (1-based index)
    # Convert to 0-based index: remove_index = int(input(...)) - 1
    # Validate the index (if 0 <= remove_index < len(items_list))
    #   Use items_list.pop(remove_index) to remove it
    #   Print a success message
    # else:
    #   Print "Invalid item number"
    # Handle the ValueError
    pass


def admin_change_price(items_list):
    """Handles the logic for changing an item's price."""
    # --- CHANGE PRICE LOGIC ---
    # Display all items (call display_items(items_list))
    # Wrap in a try/except ValueError block
    # Ask which item number to change (1-based index)
    # Convert to 0-based index: change_index = int(input(...)) - 1
    # Validate the index
    #   Ask for the new_price (as a float)
    #   Get the item: item_to_change = items_list[change_index]
    #   Update the price: item_to_change[1] = new_price
    #   Print a success message
    # else:
    #   Print "Invalid item number"
    # Handle the ValueError
    pass


def admin_menu(items_list, admin_password):
    """
    - Handles the admin workflow.
    - Modifies the items_list directly.
    """
    # Prompt the user for the 4-digit admin password

    # if password == admin_password:
    #   Print "Access granted."

    #   Start an inner loop for the admin menu
    #   admin_running = True
    #   while admin_running:
    #     Print the admin menu options:
    #     "1: Restock item"
    #     "2: Add new item"
    #     "3: Remove item"
    #     "4: Change item price"
    #     "5: Exit admin menu"
    #     admin_choice = input("Choose admin option: ")

    #     if admin_choice == "1":
    #       admin_restock_item(items_list)

    #     elif admin_choice == "2":
    #       admin_add_item(items_list)

    #     elif admin_choice == "3":
    #       admin_remove_item(items_list)

    #     elif admin_choice == "4":
    #       admin_change_price(items_list)

    #     elif admin_choice == "5":
    #       --- EXIT ADMIN MENU ---
    #       Set admin_running = False
    #       Print "Exiting admin mode."

    #     else:
    #       Print "Invalid admin option."

    # else: (if password was wrong)
    #   print("Password is incorrect")
    pass

# --- Main Program Execution ---
# This 'run' logic is now the main script.


# This is our main data structure
items = [
    ["Chips", 2.00, 10],
    ["Soda", 1.50, 8],
    ["Candy", 0.75, 12],
    ["Water", 1.00, 5]
]

# These variables store the machine's state
balance = 0
admin_password = "1234"

keep_running = True
while keep_running:
    print("\n=== Vending Machine ===")
    # Call the display_items function
    display_items(items)

    print(f"Current Balance: ${balance:.2f}")
    print("\nOptions:")
    print("1: Insert money")
    print("2: Select item")
    print("3: Admin Menu")  # Updated option 3
    print("4: Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        # --- Insert Money ---
        # Use a try/except ValueError block
        # Prompt the user for the amount (as a float)
        # Call insert_money() and *update* the balance variable
        # e.g., balance = insert_money(amount, balance)
        pass

    elif choice == "2":
        # --- Select Item ---
        # Use a try/except ValueError block
        # Prompt the user for the item number (as an int)
        # Call select_item() and *update* the balance variable
        # e.g., balance = select_item(index, items, balance)
        pass

    elif choice == "3":
        # --- Admin Menu ---
        # Call the admin_menu() function
        # Pass in the 'items' list and 'admin_password'
        admin_menu(items, admin_password)  # Call the renamed function

    elif choice == "4":
        # --- Quit ---
        # Set keep_running to False
        # Check if balance > 0, if so, print a message to return their change
        # Print a goodbye message
        pass

    else:
        print("Invalid choice. Please try again.")