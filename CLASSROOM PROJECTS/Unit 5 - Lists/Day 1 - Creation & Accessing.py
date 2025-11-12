"""
Unit 5: Lists - Day 1 Notes
"""

# --- What is a List? ---

"""
* A list is a collection of items that are grouped together 
  and accessed using a single name (identifier).
* Think of it as a variable that can hold multiple values at once.
"""

# --- Creating a List ---

"""
You create a list using square brackets [], with items separated 
by commas.
"""

# Creating an empty list:
myList = []

# Creating a list with items:

# A list of integers:
aplus = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# A list of floats:
price = [32.23, 12.25, 56.38, 77.55, 39.0]

# A list of strings:
coworkers = ["Sarah", "Matt", "Sophie"]


# --- List Indices ---

"""
* Items in a list are accessed using their index, which is 
  their numerical position.
* Important: List indices always start at 0, not 1.

Example: For the list coworkers = ["Sarah", "Matt", "Sophie"]:
* "Sarah" is at index 0
* "Matt" is at index 1
* "Sophie" is at index 2
"""


# --- Accessing and Modifying List Data ---

"""
You use the list's name followed by the index in square brackets [] 
to get or change the data at that position.
"""

# --- Accessing (Getting) Values ---

"""
You can print values or use them in expressions by referencing 
their index.
"""

# Example:
#                     INDICES
#         0    1    2    3    4    5    6
vals = [  2,   1,   31,  7,   5,   12,  8]

# Print specific elements
print("Accessing index 0:", vals[0])  # Output: 2
print("Accessing index 2:", vals[2])  # Output: 31

# You can also use expressions inside the brackets
print("Accessing index 1 + 2:", vals[1 + 2])   # Accesses index 3. Output: 7
print("Accessing index 9 - 3:", vals[9 - 3])   # Accesses index 6. Output: 8
print("Accessing index 11 // 2:", vals[11 // 2]) # Accesses index 5. Output: 12


# Example with strings:
#                INDICES
#          0        1        2
what = ["Sarah", "Matt", "Sophie"]

print("Accessing index 0:", what[0])  # Output: Sarah
print("Accessing index 2:", what[2])  # Output: Sophie


# --- Modifying (Changing) Values ---

"""
You can change an item in a list by assigning a new value to 
its index.
"""

# Example:
#                    INDICES
#              0        1        2
coworkers = ["Sarah", "Matt", "Sophie"]
print("Original list:", coworkers)

# Change the value at index 1
coworkers[1] = "Tim"

# The list is now: ["Sarah", "Tim", "Sophie"]
print("Modified list:", coworkers)