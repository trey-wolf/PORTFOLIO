# Day 5: The Random Module

# You must import the random module to use its functions.
import random

# --- 1. random.randrange(start, stop, step) ---
# Returns a randomly selected element from a range. 'stop' is not inclusive.
print("--- Using random.randrange() ---")
# Pick a random number from 1 to 9 (10 is not included)
lottery_number = random.randrange(1, 10)
print(f"Your lottery number is: {lottery_number}.")

# --- 2. random.randint(a, b) ---
# Returns a random integer between a and b, inclusive.
# This is different from randrange where b would be not inclusive
print("--- Using random.randint() ---")
die_roll = random.randint(1, 6)
print(f"You rolled a {die_roll}.")


# --- 3. random.random() ---
# Returns a random float between 0.0 and 1.0.
print("--- Using random.random() ---")
# This is useful for probability checks (e.g., 25% chance)
if random.random() < 0.25:
    print("You won the 25% chance prize!")
else:
    print("Sorry, try again.")
