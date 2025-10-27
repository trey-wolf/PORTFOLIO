# Day 1 Notes: For Loops with the range() function

# What is a for loop?
# A for loop is used for repeating a block of code a known number of times.
# Think of it as telling the computer, "Do this exact thing X times."

# ---

## Syntax and Walkthrough

# The basic syntax for a for loop with the range() function is:
#
# for variable in range(number):
#     # Code to be repeated goes here
#     # This code must be indented!

# Let's break it down:
# 'for' -> The keyword that starts the loop.
# 'variable' -> A temporary variable that holds the current count of the loop.
#              You can name this almost anything (commonly 'i' for 'index').
# 'in' -> The keyword that connects the variable to the range.
# 'range(number)' -> This function generates a sequence of numbers, starting
#                    from 0 by default, and ending *before* the specified number.
# ':' -> The colon at the end is required to start the indented block of code.

# ---

# **Example 1: Basic Counting**
# Let's see how the loop variable changes with each repetition (iteration).

print("Starting the first loop...")
for i in range(5):
    # The code inside the loop will run 5 times.
    # The range(5) generates numbers 0, 1, 2, 3, 4.
    print(f"The current value of i is: {i}")

print("First loop has finished!")

# --- WALKING THROUGH THE CODE ---
# 1. The loop starts. 'range(5)' creates the sequence 0, 1, 2, 3, 4.
# 2. Iteration 1: The variable 'i' is set to the first value, which is 0.
#    The code prints "The current value of i is: 0".
# 3. Iteration 2: 'i' is automatically updated to the next value, 1.
#    The code prints "The current value of i is: 1".
# 4. Iteration 3: 'i' becomes 2. It prints the message with 2.
# 5. Iteration 4: 'i' becomes 3. It prints the message with 3.
# 6. Iteration 5: 'i' becomes 4. It prints the message with 4.
# 7. The 'range' sequence is now finished. The loop stops, and the program
#    continues to the line "First loop has finished!".

# ======================================================================

## The range() Function in Detail

# The `range()` function is powerful because it can be used in three different ways.
# It generates a sequence of numbers that your for loop can use.

# ---
# Way 1: range(stop) - One Argument
# ---
# This is the most common way. You provide one number, which is the **stopping point**.
# The sequence will always **start at 0** and **end one number before** the stop value.
#
# `range(4)` generates the numbers: 0, 1, 2, 3

print("\n--- Testing range(stop) ---")
for i in range(4):
    print(i) # Will print 0, then 1, then 2, then 3

# ---
# Way 2: range(start, stop) - Two Arguments
# ---
# Here, you specify both a **start** and a **stop** value.
# The sequence will start at the 'start' number and still end one number before the 'stop' value.
#
# `range(1, 5)` generates the numbers: 1, 2, 3, 4

print("\n--- Testing range(start, stop) ---")
for i in range(1, 5):
    print(i) # Will print 1, then 2, then 3, then 4

# ---
# Way 3: range(start, stop, step) - Three Arguments
# ---
# This gives you the most control. You provide a **start**, a **stop**, and a **step**.
# The 'step' is the amount to jump by between numbers.
#
# `range(0, 10, 2)` generates: 0, 2, 4, 6, 8 (starts at 0, adds 2 each time, stops before 10)
#
# The step can also be a negative number to count backwards!
# `range(5, 0, -1)` generates: 5, 4, 3, 2, 1 (starts at 5, subtracts 1, stops before 0)

print("\n--- Testing range(start, stop, step) ---")
print("Counting up by 2s:")
for i in range(0, 10, 2):
    print(i)

print("\nCounting down by 1:")
for i in range(5, 0, -1):
    print(i)

# ======================================================================

## Example 2: Mathematical Algorithm (Factorial)

# A factorial is the product of all positive integers up to a given number.
# For example, the factorial of 5 (written as 5!) is 5 * 4 * 3 * 2 * 1 = 120.
# We can use a for loop to calculate this!

print("\n--- Factorial Calculator ---")

num = 5
result = 1

for n in range(1, num + 1):
    result = result * n
print(result)

# ======================================================================

## Example 3: Drawing with the Turtle Module

# For loops are perfect for drawing shapes because shapes often involve
# repeating the same steps. A square has 4 equal sides and 4 equal angles.
# So, we can repeat "move forward" and "turn right" 4 times.

import turtle

# --- Setup the turtle ---
screen = turtle.Screen()
screen.title("Drawing a Square with a For Loop!")
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.pensize(4)

# --- The Loop ---
# We want to repeat the drawing commands 4 times.
# We use an underscore '_' for the loop variable because we don't actually
# need to use the count (0, 1, 2, 3) for anything inside the loop.
# It's a common Python convention for a variable that you don't intend to use.

for _ in range(4):
    pen.forward(150)  # Move the turtle forward by 150 pixels
    pen.right(90)     # Turn the turtle right by 90 degrees

# Keep the window open until it's clicked
screen.exitonclick()

# That's it! Using a for loop is much cleaner than writing the
# pen.forward() and pen.right() commands 4 times each.