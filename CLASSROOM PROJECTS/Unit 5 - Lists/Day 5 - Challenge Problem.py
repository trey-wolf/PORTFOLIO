# 1. GLOBAL VARIABLE: The shopping list
shopping_list = []

## 2. REQUIRED ABSTRACTION FUNCTIONS ##

def add_item(item_to_add):
    # Use the append() function here
    print(f"Added '{item_to_add}'.\n")
    shopping_list.append(item_to_add)

def remove_item(item_to_remove):
    # Use the remove() function here (Remember error handling!)
    pass

def sort_items():
    # Use the sort() function here
    print("List sorted alphabetically.\n")

def insert_item(index, item_to_add):
    # Use the insert() function here (Remember error handling for index! Similar to how we would handle pop error handling.)
    pass

def cross_out_item(index):
    # Use the pop() function here (Remember to return the value and handle errors!)
    pass

def show_shopping_list():
    # This function should simply loop through the entire list and show everything in the list with a respective index
    # The index should be represented starting at 1 NOT 0. When a user sees a position of something, they usually don't think in terms
    # of 0 indexing like we would in programming
    # This is something you will have to handle with later on in the main program loop

    # for example:
    # 1. Apples
    # 2. Bananas
    # 3. Oranges
    #    etc.
    pass


## 3. MAIN PROGRAM LOOP ##

is_running = True
while is_running:
    print("\n--- Smart Shopping List ---")
    print("current list:\n")
    show_shopping_list()
    print("\nMENU:")
    print("1: Add item (append)")
    print("2: Remove item by name (remove)")
    print("3: Sort list (sort)")
    print("4: Insert item at position (insert)")
    print("5: Go to Store")
    print("6: Exit\n")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '2':
        # call the show_shopping_list function
        # Add logic to get item from the user and call remove_item()
        pass
    elif choice == '3':
        # call sort_items function
        # call the show_shopping_list function
        pass
    elif choice == '4':
        # call the show_shopping_list function
        # Add logic to get index and item from the user, then call insert_item()
        pass
    elif choice == '5':
        # 0a. create a variable called `total` and set it equal to 0
        # 0b. create a variable called `is_shopping` and set it equal to True
        # 1. write a while loop that continues to loop until we are done shopping
        # 2. call the `show_shopping_list` function
        # 3. ask the user what index they want to pop off their list
        #    keep in mind, the user sees the index starting at 1, so you will need to subtract 1 from their input.
        # 4. call the `cross_out_item` function and store it into a variable called `crossed_out_item`
        #    when we cross out the item, we are "grabbing it off the shelf"
        #    the item is removed and ready to be purchased.
        # 5. generate a random float between 1 and 10
        #    you can use the following code if you would like: cost = random.random() * 10
        # 6. add the `cost` to your `total` variable
        # 7. Once we pop everything off the list (aka len is 0) -> set `is_shopping` to False
        # 8. Outside the loop print the total cost of the shopping list
        pass
    elif choice == '6':
        print("Thank you for using the Smart Shopping List! Goodbye.\n")
        # What do you need to change to make sure we stop the loop? What variable?
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")

