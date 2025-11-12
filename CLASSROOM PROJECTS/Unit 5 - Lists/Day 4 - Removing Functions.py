# --- .remove() Method ---

"""
`my_list.remove(item_value)` searches for the *first* occurrence of `item_value` in the list and removes it.
This modifies the original list.

If the item is not found, it will cause a ValueError.
"""
colors = ["Red", "Green", "Blue", "Green"]
print(f"Original colors: {colors}")

colors.remove("Green")
print(f"After remove: {colors}")  # Output: ['Red', 'Blue', 'Green']

# --- .pop() Method ---

"""
`my_list.pop(index)` removes the item at the specified
index and *returns* it (so you can save it to a variable).

If you don't provide an index ( my_list.pop() ), it will 
remove and return the *last* item in the list.
"""
stack = [100, 200, 300, 400]
print(f"Original stack: {stack}")

# Remove item at index 1
removed_item = stack.pop(1)
print(f"Removed item: {removed_item}")  # Output: 200
print(f"Stack after pop(1): {stack}")  # Output: [100, 300, 400]

# Remove the last item
last_item = stack.pop()
print(f"Removed last item: {last_item}")  # Output: 400
print(f"Stack after pop(): {stack}")  # Output: [100, 300]

# --- .sort() Method ---

"""
`my_list.sort()` modifies the list in place, sorting the items.

- For numbers, it sorts numerically (ascending).
- For strings, it sorts alphabetically (ascending).

It does *not* return a new list; it changes the original.
"""

# Example 1: Sorting Integers
numbers = [5, 1, 8, 3, 2]
print(f"\nOriginal numbers: {numbers}")
numbers.sort()
print(f"Sorted numbers (ascending): {numbers}")  # Output: [1, 2, 3, 5, 8]

# Example 2: Sorting Strings
fruits = ["Banana", "Apple", "Cherry", "Date"]
print(f"\nOriginal fruits: {fruits}")
fruits.sort()
print(f"Sorted fruits (alphabetical): {fruits}")  # Output: ['Apple', 'Banana', 'Cherry', 'Date']

# Example 3: Using the 'reverse' parameter
"""
You can sort in descending order by passing `reverse=True`
"""
numbers_desc = [5, 1, 8, 3, 2]
print(f"\nOriginal numbers (for reverse): {numbers_desc}")
numbers_desc.sort(reverse=True)
print(f"Sorted numbers (descending): {numbers_desc}")  # Output: [8, 5, 3, 2, 1]

# --- Error Handling with 'if' Statements ---

"""
Both .remove() and .pop() can cause errors if used incorrectly.
- .remove(x) causes a ValueError if 'x' is not in the list.
- .pop() causes an IndexError if the list is empty.

We can use 'if' statements to prevent these crashes.
"""

# Example 1: Safely using .remove()
nums = [3, 6, 9, 12]
n = int(input("give an element"))

if n in nums:
    nums.remove(n)
    print(f"removed the element {n}")
else:
    print(f"The element {n} is not in the list")

# Example 2: Safely using .pop()

nums = [3, 6, 9, 12]
i = int(input("give an index"))

if i < len(nums) and i >= 0:
    nums.pop(i)
    print(f"removed the element at {i}")
else:
    print("Out of range")

