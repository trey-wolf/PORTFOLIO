# Day 3: Else Statement Practice

# Problem 1: Check if a user is an administrator.
# Use an 'if-else' structure to check if the 'user_role' variable is "admin".
# Print "Access granted" if true, otherwise print "User privileges applied."
user_role = "user"


# Problem 2: Check if a number is a multiple of 3.
# Use the modulo operator (%) and an 'if-else' structure to check
# if the 'number' is a multiple of 3.
number = 14


# Problem 3: Check a variable's state.
# Create a variable 'is_online' and set it to False.
# Use an 'if-else' statement to print "Server is online" / "Server is offline."


# Problem 4: Check if a value is within a range.
# Check if the variable 'value' is between 10 and 20.
# Then check if the variable 'value' is between 20 and 30.
# Print "In range" if it is between 10 and 20, "almost in range" if between 20 and 30, and "Out of range" otherwise.
value = input("Type in a value")


# --- Challenge Problem: 9 weeks average calculator ---
"""
Write a program that will calculate the average of a students 9 weeks grades
The program should include a way to ask the user what level of class they are in
The options are 'level', 'honors', or 'AP'

Use the following weights to calculate the averages correctly
Use an if-elif-elif-else statement
- If they are in level -> minor assignments = 0.6, major assignments = 0.4
- If they are in honors -> minor assignments = 0.65, major assignments = 0.35
- If they are in AP -> minor assignments = 0.7, major assignments = 0.3
- If they type in none of the 3 options assume they are in level and use the level weights

Then ask the user the following two things
- the users average minor assignment grade
- the users average major assignment grade

Calculate the weighted average by taking the average of each assignment 
and multiplying by the correct weight and adding those together

Using an f-string output the final 9 weeks average to the user
"""
# Press the arrow to open an alternate solution
"""
You could simplify this by doing the following
if grade_level == "ap":
    ...
elif grade_level == "honors":
    ...
else:
    ...
"""
grade_level = input("What level course? (level, honors, ap)")
if grade_level == "level":
    minor_weight = 0.4
    major_weight = 0.6
elif grade_level == "honors":
    minor_weight = 0.35
    major_weight = 0.65
elif grade_level == "ap":
    minor_weight = 0.3
    major_weight = 0.7
else:
    minor_weight = 0.4
    major_weight = 0.6

# average for each type of assignments
minor_average = float(input("Type in your minor assignment average: "))
major_average = float(input("Type in your major assignment average: "))

# total weighted average with the assignment weights
total_average = (minor_average * minor_weight) + (major_average * major_weight)

print(f"Your average score is: {total_average}")