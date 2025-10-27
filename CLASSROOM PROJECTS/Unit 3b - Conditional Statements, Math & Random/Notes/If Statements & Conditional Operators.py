# Day 1: If Statements & Conditional Operators
# An if statement is a fundamental control structure that allows a program
# to make a decision based on a condition.
# It executes a block of code only if a condition is true.
# This allows us to break up the "sequence" of code running line by line

# Conditional operators (also called relational operators) are used to
# compare two values and produce a Boolean result (True or False).
# >   Greater than
# <   Less than
# ==  Equal to
# !=  Not equal to
# >=  Greater than or equal to
# <=  Less than or equal to

# Example 1: Using 'greater than' and 'less than'
age = 17
if age >= 16:
    print("You are old enough to drive.")

gpa = 3.5
if gpa < 2.0:
    print("You are on academic probation.")

# Example 2: Using 'equal to' and 'not equal to'
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")

password = "secure_password"
if password != "123456":
    print("Good password choice.")

# Example 3: Using a straight boolean value

is_running = True
if is_running:
    print("He's a runner.")

# A common way beginners type something like this is by doing the following.
if is_running == True:
    print("He's a runner.")

# This will not create a syntax error, but it is an improper way to handle a boolean condition.
# This is because our if statement checks, if a condition is True.
# the variable is_running is a statement, that is already True.
# therefore, checking if the is_running variable is True is completely unnecessary.