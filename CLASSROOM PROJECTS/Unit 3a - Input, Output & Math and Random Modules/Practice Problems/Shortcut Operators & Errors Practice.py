#
# Practice: Shortcut Operators & Errors
#
# This practice file will test your knowledge of shortcut operators
# and your ability to identify different types of errors.
#

# --- Practice Problems ---

# Problem 1: Use a shortcut operator to add 10 to the `points` variable. Print the new value.
points = 50


# Problem 2: Use a shortcut operator to subtract 7 from the `items_in_stock` variable. Print the new value.
items_in_stock = 35


# Problem 3: Use a shortcut operator to multiply the `price` variable by 2. Print the new value.
price = 15.50


# Problem 4: Use a shortcut operator to divide the `distance` variable by 5. Print the new value.
distance = 100


# Problem 5 (Logical Error): Look at the code below. It has a logical error.
# The goal is to calculate the final amount after adding 50 to the starting value and then
# multiplying the result by 2.
# Find the error and fix it so that the program prints the correct answer, which should be 300.
#
# starting_value = 100
# final_amount = starting_value + 50 * 2
# print(f"The final amount is: {final_amount}")


# Problem 6 (Syntax Error): The code below has Syntax Errors.
# The program won't even run.
# Find the errors and fix the code so that it correctly prints "Ready to code!".

# 1message = Ready to code
# print message

# Problem 7 (Runtime Error): The code below has a Runtime Error.
# It will run, but it will crash when it tries to perform an invalid operation.
# Find the error and fix it so the program runs without crashing.

# x = 15
# y = 0
# result = x / y
# print(f"The result is: {result}")


# --- Challenge Problem ---
#
# The Galactic Fuel Calculator
# Mission Objective: Find and fix the bugs, then add new features!
#

# --- DO NOT MODIFY THE FOLLOWING LINES ---
distance_light_years = 50
cargo_weight = 100 # in metric tons
cost_of_fuel = 2000000 # per metric ton, in solari
# ----------------------------------------

# Fix the syntax error here:
print("Calculating fuel cost for a mission of" distance_light_years "light years.")

# Based on the variable name, total_fuel_cost
# Fix the logical error here:
total_fuel_cost = distance_light_years * cargo_weight

# Add your new features below this line:
# ---- Calculation Features ----
# Feature 1: Use a shortcut operator to add a fixed 100000 to the total fuel cost for maintenance.
# Feature 2: Use a shortcut operator to add a 12.99% tax to the fuel
# Feature 3: Use a shortcut operator to subtract a fixed 99999 to the total fuel cost for being part of the spacing guild
# Feature 4: Create a new variable called crew_salary, and use the final total fuel cost * 2.79
# Feature 5: Create a new variable called captains_salary that subtracts 20% of the crews salary and stores it into captains_salary
# Feature 6: Using a shortcut operator divide out the remaining salary for this trip among 28 crewmen

# ---- Output Features ----
# Make sure all these outputs are formatted and describe what is being shown (use an f-string)
# Feature 7: Output the modified total fuel cost for this trip from the calculations above
# Feature 7: Output the captains salary
# Feature 8: Output the divided salary of each crew member

# Example of the final print statement (you will need to modify this):
print(f"The total fuel cost for the mission is: {total_fuel_cost} units.")
