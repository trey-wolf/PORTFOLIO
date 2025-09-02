"""
Practice Problem 1: The Birthday Card
Objective: Create a virtual birthday card using a background color, text, and a filled shape.
Your Challenge:
Change the background of the screen to a festive color of your choice.
Draw a filled party hat using begin_fill() and end_fill().
The hat can be a simple triangle with a some lines coming out of the top like a pom-pom
Make sure the fill color is different from the outline color!

Write a birthday message (e.g., "Happy Birthday!") on the screen using the write() function.
Experiment with the font parameter to change the font, size, and style of the text.

Remember to use penup() and goto() to position your turtle where you want the
hat and text to be drawn.

Website that could be useful to find out the angles and size of an isosceles triangle
https://www.omnicalculator.com/math/isosceles-triangle
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
# Some things you could consider adding to your hat / scene
# 1. More Pom-Pom lines
# 2. Shapes on hat
# 3. Shapes in the scene
# 4. Rainbow text (each character a different color)
# 5. More text / Personalize it
# 6. Some other 6th thing