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