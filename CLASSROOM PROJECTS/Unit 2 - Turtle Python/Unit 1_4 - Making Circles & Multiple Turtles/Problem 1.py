"""
Objective: Draw a traffic light using a pole and three filled circles for the lights.
Your Challenge:
Set Up the Scene:
Create a turtle screen and change its background color using screen.bgcolor().
Use a turtle to draw a filled rectangle for the traffic light pole. You'll need to use begin_fill()
end_fill(), and functions like forward() and right() to draw the shape.

Draw the Lights:
Use penup() and goto() to move your turtle to the correct positions for each light.
Use begin_fill() and end_fill() along with the circle() function to draw a
red, yellow, and green light.
Make sure to set a different fillcolor() for each circle before you draw it.

Add a Sign:
Use penup() and goto() to position your turtle near the top of the pole.
Use the write() function to add a sign or message, like "GO", "SLOW", or "STOP,"
near the corresponding light.
Experiment with the font parameter to change the appearance of your text.
"""
import turtle
# Set up the screen
screen = turtle.Screen()
screen.bgcolor("gray")
turtle.colormode(255)

# Create the turtle
t = turtle.Turtle()
t.pensize(3)
t.speed(5)
t.hideturtle()

# OPTIONAL EXTENSION
# 1. Green arrow for dedicated turn to left
# 2. Instead of just drawing the traffic light, animate it over time
#    Have it start with a green arrow / green solid circle for 10 seconds
#    then go to yellow for 5 seconds
#    Then red for 15 seconds