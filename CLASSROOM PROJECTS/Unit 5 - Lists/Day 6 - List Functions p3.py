# --- .count() Method ---
"""
`count = my_list.count()` allows us to count the number of times
an element shows up in our list `my_list`
"""
nums = [1, 2, 3, 3, 3, 2, 1, 2, 3, 3]
count1 = nums.count(1)
count2 = nums.count(2)
count3 = nums.count(3)
count4 = nums.count(4) # the element 4 is not in the list
print(f"# of 1's: {count1}\n# of 2's: {count2}\n# of 3's: {count3}")
print(f"# of 4's: {count4}")
# --- .index() Method ---
"""
`index = my_list.index(x)` allows us to find the index of the first element, x
in our list `my_list`. It searches the list from left to right.
"""
nums = [1, 4, 5, 3, 3, 2, 1, 4, 5, 3]
count1 = nums.index(1)
count2 = nums.index(2)
count3 = nums.index(3)
count4 = nums.index(3)
print(f"index of 1: {count1}\nindex of 2: {count2}\nindex of 3: {count3}")
print(f"index of 3?: {count4}")

# What if the element is not in the list when we try to use the index method?
count0 = nums.index(0)
print(f"index of 0: {count0}")
# If you run the code, we get a runtime error.
# Similar to how you would error test pop and remove for a user input.
# You would want to error test for an element not existing in the list for the .index() method.

# index expansion
# Lets say I have the scenario where I want to find the 3 in between two indices in a list
# We can do this by specifying a start / stop point in the index call
# .index(x, start, stop) remember stop is excluded
# This WILL NOT be tested, but I want to show you it anyway.
nums = [1, 4, 5, 3, 3, 2, 1, 4, 5, 3]
count4 = nums.index(3, 4, 10)
print(count4)
# --- .copy() Method ---

"""
`new_list = my_list.copy()` creates a *shallow copy* of
the list. This is important!

If you just write `new_list = my_list`, both variables
point to the *same* list in memory. Changing one
will change the other.

.copy() creates a brand new, independent list.
"""

# Example WITHOUT .copy() (This is the "wrong" way)
list_a = [1, 2, 3]
list_b = list_a  # list_b is just another name for list_a
list_b.append(4)
print(f"List A (wrong way): {list_a}") # Output: [1, 2, 3, 4]
print(f"List B (wrong way): {list_b}") # Output: [1, 2, 3, 4]

# Example WITH .copy() (This is the "right" way)
list_x = [1, 2, 3]
list_y = list_x.copy() # list_y is a new, separate list
list_y.append(4)
print(f"List X (right way): {list_x}") # Output: [1, 2, 3]
print(f"List Y (right way): {list_y}") # Output: [1, 2, 3, 4]


# --- .clear() Method ---

"""
`my_list.clear()` removes *all* items from the list, 
leaving you with an empty list.
"""
junk_drawer = ["tape", "keys", 8, "screws"]
print(f"Junk drawer: {junk_drawer}")

junk_drawer.clear()
print(f"Cleared drawer: {junk_drawer}") # Output: []