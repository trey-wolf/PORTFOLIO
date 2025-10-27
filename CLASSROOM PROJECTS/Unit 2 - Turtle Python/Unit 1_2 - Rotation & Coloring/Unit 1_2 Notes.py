# The turtle module is used for creating simple graphics.
import turtle

# Creates a turtle called timmy.
timmy = turtle.Turtle()

# Creates the screen and its properties called screen.
screen = turtle.Screen()

# sets the shape of the turtle timmy to an arrow
timmy.shape("arrow")

# sets timmy's speed to "instant"
timmy.speed(0)

# sets timmy's speed to the slowest speed
timmy.speed(0)

# sets timmy's speed to the fastest speed
timmy.speed(10)

# Rotation functions
# Rotation is measured in degrees.
# By default, 0 degrees is to the right (east).
# right() rotates the turtle clockwise by the value in parentheses.
# Rotates timmy 90 degrees clockwise.
timmy.right(90)

# left() rotates the turtle counter-clockwise by the value in parentheses.
# Rotates timmy 90 degrees counter-clockwise.
timmy.left(90)

# Negative values
# Placing a negative value in the parenthesis will move the turtle
# in the opposite direction the function specifies.
# Rotates timmy 90 degrees counter-clockwise.
timmy.right(-90)

# Rotates timmy 90 degrees clockwise.
timmy.left(-90)

# Color functions
# color() changes the turtle's color.
# You can use common color names as strings.
timmy.color("blue")


# Comments
# Comments are lines of code that are ignored by the Python interpreter.
# They are used to explain code and make it more readable.
# A good comment should be descriptive of the code that is being referenced.
# Comments are created by using the "#" character.
# This is a single-line comment.

"""
This is a multi-line comment.
You can use triple quotes to write a comment
that spans multiple lines.
"""

# Example of a good comment:
# Red in order to check for first test case.
timmy.color("red")