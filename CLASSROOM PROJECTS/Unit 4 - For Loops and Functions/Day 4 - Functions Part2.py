# Day 4 Notes: Functions with Parameters and Return Values

# What are parameters and return values?
# So far, our functions have been like self-contained units that just run a fixed set of instructions.
# But what if we want to make them more flexible?
#
# * **Parameters** are variables that let you pass information *into* a function. They act as placeholders for the data the function needs to work with. Think of them as the ingredients for your recipe.
# * A **Return Value** is the data that a function sends *back* to the code that called it. It's the finished dish from your recipe that you can then use elsewhere.

# ---

## Syntax for Parameters and Return Values

# 1. **Defining with Parameters:** You list the parameter names inside the parentheses.
#    These names are the local variables you'll use inside the function.
#
#    def function_name(parameter1, parameter2):
#        # Code can now use parameter1 and parameter2
#        # ...

# 2. **Calling with Arguments:** When you call the function, you provide the actual values,
#    called **arguments**, that will be assigned to the parameters.
#
#    function_name(value1, value2) # value1 is passed to parameter1, value2 to parameter2

# 3. **Using the `return` keyword:** To send a value back, use the `return` keyword.
#    When `return` is executed, the function stops immediately and sends the value back.
#
#    def add_numbers(num1, num2):
#        result = num1 + num2
#        return result # Sends the value of 'result' back

# ---

## The Importance of Scope

# Scope refers to the region of your code where a variable can be accessed. This is a crucial concept!

# * **Global Scope:** A variable created in the main body, before calling any functions, of your program is a **global variable**. It can be accessed from anywhere in your code, including inside functions.

# The key here is that a variable must be created before you call the function
# global_variable = 10
# def use_global():
#     print(global_variable)
#
# use_global()

# OR

# def use_global():
#     print(global_variable)
# global_variable = 10
# use_global()

# Both will print out 10 even though use_global has no parameter, because global_variable is global

# * **Local Scope:** A variable created *inside* a function is a **local variable**. It **only exists within that function**. It's like temporary scratch paper that the function uses and then throws away when it's done. You cannot access a local variable from outside its function.

# Understanding scope prevents bugs where you might accidentally change a variable you didn't mean to, or try to use a variable that doesn't exist where you're calling it.

# **Example of Scope in Action**
my_global_variable = "I am outside the function"

def scope_test():
    # This local variable has the same name, but it is completely separate!
    my_local_variable = "I am INSIDE the function"
    print(my_local_variable) # Prints the local variable's value
    print(my_global_variable) # We can ACCESS the global variable from inside

print("--- Scope Test ---")
scope_test()

print(my_global_variable) # This works perfectly fine.

# The line below will cause an ERROR because `my_local_variable` only exists inside the function.
# print(my_local_variable) # NameError: name 'my_local_variable' is not defined
print("--- End of Scope Test ---")

# IMPORTANT IDEA
# DO NOT name a local variable and a global variable the same thing.
# This can cause logical issues with scope as the local variable inside the function always takes precedence
# ---

## Example 1: Personalized Greeting (Parameters)

# This function takes a `name` as a parameter to make the greeting specific.
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")

# Now we call the function with different arguments.
print("\n--- Personalized Greetings ---")
greet_user("Alice")
greet_user("Bob")

# ---

## Example 2: Area of a Circle (Parameters and Return Value)

# This function takes a radius, calculates the area, and returns the result.
# We need the `math` module for the value of PI.
import math

def calculate_circle_area(radius):
    # 'area' is a local variable.
    area = math.pi * radius * radius
    return area # Send the calculated value back.

# To use the returned value, we must store it in a variable.
print("\n--- Circle Area Calculator ---")
# The value returned by the function is stored in circle1_area
circle1_area = calculate_circle_area(5)
print(f"A circle with a radius of {5} has an area of {circle1_area:.2f}.")

circle2_area = calculate_circle_area(12)
print(f"A circle with a radius of {12} has an area of {circle2_area:.2f}.")

# ---

## Example 3: Drawing Shapes with Turtle (Putting it all together)

# This is a great example of procedural abstraction. We create a flexible function
# that can draw a regular polygon of any size, color, and number of sides.
# We pass all the details the function needs as parameters.

import turtle

# --- Setup the turtle ---
screen = turtle.Screen()
screen.title("Drawing with Functions & Parameters!")
pen = turtle.Turtle()
pen.speed(5) # Make the turtle draw a bit faster

# 1. DEFINING a flexible drawing function.
# The parameters `num_sides`, `side_length`, and `pen_color` allow us
# to customize the shape each time we call the function.
def draw_polygon(num_sides, side_length, pen_color):
    # This angle calculation is a local variable.
    angle = 360 / num_sides
    pen.color(pen_color)
    pen.begin_fill()
    for _ in range(num_sides):
        pen.forward(side_length)
        pen.right(angle)
    pen.end_fill()


# 2. CALLING the function with different arguments to draw different shapes.
# Draw a blue triangle
draw_polygon(3, 100, "blue")

# Lift the pen and move to a new position to avoid drawing lines between shapes.
pen.penup()
pen.goto(150, 150)
pen.pendown()

# Draw a red square
draw_polygon(4, 80, "red")

pen.penup()
pen.goto(-150, 50)
pen.pendown()

# Draw a green hexagon
draw_polygon(6, 60, "green")

screen.exitonclick()