"""
Day 3: Processing Lists With Loops

This file contains notes on the two main ways to loop through
lists in Python: the standard 'for' loop (with an index)
and the 'for each' loop (with an item).
"""

# ========================================
# Review of 'for' and 'for each' loop
# ========================================

# --- for loop (using index) ---

# The 'for' loop will loop through every index in your list.
# The loop variable (e.g., 'x') will be set to each index, one by one.

# Syntax example:
# for x in range(len(list)):
#     pass


# --- for each loop (using item) ---

# The 'for each' loop will loop through every item in your list.
# The loop variable (e.g., 'x') will be set to each item, one by one.

# Syntax example:
# for x in list:
#     pass


# ========================================
# For loop example (using range)
# ========================================

print("--- Example 1: 'for' loop ---")
myList = []
for num in range(5):
    myList.append(num)
print(myList)

# OUTPUT:
# [0, 1, 2, 3, 4]


# ========================================
# For loop example (summing with index)
# ========================================

print("\n--- Example 2: 'for' loop (index) ---")

# NOTE: Using 'list' as a variable name is generally
# bad practice because it "shadows" the built-in
# list() function. We use it here to match the slide.
list = [56, 65, 98, 2, 25]
total = 0
for x in range( len( list ) ) :
    total += list[ x ]
print(total)

# OUTPUT:
# 246


# ========================================
# For each loop example (printing items)
# ========================================

print("\n--- Example 3: 'for each' loop ---")
bob = [56,65,98,2,25]
for num in bob:
    print(num)

# OUTPUT:
# 56
# 65
# 98
# 2
# 25


# ========================================
# For each loop example (summing items)
# ========================================

print("\n--- Example 4: 'for each' loop ---")
list = [56, 65, 98, 2, 25]
total = 0
for num in list:
    total += num
print(total)

# OUTPUT:
# 246