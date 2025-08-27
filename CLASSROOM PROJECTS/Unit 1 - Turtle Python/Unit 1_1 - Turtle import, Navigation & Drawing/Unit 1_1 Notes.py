# import is needed to load the turtle module into python
import turtle
# creates a turtle called tina
tina = turtle.Turtle()
# creates the screen and its properties called screen
screen = turtle.Screen()

# sets the screen size to a 400 x 400 canvas
screen.screensize(400,400)

# forward and back functions
# the value you put in the parenthesis changes how many pixels she moves
# allows tina to move 100 pixels in the direction she is facing
tina.forward(100)

# allows tina to move 100 pixels in the opposite direction she is facing
tina.back(100)

# goto function
# allows tina to move to a specific location on the canvas
# goes in the order of (x, y) and the origin is the middle of the canvas
# moves tina to (0, 0) - the middle of the screen
tina.goto(0, 0)

# Negative values
# for the forward and back functions
# placing a negative value in the parenthesis will move the turtle
# in the opposite direction the functions specifies
# moves tina back 100 pixels
tina.forward(-100)

# moves tina forward 100 pixels
tina.back(-100)

# PEN TOOL
# the pen tool allows a turtle draw
# sets tina's pen in the "down" state and allows her to start drawing
tina.pendown()

# sets tina;s pen in the "up" state and allows her to stop drawing
tina.penup()