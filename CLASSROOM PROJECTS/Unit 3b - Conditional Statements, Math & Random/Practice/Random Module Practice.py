# Day 5: Random Module Practice

import random

# Problem 1: Roll an eight-sided die.
# Use random.randint() to simulate rolling a eight-sided die (1-8).
# Print the result.


# Problem 2: Pick a random number from a specific range.
# Use random.randrange() to pick a random number between 5 and 15 (inclusive of 5, not 15).
# Print the result.


# Problem 3: Simulate a coin flip.
# Use random.randint() to get a 0 or 1.
# If the result is 0, print "Heads". If it's 1, print "Tails".


# Problem 4: Simulate a 50% chance.
# # Use random.random() to create a condition that is true about half the time.
# # Print "Success!" or "Failure." based on the outcome.


# --- Challenge Problem: The Number Guessing Game ---
# Create a simple game where the user tries to guess a random number.
#
# 1. Use random.randint() to generate a random number between 1 and 10.
#    Store it in a variable called 'secret_number'.
#
# 2. Use the input() function to ask the user to guess a number between 1 and 10.
#    Convert the input to an integer using int(). Store it in a variable
#    called 'user_guess'.
#
# 3. Use an 'if-else' statement to compare 'user_guess' to 'secret_number'.
# 4. If they are the same, print "You guessed it! You win!"
# 5. If they are different, print "Sorry, that's not the number. Try again."