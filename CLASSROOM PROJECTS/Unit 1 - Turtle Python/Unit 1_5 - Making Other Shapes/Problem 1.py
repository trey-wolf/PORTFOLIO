"""
Objective: Draw a vibrant shape-sorting toy.
You'll create a rectangular base and then draw five different shapes on top of it:
a square, a star, a circle, a semicircle, and a triangle.

Draw the Base:
Use penup() and goto() to move your turtle to a starting point for the large rectangular base of the toy.
Use begin_fill() and end_fill() to draw a filled rectangle in a neutral color like gray or brown.

Draw the Shapes:
Use penup() and goto() to move your turtle to a new position for each of the five shapes you need to draw.
For each shape (square, star, circle, semicircle, triangle), use a different, bright, vibrant color for both
the fill and the outline.

Make sure each shape is drawn completely on top of the rectangular base.

Add a Title:
Move your turtle to the top of the screen.
Use the write() function to give your creation a title, such as "Shape Sorter."
Use the font parameter to make the title stand out with a larger size and bold style.
"""
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
turtle.colormode(255)
t = turtle.Turtle()
t.speed(5)
t.pensize(2)

# --- Draw the rectangular base ---
t.penup()
t.goto(-200, -150)
t.pendown()
t.color(100, 100, 100) # Gray color
t.begin_fill()
t.fillcolor(150, 150, 150) # Lighter gray fill
t.forward(400)
t.left(90)
t.forward(300)
t.left(90)
t.forward(400)
t.left(90)
t.forward(300)
t.left(90)
t.end_fill()

# Write your code after here