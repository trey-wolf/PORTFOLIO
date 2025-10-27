# Day 3: Else Statements
# An 'else' statement provides a "catch-all" block of code.
# It is executed only when the preceding 'if' and 'elif' conditions
# (if any) are all false. It must be the last statement in a conditional block.

# Example 1: An if-else structure
age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 2: Checking if a number is even or odd
number = 5

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Example 3: Categorizing a grade
# If-elif-else structure

grade = 89
if grade >= 90:
    print("Your grade is an A!")
elif grade >= 80:
    print("Your grade is a B.")
elif grade >= 70:
    print("Your grade is a C.")
else:
    print("You are failing. :(")


# For beginner programmers I see this as a solution for the above problem, categorizing a grade
# The reason why this is an issue because the value of grade being 89 is True for both
# lines 43 and 45. This is a logical error because a grade shouldn't have two categories

"""
grade = 89
if grade >= 90:
    print("Your grade is an A!")
if grade >= 80:
    print("Your grade is a B.")
if grade >= 70:
    print("Your grade is a C.")
if grade < 70:
    print("You are failing. :(")
"""