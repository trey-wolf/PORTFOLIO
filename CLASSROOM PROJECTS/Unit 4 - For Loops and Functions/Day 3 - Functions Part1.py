# Day 3 Notes: Introduction to Functions (No Parameters)

# What is a function?
# A function is a named block of reusable code that performs a specific task.
# Think of it like a recipe: you write the instructions once (defining the function),
# and then you can use that recipe whenever you want by its name (calling the function).

# This helps you:
# 1. Stay organized: Group related code together.
# 2. Avoid repetition: Write code once and use it multiple times.
# 3. Procedurally Abstract: Hiding the complex details of a process inside a function and giving it a simple, descriptive name. This allows you to manage the complexity of your program.
#    Think about a microwave button that says "Popcorn" 🍿. You don't need to know the exact power level or time the microwave uses. You just press the "Popcorn" button, and the procedure for making popcorn runs automatically. The button is an **abstraction** for a more complex process.

# Advantages of using procedural abstraction
# * **It simplifies your main code:** Instead of seeing a complex `for` loop and angle calculations, your main code just has a simple call like `draw_star()`. This makes your program easier to read, test, and debug.
# * **It promotes code reuse:** You can call `draw_star()` multiple times without copying and pasting the complex logic.
# * **It helps with collaboration:** One programmer can write a function to solve a specific problem, and other programmers can use that function without needing to understand its internal details.

# ---

## Defining vs. Calling a Function

# There are two main steps to using a function:

# 1. **Defining the function:** This is where you create the function and write the
#    code that goes inside it. The code is NOT executed yet. It's just the recipe.

#    The syntax is:
#    def function_name():
#        # Code to be executed goes here
#        # This code MUST be indented!

#    - `def` is the keyword that tells Python you are defining a function.
#    - `function_name` is the name you choose. It should be descriptive!
#    - `()` are the parentheses. For now, they will be empty.
#    - `:` The colon marks the start of the function's code block.

# 2. **Calling the function:** This is where you actually run the code inside the
#    function. To call it, you just type its name followed by parentheses.

# The syntax is:
# function_name()

# ---

## How the Computer Evaluates a Function Call

# When you call a function, the computer follows these steps:
# 1. The program executes line by line from the top.
# 2. When it sees a function call (e.g., `show_welcome_message()`), it pauses its
#    current execution.
# 3. It **jumps** to the `def show_welcome_message():` line where the function was defined.
# 4. It runs all the code inside the function's indented block from top to bottom.
# 5. Once the last line of the function is finished, the computer **returns** to the
#    spot where the function was originally called and continues executing from the next line.

# ---

# **Example 1: A Simple Welcome Message**

# 1. DEFINING the function.
# This block of code does nothing by itself. It's just a stored set of instructions.
def show_welcome_message():
    print("========================")
    print("Welcome to my program!")
    print("Have a great day!")
    print("========================")


# 2. CALLING the function.
# These lines will actually execute the code inside the function above.
print("Let's show the welcome message for the first time:")
show_welcome_message()

print("\nWe can do other things in our program now.")
print("And then we can show the welcome message again without re-writing it!")
show_welcome_message()

# ---

## Example 2: A "Roll the Dice" Mini-Game

# This function will use the `random` module and `if` statements to
# simulate rolling two dice and checking for doubles.

import random


# 1. DEFINING the game logic in a function.
def roll_for_doubles():
    print("\n--- Rolling the Dice! ---")
    # Generate two random numbers between 1 and 6
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print(f"You rolled a {die1} and a {die2}.")

    # Use an if statement to check if they are the same
    if die1 == die2:
        print("Congratulations! You rolled doubles!")
    else:
        print("Better luck next time.")


# 2. CALLING the function to play the game.
# Each time we call it, a new set of random numbers will be generated.
roll_for_doubles()
roll_for_doubles()

# ---

## Example 3: Drawing a Star with Turtle

# Functions are great for drawing, because you often redraw the same shapes.
# Let's create a function to draw a star, which involves a repetitive pattern.

import turtle

# --- Setup the turtle ---
screen = turtle.Screen()
screen.title("Drawing with Functions!")
pen = turtle.Turtle()
pen.color("gold")
pen.pensize(3)


# 1. DEFINING the drawing instructions.
def draw_star():
    # A star has 5 points. We can draw it by repeating a forward
    # and turn motion 5 times.
    for _ in range(5):
        pen.forward(150)
        pen.right(144)  # 144 degrees is the magic angle for a 5-pointed star


# 2. CALLING the function to draw the star.
print("\nDrawing the star now...")
draw_star()
print("Star drawing complete!")

# You can now easily move the pen and draw another one!
pen.penup()
pen.goto(-200, 100)
pen.pendown()
pen.color("red")
draw_star()  # Reusing our code!

screen.exitonclick()

def product(x, y):
    result = x * z
    print(f"The product of the numbers is {result}")

product(2,3)

