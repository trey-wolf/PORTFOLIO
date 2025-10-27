# Day 2 Notes: The While Loop

# What is a while loop?
# A while loop is used to repeat a block of code as long as a certain
# condition is True. Unlike a for loop, you don't need to know how many
# times you need to repeat beforehand. The loop continues until the
# condition becomes False.

# ---

## Syntax and Walkthrough

# The basic syntax for a while loop is:
#
# while condition:
#     # Code to be repeated goes here
#     # This code must be indented!

# Let's break it down:
# 'while' -> The keyword that starts the loop.
# 'condition' -> A boolean expression (evaluates to True or False).
#                As long as it's True, the loop will run.
# ':' -> The colon at the end is required to start the indented block of code.

# A 'while' loop requires three key parts for counting:
# 1. Initialization: Create a variable and set its starting value before the loop.
# 2. Condition: The test in the 'while' line that checks the variable.
# 3. Update: Change the variable inside the loop. If you forget this, you
#    will create an INFINITE LOOP!

# ---

# **Example 1: Basic Counting**
# Let's use a while loop to count from 0 to 4, just like in the for loop example.

print("Starting the first loop...")

# 1. Initialization
counter = 0

# 2. Condition
while counter < 5:
    print("The current value of counter is:", counter)

    # 3. Update
    # We add 1 to the counter in each loop iteration.
    # Without this line, 'counter' would always be 0, and the loop would run forever!
    counter = counter + 1
    # A common shorthand for this is: counter += 1

print("First loop has finished!")

# --- WALKING THROUGH THE CODE ---
# 1. A variable 'counter' is created and set to 0.
# 2. The loop begins. It checks the condition: is 0 < 5? Yes, it's True.
# 3. The code inside runs. It prints "The current value of counter is: 0".
# 4. The counter is updated. 'counter' is now 1.
# 5. The loop goes back to the top and re-checks the condition: is 1 < 5? True.
# 6. It prints the message for 1 and updates 'counter' to 2.
# 7. This continues for 2, 3, and 4.
# 8. After printing for 4, 'counter' is updated to 5.
# 9. The loop re-checks the condition: is 5 < 5? No, it's False.
# 10. The condition is now False, so the loop stops, and the program
#     continues to the line "First loop has finished!".

# ======================================================================

## Example 2: Mathematical Algorithm (Factorial)

# Let's calculate a factorial again, this time with a while loop.
# Remember, 5! = 5 * 4 * 3 * 2 * 1 = 120.

print("\n--- Factorial Calculator (while loop version) ---")

# Get a number from the user
num_input = int(input("Enter a positive number to find its factorial: "))

# A variable to store the final result
factorial_result = 1

# 1. Initialization
current_number = 1

# 2. Condition: Loop as long as the number we are multiplying by is less
#    than or equal to the user's input number.
while current_number <= num_input:
    factorial_result = factorial_result * current_number

    # 3. Update: Move to the next number
    current_number = current_number + 1

print(f"\nThe factorial of {num_input} is {factorial_result}.")

# ======================================================================

## Controlling a Loop: break and continue

# Sometimes you need more control over your loop than just the 'while' condition.
# Python gives us two keywords to handle this: `break` and `continue`.

# ---
# The `break` Statement
# ---
# The **`break`** keyword immediately **terminates the loop**. It doesn't just end the
# current iteration, it exits the entire loop and the program continues with the
# next line of code after the loop.
# Think of it as an emergency exit from the loop.

print("\n--- `break` statement example ---")
print("Counting up to 10, but stopping if we see the number 5.")
i = 0
while i < 10:
    if i == 5:
        print("Found the number 5! Breaking out of the loop.")
        break  # Exit the loop now!

    print(i)
    i += 1
print("Loop finished.")  # This line runs after 'break' is called.

# ---
# The `continue` Statement
# ---
# The **`continue`** keyword immediately ends the **current iteration** and jumps
# back to the top of the loop to check the condition again. Any code inside
# the loop after the `continue` statement is skipped for that one iteration.
# Think of it as a "skip this round" button.

print("\n--- `continue` statement example ---")
print("Printing numbers from 0 to 6, but skipping the number 3.")
j = 0
while j < 7:
    if j == 3:
        print("Found 3! Skipping this iteration with `continue`.")
        j += 1  # IMPORTANT! We still need to update our counter!
        continue  # Jump back to the top of the 'while' loop

    print(j)
    j += 1
print("Loop finished.")

# ======================================================================

## Example 3: User Input (A Simple Guessing Game)

# A while loop is perfect for situations where you need to wait for a
# specific user input. In this game, the loop will continue running
# as long as the user's guess is not correct. We don't know if it will
# take the user 1 try or 20 tries!

print("\n--- Guess the Number Game! ---")
print("I'm thinking of a number between 1 and 10.")

secret_number = 7
user_guess = 0  # Initialize with a value that is NOT the secret number

# The loop will run as long as the user's guess is not the secret number.
while user_guess != secret_number:
    # Get input from the user INSIDE the loop
    user_guess = int(input("Enter your guess: "))

    # Use if/elif statements to give the user hints
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")

# This line will only be reached AFTER the loop condition becomes False.
# The only way for that to happen is if user_guess == secret_number.
print(f"\nCongratulations! You guessed it! The secret number was {secret_number}.")

number = 1
total = 0

while number <= 4:
    number += 1
    if total >= 10:
        continue
    total += number

print(total)

