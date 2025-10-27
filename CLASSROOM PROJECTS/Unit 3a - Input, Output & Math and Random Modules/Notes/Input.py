"""
User Input in Python

What is 'input'?

The **input()** function in Python is used to get data from the user. It pauses
your program and waits for the user to type something and press the 'Enter' key.
Whatever the user types is then returned as a value.

A crucial thing to remember is that the `input()` function **always returns a
string** (str), even if the user types a number. This is a common point of
confusion for new programmers.

### Basic Input Syntax

The basic syntax is simple: `variable = input("prompt")`

The "prompt" is a string that is displayed to the user before they type. It's
a good practice to use a clear and concise prompt so the user knows what to do.

Examples:
"""
# Getting the user's name
name = input("Please enter your name: ")
# An f-string is a string prefixed with 'f' that allows you to embed variables in curly braces {}.
print(f"Hello, {name}!")

# Getting a number from the user (but it's a string!)
age_str = input("How old are you? ")
print(f"You are {age_str} years old.")
print(f"The data type of 'age_str' is: {type(age_str)}")

"""
Notice in the example above, even though the user entered a number, the
`type()` function shows it's a string. This means you can't do math with it
directly.

--------------------------------------------------------------------------------

Good Input Techniques

### 1. Always use a clear prompt.
A good prompt tells the user exactly what to enter. A bad prompt (or no prompt
at all) leaves the user confused.

- **Bad:** `name = input()`
- **Good:** `name = input("What is your full name? ")`

### 2. Convert data types when needed.
Since `input()` always returns a string, you often need to convert it to a
different data type (like `int` or `float`) if you plan to use it in calculations.
You do this using **type casting**.

- **`int()`:** Converts a string to an integer.
- **`float()`:** Converts a string to a float.

Example:
"""
# Get input and convert it to an integer for calculations
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert the strings to integers
num1 = int(num1_str)
num2 = int(num2_str)

# Now you can perform math operations
total = num1 + num2
print(f"\n{num1} + {num2} = {total}")

# Get input and convert it to a float for calculations
price_str = input("Enter the price of an item: ")
price = float(price_str)
print(f"The price is ${price:.2f}")

"""
### 3. Combine the prompt and conversion.
For cleaner code, you can perform the `input()` and the type conversion on the
same line.

Example:
"""
# Cleaner way to get an integer
grade = int(input("What is your grade? "))
print(f"Your grade is {grade}")

# Cleaner way to get a float
weight = float(input("Enter your weight in pounds: "))
print(f"Your weight is {weight} lbs.")