"""
Project: The Dynamic Shape Drawer
Goal: Use ONE function to draw different shapes by changing its arguments when called.

Your task is to build a single, flexible function called `draw_shape`.
This function will be our "drawing engine." We will tell it WHAT to
draw and HOW BIG to draw it by passing it different arguments.
"""
# This function will have 3 parameters
# shape_type: controls what we are drawing. Either a square or triangle
# size: controls how many symbols we will use to draw
# symbol: what kind of symbol we are going to use
def draw_shape(shape_type, size, symbol):
    print(f"\n--- Drawing a {shape_type} of size {size} with '{symbol}' ---")
    if size <= 0:
        # if the size is less than or equal to 0, print an error message
        print("Your size must be bigger than 0")
    else:
        # Check what `shape_type` is
        if shape_type == "square":
            # If it's a "square", use a `for` loop that runs `size` times.
            # Each time we iterate we will print a *full line* of symbols.
            # You can achieve this by simply doing print(symbol * size).
            # Write your 'square' logic here (1-2 lines of code)
            pass # 'pass' is a placeholder, you can delete it once you have written code

        elif shape_type == "triangle":
            # If it's a "triangle", use a `for` loop that counts from 1 up to the size of our triangle (included).
            # For each iteration, print the `symbol` multiplied by the *current iteration* of the for loop.
            # This is done in a similar way how you did the square but slightly different.
            # Write your 'triangle' logic here (1-2 lines of code)
            pass

        else:
            # If the shape_type is unknown, print an error message
            pass

    # This print() just adds a newline after the shape is drawn
    print()


# --- Step 2: Test The Function ---
#
# Now, let's "call" your function with different *arguments*
# to see how its output changes.
#
# The code in `draw_shape` stays the same, but the *results*
# will be different based on what we pass in.

# Test 1: A 5x5 square of asterisks
# Call draw_shape() with shape_type "square", size 5, and symbol "*"

# Test 2: A triangle of size 7 made of hashes
# Call draw_shape() with shape_type "triangle", size 7, and symbol "#"

# Test 3: A 3x3 square of dollar signs
# Call draw_shape() with shape_type "square", size 3, and symbol "$"

# Test 4: An unknown shape
# Call draw_shape() with shape_type "circle", size 6, and symbol "O"

# --- Step 3: User-Controlled Art! ---
# Once you have finished testing and verified that your function is working as intended,
# One thing you can do is click the arrow next to the function name.
# This will `hide` the function from view which is a good representation of what abstraction does for us.

# Now use a `while` loop to let the user decide what to draw.
# This is the "main" part of your program.
# You may delete the tests or simply comment them out.

print("\n--- Welcome to the Dynamic Shape Drawer! ---")
# Write a `while True` loop
# 1. Ask the user for a shape_type ("square", "triangle", or "quit")
# 2. If they type "quit", use `break` to exit the loop.
# 3. Ask the user for a `size` (and convert it to an int).
# 4. Ask the user for a `symbol`.
# 5. Call your `draw_shape` function with the user's three variables as arguments!
#
# Your `draw_shape` function doesn't need to change at all.
# Your loop will just *use* it.

# --- Step 4: (OPTIONAL) Add a 'Pyramid' Shape! ---
#
# Modify your function to draw a third shape, a pyramid.
#
# 1. Add an `elif shape_type == "pyramid":` to your `draw_shape` function.
#
# 2. A pyramid is tricky. For a `size` of 5, it should look like this:
#
#        *
#       ***
#      *****
#     *******
#    *********
#
# 3. HINT: You will need a `for` loop that runs `size` times
#    (e.g., `for i in range(size)`).
#
# 4. HINT: Inside the loop, you need to calculate two things for each line:
# #    a) The number of spaces to print before the symbols.
# #    b) The number of symbols to print.
#
# 5. After you add the logic, test it! Call `draw_shape("pyramid", 5, "*")`
#    and try to use it in your `while` loop!