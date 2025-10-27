"""
Introduction to Python: Day 1

What is a 'print' statement?

In Python, the **print()** statement is a built-in function used to display
output on the console (the screen). It's one of the first things you'll
learn, outside of turtle, because it's how you make your program communicate with you.

You can print a variety of things such as text and numbers.
When you want to print text, you must enclose it in single quotes (')
or double quotes (").

Examples:
"""
# Printing a simple message
print("Hello, world!")

# Printing a number
print(123)

"""
--------------------------------------------------------------------------------

What are Escape Sequences?

An **escape sequence** is a special combination of characters used inside a
string to represent a character that would otherwise be difficult or
impossible to type.

In Python, all escape sequences begin with a backslash (\). When Python sees
a backslash inside a string, it knows the next character has a special meaning.

### Common Escape Sequences ###

- **\n (Newline):** This sequence moves the cursor to the next line.
  It's like pressing the 'Enter' key on your keyboard.

- **\t (Tab):** This sequence inserts a horizontal tab space. It's
  useful for creating neatly aligned columns of text.

- **\\ (Backslash):** If you want to print a literal backslash, you have to
  use two of them. The first backslash "escapes" the second one, so Python
  knows you want to print it and not treat it as the start of an escape sequence.

Examples:
"""

# Using \n to create a newline
print("This is the first line.\nThis is the second line.")
# Expected output:
# This is the first line.
# This is the second line.


# Using \t for a tab space
print("Name:\t\tAge:\t\tCity:")
print("Alice\t\t25\t\tNew York")
print("Bob\t\t30\t\tLondon")
# Expected output:
# Name:          Age:          City:
# Alice          25            New York
# Bob            30            London


# Using \\ to print a backslash
# This is important for file paths!
print("C:\\Users\\Guest\\Documents")
# Expected output:
# C:\Users\Guest\Documents