"""
================================
Unit 5: Lists - Day 2 Notes
================================

Day 2 focuses on functions and methods that let us
modify and work with lists.

A "method" is a function that belongs to an object
(in this case, the list). We call it using dot notation,
like:  my_list.method_name()
"""

# --- len() Function ---

"""
`len(list_name)` is a built-in function (not a method)
that returns the number of items currently in the list.
"""
numbers = [10, 20, 30]
count = len(numbers)
print(f"The list has {count} items.") # Output: The list has 3 items.


# --- .append() Method ---

"""
`my_list.append(item)` adds a new item to the 
*very end* of the list. This modifies the original list.
"""
pets = ["Dog", "Cat"]
print(f"Original pets: {pets}")

pets.append("Fish")
print(f"After append: {pets}") # Output: ['Dog', 'Cat', 'Fish']

pets.append("Lizard")
print(f"After append: {pets}") # Output: ['Dog', 'Cat', 'Fish', 'Lizard']


# --- .insert() Method ---

"""
`my_list.insert(index, item)` inserts a new item at 
the specified index. All items from that index onward 
are shifted one position to the right.
"""
letters = ['A', 'C', 'D']
print(f"Original letters: {letters}")

# Insert 'B' at index 1
letters.insert(1, 'B')
print(f"After insert: {letters}") # Output: ['A', 'B', 'C', 'D']