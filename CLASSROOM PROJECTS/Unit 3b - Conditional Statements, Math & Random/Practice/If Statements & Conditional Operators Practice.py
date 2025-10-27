# Day 1: If Statements & Conditional Operators Practice

# Problem 1: Check if the temperature is below freezing.
# Use an 'if' statement and a conditional operator to print a message
# if the temperature is less than or equal to 32.
temperature = 30


# Problem 2: Check for a specific username.
# Use an 'if' statement to print "Welcome, admin!" if the variable
# 'username' is exactly "admin".
username = "admin"


# Problem 3: Check if a number is positive.
# Use an 'if' statement to check if 'num' is greater than 0.
num = 15


# Problem 4: Check if a score is passing.
# A passing score is 70 or higher. Print "You passed!" if the score meets this condition.
score = 85


# Problem 5: Check for inequality.
# Use the 'not equal to' operator to print a message if the variable
# 'current_day' is not "Sunday".
current_day = "Saturday"


# Problem 6: Fix the boolean check.
# The following code works, but it's an improper way to check a boolean value.
# Rewrite the 'if' statement to be more concise and proper.
is_logged_in = True
if is_logged_in == True:
    print("Welcome back!")


# --- Challenge Problem: The Access Control System ---
# The goal is to create a simple program that grants access to a system.
# The user needs to enter a password that matches the correct one.
#
# 1. Create a variable called 'correct_password' and set it to "Python123".
# 2. Ask the user to enter a password using the input() function and store it
#    in a variable called 'user_password'.
# 3. Use an 'if' statement to check if the user's password matches the correct password.
# 4. If they match, print "Access Granted. Welcome to the system."
# 5. If they do not match, print "Access Denied. Incorrect password."
correct_password = "Python123"
user_password = input("Type in your password")
if user_password == correct_password:
    print("Access Granted. Welcome to the system.")
if user_password != correct_password:
    print("Access Denied. Incorrect password.")