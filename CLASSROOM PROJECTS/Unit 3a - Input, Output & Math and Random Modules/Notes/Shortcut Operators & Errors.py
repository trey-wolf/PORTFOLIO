#
# Python Notes: Shortcut Operators and Common Errors
#

# --- Part 1: Shortcut Operators ---

# Shortcut operators provide a quick way to update a variable.
# They are also known as augmented assignment operators.

# Let's start with a variable.
x = 10

# Addition Assignment (+=)
# This adds a value to x.
print(f"Starting value of x: {x}")
x += 5  # This is the same as x = x + 5
print(f"After x += 5, x is now: {x}")

# Subtraction Assignment (-=)
# This subtracts a value from x.
print(f"Starting value of x: {x}")
x -= 3  # This is the same as x = x - 3
print(f"After x -= 3, x is now: {x}")

# Multiplication Assignment (*=)
# This multiplies x by a value.
print(f"Starting value of x: {x}")
x *= 2  # This is the same as x = x * 2
print(f"After x *= 2, x is now: {x}")

# Division Assignment (/=)
# This divides x by a value. The result is always a float.
print(f"Starting value of x: {x}")
x /= 4  # This is the same as x = x / 4
print(f"After x /= 4, x is now: {x}")

# SIDE NOTE
# You can do these shortcut operators with //, %, and ** as well
# However, typically those are less used compared to the basic 4

# --- Part 2: Understanding Common Errors ---

# There are three main types of errors you will encounter while coding.
# And you will need to know these for the AP Exam

# 1. Syntax Error:
# A syntax error is a grammatical mistake in your code.
# The program will not run at all.

# The line below is commented out because it would stop the program.
# It's missing a closing parenthesis.
# print("This line has a syntax error"

# 2. Runtime Error (or Exception):
# A runtime error occurs while the program is running.
# The code is grammatically correct, but something goes wrong during execution.

# The code below will cause a "ZeroDivisionError" when it runs.
# You cannot divide by zero in mathematics or in programming.
#
# UNCOMMENT THE NEXT TWO LINES TO SEE THE ERROR:
# numerator = 10
# denominator = 0
# print(numerator / denominator)

print("This line will print because the code above it is commented out.")

# 3. Logical Error:
# A logical error is the hardest to find. The program runs without crashing,
# but the result is incorrect because the logic is flawed.

# The code below has a logical error because it does not follow the
# correct order of operations to calculate an average.
num1 = 10
num2 = 20
num3 = 30
# The division happens before the addition, which is incorrect for an average.
bad_average = num1 + num2 + num3 / 3
print(f"Incorrect average: {bad_average}")

# To fix the logical error, we use parentheses to force the addition first.
correct_average = (num1 + num2 + num3) / 3
print(f"Correct average: {correct_average}")