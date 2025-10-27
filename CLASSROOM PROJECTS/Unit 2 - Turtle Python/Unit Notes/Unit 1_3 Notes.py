# The turtle module is used for creating simple graphics.
import turtle

# Creates a turtle called timmy.
timmy = turtle.Turtle()

# Creates the screen and its properties called screen.
screen = turtle.Screen()

# sets the shape of the turtle timmy to an arrow
timmy.shape("arrow")

# sets the background color of the screen to blue
# other example colors below in comments
screen.bgcolor("blue")

# screen.bgcolor("white")
# screen.bgcolor("black")
# screen.bgcolor("red")
# screen.bgcolor("green")
# screen.bgcolor("yellow")
# screen.bgcolor("orange")
# screen.bgcolor("purple")
# screen.bgcolor("pink")
# screen.bgcolor("brown")

# We can also set the background color to a red, blue, green (rgb) color code
# Sets the red, green and blue all to half intensity
screen.bgcolor(0.5, 0.5, 0.5)

# Sets the red to full intensity, green to half, blue to none
screen.bgcolor(1, 0.5, 0)

# If you dont like the intensity setting for bgcolor, we can change to a raw amount
# between the values of 0 to 255
# We do this by using the colormode function
# This function changes the colormode of turtles and the screen, not just the screen
turtle.colormode(255)

# Sets red to be at full, 255. Green to be at 200, and blue to be almost half at 150
screen.bgcolor(255, 200, 150)

# All these colorcodes and ways to make colors works with the turtles themselves too
# We learned how to change the color of turtles yesterday

# If we want a turtle to output text we can do that with the write function
# timmy will write Hello World from its current location
timmy.write("Hello World")

# In the write function we can specify the size and style
timmy.write("Hello World", font=("Arial", 20, "normal"))

"""
The font attribute
font works in the following way
font("Font Name", Font Size, "Font Style)
Examples
Font Name: A string for the font family, like "Arial", "Courier", or "Verdana", etc.
Font Size: An integer for the size in points, e.g., 12, 18, or 24, etc..
Font Style: A string for the style, such as "normal", "bold", or "italic".
"""

# --- Drawing a filled square ---
# Begin and End fill showcase

# Begin the fill process
# Any shape drawn after this command will be filled
timmy.begin_fill()

# Set the outline color to red
timmy.color("red")

# Set the fill color to blue
timmy.fillcolor("blue")

# Draw the first side of the square
timmy.forward(100)
timmy.right(90)

# Draw the second side
timmy.forward(100)
timmy.right(90)

# Draw the third side
timmy.forward(100)
timmy.right(90)

# Draw the fourth side
timmy.forward(100)
timmy.right(90)

# End the fill process
# This command fills the shape that was drawn between begin_fill() and end_fill()
timmy.end_fill()