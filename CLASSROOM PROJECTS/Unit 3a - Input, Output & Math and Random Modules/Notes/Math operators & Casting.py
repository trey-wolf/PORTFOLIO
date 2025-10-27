#
# Python Notes: Math Operators and Type Casting
#

# --- Part 1: Math Operators ---

# The basic math operators are used to perform calculations.
# Let's define three variables to use in our examples a, b and c.
a = 15
b = 4
c = 2

# Addition (+)
addition_result = a + b
print(f"Addition: {a} + {b} = {addition_result}")

# Subtraction (-)
subtraction_result = a - b
print(f"Subtraction: {a} - {b} = {subtraction_result}")

# Multiplication (*)
multiplication_result = a * b
print(f"Multiplication: {a} * {b} = {multiplication_result}")

# Division (/)
# The result is always a float.
division_result = a / b
print(f"Division: {a} / {b} = {division_result}")

# Floor Division (//)
# Divides and rounds down to the nearest whole number (an integer).
floor_division_result = a // b
print(f"Floor Division: {a} // {b} = {floor_division_result}")

# Modulo (%)
# Returns the remainder of the division.
modulo_result = a % b
print(f"Modulo: {a} % {b} = {modulo_result}")

# Exponentiation (**)
# Raises the first number to the power of the second number.
exponentiation_result = b ** c
print(f"Exponentiation: {b} ** {c} = {exponentiation_result}")

# --- Part 2: Type Casting ---

# Type casting is the process of converting a variable from one data type
# to another using built-in functions like str(), int(), and float().

# Let's define a users age as 24
# keep in mind that the data type of this is a string
user_age_str = "24"

# Here's what would happen if you forgot to cast it:
# You would get a TypeError because you can't add a number to a string.
#
# UNCOMMENT THE NEXT TWO LINES TO SEE THE ERROR:
# print("Next year, you will be " + user_age_str + 1)
# print(user_age_str + 1)

# Example 1: Casting from string to integer (int)
# We must cast the string to an int to do math with it.
user_age_int = int(user_age_str)
print(f"Your age is {user_age_int}.")
print(f"Next year, you will be {user_age_int + 1} years old.")

# Example 2: Casting from string to float (float)
# This is useful for numbers with decimals.
price_str = input("Enter the price of an item: ")
price_float = float(price_str)
tax_amount = price_float * 0.08  # Calculating a simple tax
print(f"The tax on a ${price_float} item is ${tax_amount:.2f}.")

# Example 3: Casting from integer or float to string (str)
# This is useful for combining numbers with strings without f-strings.
current_year = 2025
print("The current year is " + str(current_year) + ".")

pi_value = 3.14159
print("The value of PI is approximately " + str(pi_value) + ".")