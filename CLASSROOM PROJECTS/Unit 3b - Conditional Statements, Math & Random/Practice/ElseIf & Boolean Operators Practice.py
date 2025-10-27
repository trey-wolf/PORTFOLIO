# Day 2: Else-If & Boolean Operators Practice

# Problem 1: Check if a number is positive, negative, or zero.
# Use 'if' and 'elif' to print the correct category for the input variable 'number'.
number = input("Type in a number")


# Problem 2: Check for a valid login.
# A user must have both a username and a valid API key.
# Use an 'if' statement with the 'and' operator to check both conditions.
user_name = "coder123"
has_api_key = True


# Problem 3: Determine the movie rating.
# A movie is "PG-13" if its rating is 13 or higher. It's "G" otherwise.
# A movie is a "Blockbuster" if it's rated 13 or higher AND its budget is over 100 million.
# Use 'if and 'elif' with boolean operators.
movie_rating = 15
movie_budget_millions = 150


# Problem 4: Check if you are ready to go outside.
# You are ready to go outside if it's not raining OR it's a weekend.
# Use an 'if' statement with 'not' and 'or'.
is_raining = True
is_weekend = True


# --- Challenge Problem: Graduation Eligibility Checker ---
# You need to create a program that checks if a student is eligible to graduate
# First: Find the users graduating gpa by taking all gpas and averaging them together

# Don't forget to convert these (remember these inputs are strings)
f_year = input("type in your freshmen gpa")
so_year = input("type in your sophomore gpa")
j_year = input("type in your junior gpa")
s_year = input("type in your senior gpa")

# Second: Check to see if the user can graduate
can_graduate = False
# The user can graduate if the average gpa >= 2.0
# If they can graduate set the can_graduate variable to True

# Third: Check to see if they got any honors award
# Sets the initial value of award to an empty string
# This variables purpose is to store the string matching the award they get
# For example: award = "cum laude"
award = ""
# Along with changing the award variable output an f-string congratulating them on graduating and their award in each if statement
# - If they can graduate and their gpa is between 4.0 and 4.6 they are awarded the cum laude award
# - elif they can graduate and their gpa is between 4.6 and 5.2 they are awarded the magna cum laude award
# - elif they can graduate and their gpa is above 5.2 they are awarded the summa cum laude
# - elif they can graduate and their gpa is below 4.0 they are awarded no award, but still graduate
# - elif if they cannot graduate, output a sad message that they cannot graduate
f_year = input("type in your freshmen gpa")
f_year_int = int(f_year)
so_year = input("type in your sophomore gpa")
so_year_int = int(so_year)
j_year = input("type in your junior gpa")
j_year_int = int(j_year)
s_year = input("type in your senior gpa")
s_year_int = int(s_year)

average_gpa = (f_year_int + so_year_int + j_year_int + s_year_int) / 4

can_graduate = False
if average_gpa >= 2.0:
    can_graduate = True

award = ""
if can_graduate and average_gpa >= 5.2:
    award = "Summa Cum Laude"
elif can_graduate and average_gpa < 5.2 and average_gpa >= 4.6:
    award = "Magna Cum Laude"
elif can_graduate and average_gpa < 4.6 and average_gpa >= 4.0:
    award = "Cum Laude"

if not award == "" and can_graduate:
    print(f"Congratulations on graduating! ({award})")
elif not can_graduate:
    print("Sorry you dont get to graduate")

