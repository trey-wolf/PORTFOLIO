# --- Python List Methods: Practice Problems ---

"""
Instructions:
For each problem, write the Python code to solve it.
Start with the provided list and modify it as requested.
"""

# --- .remove() Problems ---

# Problem 1:
guest_list = ["Alice", "Bob", "Charlie", "David"]
# "Charlie" can no longer make it to the event.
# Write code to remove "Charlie" from the guest_list.
# Print the final guest_list.


# Problem 2:
inventory = ["apple", "banana", "orange", "apple", "banana"]
# A customer just bought one "apple".
# Write code to remove "apple" from the inventory.
# Print the updated inventory.


# --- .pop() Problems ---

# Problem 3:
tasks = ["Wash dishes", "Do homework", "Walk the dog", "Call friend"]
# You just completed the *last* task on your list.
# Write code to remove the last task.
# Store the removed task in a variable called 'completed_task'.
# Print the 'completed_task'.
# Print the remaining 'tasks' list.


# Problem 4:
contestants = ["Michael", "Sarah", "Kevin", "Jenna", "Chris"]
# The contestant at index 2 ("Kevin") has been disqualified.
# Write code to remove the contestant at index 2.
# Print the list of remaining contestants.


# --- .sort() Problems ---

# Problem 5:
numbers = [42, 11, 99, 3, 15, 78]
# Write code to sort this list of numbers in ascending order.
# Print the sorted list.


# Problem 6:
high_scores = [1200, 850, 2100, 1500, 975]
# You are building a leaderboard and need to show the best scores first.
# Write code to sort the 'high_scores' list from highest to lowest.
# Print the sorted leaderboard.


# --- Error Handling Problems ---

# Problem 7:
pantry = ["Cereal", "Milk", "Sugar", "Flour"]
# Write code that asks the user for an item to remove from the pantry.
# If the item is in the list, remove it and print the updated pantry.
# If the item is *not* in the list, print a message like:
# "Sorry, [item_name] is not in the pantry."


# Problem 8:
letters = ["a", "b", "c", "d", "e"]
# Write code that asks the user for an *index* to remove.
# Convert the user's input to an integer.
# Check if the index is valid (i.e., it exists within the list).
# If the index is valid, remove the item at that index and print the new list.
# If the index is "out of range" (not valid), print a message like:
# "Error: Invalid index."