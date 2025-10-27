# ================================================
# Practice Problems
# ================================================

# Problem 1: write a for loop that will print hello, 6 times

# Problem 2: write a for loop that will add all integers between 3 and 8, inclusive

# Problem 3: write a for loop that will have a turtle create a triangle
import turtle
tina = turtle.Turtle()
# For loop here

# ================================================
# Evaluate Code
# ================================================
# For these problems practice 'tracing' the code and evaluating the output
# Consider getting a piece of paper and writing out the evaluation
# Run the code to confirm your result
# Problem 1
num_result = 1
for i in range(2, 6):
    num_result *= i
print(num_result)

# Problem 2
a = 5
b = 10
for i in range(2, 9, 2):
    a += i
    b -= i
result = a + b
print(result)

# Problem 3
num_result3 = 0
for i in range(1234567890):
    num_result3 *= i
print(num_result3)

# DONT DELETE
turtle.done()
turtle.bye()
# DONT DELETE