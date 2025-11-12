# --- Item Helper Functions ---
# These functions replace the methods from the Item class
# They operate on a single item list, e.g., ["Chips", 2.00, 10]

def get_name(item):
    """Returns the name of the item."""
    return item[0]


def get_price(item):
    """Returns the price of the item."""
    return item[1]


def get_stock(item):
    """Returns the stock of the item."""
    return item[2]


def is_available(item):
    """Returns True/False if the stock of item is positive ( > 0)."""
    return get_stock(item) > 0


def restock(item, amount):
    """
    - If the amount is positive ( > 0) add that amount to the stock of item.
    - Return True if you restocked an item, False otherwise.
    """
    if amount > 0:
        item[2] += amount  # item[2] is the stock
        return True
    return False


def purchase(item):
    """
    - If the stock is available, reduce the stock by 1.
    - Return True if you purchased an item, False otherwise.
    """
    if is_available(item):
        item[2] -= 1  # item[2] is the stock
        return True
    return False


def get_item_string(item, index):
    """
    Returns an f-string that outputs the state of any item object in the following way:
    {index}: {item_name}, ${item_price}, (Current stock: {item_stock})
    """
    # Using {:.2f} to format the price to two decimal places
    return f"{index}: {get_name(item)}, ${get_price(item):.2f}, (Current stock: {get_stock(item)})"


# --- Vending Machine Functions ---
# These functions replace the methods from the VendingMachine class
# They operate on the main 'items' list and 'balance'

def display_items(items_list):
    """
    - prints a statement of each item in the vending machine using the items toString method
    """
    print("Available Items:")
    for i, item in enumerate(items_list):
        # We use i + 1 to show a 1-based index to the user
        print(get_item_string(item, i + 1))


def insert_money(amount, current_balance):
    """
    - Check to see if the amount is positive ( > 0)
    - Add that amount to the balance of the vending machine
    - return a message of how much money they inserted and what their balance is
    - also handle a print message if they input an invalid amount
    """
    if amount > 0:
        new_balance = current_balance + amount
        print(f"Added ${amount:.2f}. Current balance: ${new_balance:.2f}")
        return new_balance
    else:
        print(f"That is not a valid amount")
        return current_balance  # Return the balance unchanged


def select_item(index, items_list, current_balance):
    """
    - Handles the item selection and purchase logic.
    - Returns the new balance (0 if purchase is successful, otherwise the original balance).
    """
    # User sees 1-based index, list is 0-based
    item_index = index - 1

    if 0 <= item_index < len(items_list):
        current_item = items_list[item_index]
        item_name = get_name(current_item)
        item_price = get_price(current_item)

        if not is_available(current_item):
            print(f"Sorry, {item_name} is out of stock.")
        elif current_balance < item_price:
            print(f"Insufficient funds. {item_name} costs ${item_price:.2f}.")
        else:
            # 1. Purchase the item (reduces stock)
            purchase(current_item)

            # 2. Reduce the balance by the items price (calculate change)
            change = current_balance - item_price

            # 3. Print message
            print(f"Dispensing {item_name}. Change returned: ${change:.2f}")

            # 4. Set balance back to 0
            return 0
    else:
        print("Invalid selection. Please try again.")

    # If any check failed, return the balance unchanged
    return current_balance


def restock_items(items_list, admin_password):
    """
    - Handles the admin restock workflow.
    - Modifies the items_list directly.
    """
    password = input("Enter the 4-digit admin password: ")
    if password == admin_password:
        print("Access granted. Restocking mode activated.")
        available_indices = []
        for i, item in enumerate(items_list):
            # Print each item using its 1-based index
            print(get_item_string(item, i + 1))
            available_indices.append(i + 1)  # Store the 1-based index

        try:
            restock_choice = int(input("Which item do you want to restock? (Enter number): "))
            if restock_choice in available_indices:
                restock_amt = int(input("How many do you want to add? "))

                # Get the 0-based index for the list
                item_to_restock = items_list[restock_choice - 1]

                if restock(item_to_restock, restock_amt):
                    print(
                        f"Restocked: {get_name(item_to_restock)} with {restock_amt}. New stock: {get_stock(item_to_restock)}")
                else:
                    print("Invalid restock amount. Must be positive.")
            else:
                print("Not a valid item")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Password is incorrect")


# --- Main Program Execution ---
# This 'run' logic is now the main script.
if __name__ == "__main__":

    # This is our main data structure, replacing self.items
    items = [
        ["Chips", 2.00, 10],
        ["Soda", 1.50, 8],
        ["Candy", 0.75, 12],
        ["Water", 1.00, 5]
    ]

    # These variables replace self.balance and self.admin_password
    balance = 0
    admin_password = "1234"

    keep_running = True
    while keep_running:
        print("\n=== Vending Machine ===")
        display_items(items)
        print(f"Current Balance: ${balance:.2f}")
        print("\nOptions:")
        print("1: Insert money")
        print("2: Select item")
        print("3: Restock items (Admin only)")
        print("4: Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to insert: "))
                # Update the balance variable with the new balance
                balance = insert_money(amount, balance)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            try:
                index = int(input("Enter item number: "))
                # Update the balance variable (will be 0 on success)
                balance = select_item(index, items, balance)
            except ValueError:
                print("Invalid selection. Please enter a number.")

        elif choice == "3":
            # Pass the items list to be modified
            restock_items(items, admin_password)

        elif choice == "4":
            keep_running = False
            if balance > 0:
                print(f"Don't forget your change: ${balance:.2f}")
            print("Thank you! Have a nice day.")

        else:
            print("Invalid choice. Please try again.")