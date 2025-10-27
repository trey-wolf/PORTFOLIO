# Question 1: Floor Division (3 choices)
a = 10
b = 4

print(a // b)
# Answer: 2

# Question 2: Exponentiation (3 choices)
a = 10
b = 4

print(a ** b)
# Answer: 16
# Question 3: Modulo (3 choices)
a = 10
b = 4

print(a % b)
# Question 4-5: Basic math 2 operations (3 choices (all used))
x = 15
y = 6
z = 4

print(x + y - z)

print(x + y * z)

# Question 6: Determine correct algorithm
candy_to_give = 3
cost_per_bag = 5.99
candies_per_bag = 67
budget = 25.00

bags_bought = budget // cost_per_bag
# MISSING CODE #
print(f"Trick or Treaters Served: {trick_or_treaters_served}")

trick_or_treaters_served = (bags_bought * candies_per_bag) // candy_to_give

trick_or_treaters_served = (bags_bought * candies_per_bag) * candy_to_give

trick_or_treaters_served = (bags_bought * candies_per_bag) + candy_to_give

trick_or_treaters_served = (bags_bought * candies_per_bag) - candy_to_give
# Print the results
print(f"You can buy {bags_bought} bags of candy.")
print(f"You can give candy to {trick_or_treaters_served} trick-or-treaters.")
# Question 7-8: Escape Sequence (2 choices (all used))

print("This\tis just\na\n\'test\'")
print("This \\is\\ just\ta\ttest")

# Question 9: Error type matching (each error type)

# print("4ppl3")
#
# print(4pple)
#
# print(4/0)
#
# Print("No Error")

# Question 10: Fixing a logical error type
name = input("What is your name?")
age = input("What is your age?")

print("Welcome {name}, congrats on being {age}")
# Question 11: Input -> Output

num = input("Enter the first number")
num = input("Enter the second number")

print(num)
print(num)

# Question 12: Fix Input casting
age = input("What is your age")
print(f"You can vote in {18 - age} years")

# Question 13: Correctly casting
# Question 14: fstring
name = "Ricky"
AGE = 35
is_racer = True
speed = 201.20

print(f"Racer? -> {is_racer}")
print(f"{name} Bobby goes fast, at the age of {age}")
print(f"{speed} is his true speed")

# Question 15-16: Using shortcut operators correctly in program
x = 2
y = 3

x += 2
y = x + 1

print(x)
print(y)

x = 5
x += 3
x = x + 1
x = 4

print(x)
# Question 17: Insert code using escape sequence and output
appetizer_price = 4.50
entree_price = 12.0
dessert_price = 6.00
total_price = appetizer_price + entree_price + dessert_price
# Question 18: Insert code using correct variable names and not causing errors
adjective = "red"
noun = "table"
adverb = "quickly"
verb = "run"
animal = "cow"

# print out the madlib
print(f"The {adjective} {noun} sat in the field.")
print(f"A wild {animal} came {adverb} toward it.")
print(f"It began to {verb} around the {noun}.")
print(f"The {adjective} {noun} was not impressed.")
print(f"This is the story of a {adjective} {noun} and a {animal} who could not {verb} away.")

print(f"this is a string")

print("Hello")
print(int("Hello"))

# Unit 3b Exam
# Question 1-2: Vocab Questions (relational operators and conditional operators)
# Question 3-5: Evaluate if, elif, else
"Question 3"
x = 15
y = 10
result = "D"

if x > 15:
    result = "A"
if x == 15 and y <= 10:
    result = "B"
if x < 20 and y == 10:
    result = "C"

print(result)
# Answer: C

"Question 4"
x = 15
y = 10
result = "D"

if x > 15:
    result = "A"
elif x == 15 and y <= 10:
    result = "B"
elif x < 20 and y == 10:
    result = "C"

print(result)
# Answer: B

"Question 5"
a = True
b = False
result = "D"

if a:
    if a and b:
        result = "A"
    else:
        result = "B"
else:
    result = "C"

print(result)
# Answer: B
# Question 6-7: Correct if / elif statements

"Question 6"
# The following program does not output the expected result of "B"
# Instead we get the output of "B \n C \n D"
# Which answer choice explains what the programmer would need to fix such that
# we get the correct result of "B"
grade = 85

if grade >= 90:
    print("A")
if grade >= 80:
    print("B")
if grade >= 70:
    print("C")
if grade >= 60:
    print("D")
else:
    print("F")
# Answer: Change if to elif on lines 190, 192, and 194

"Question 7"
# A customer needs to be at least 65 and have a senior card in order to receive a senior discount
# Currently the program does not output as intended, due to the fact that the customer's age is 60
# Which answer choice best describes the fix the programmer would need to make in order to fix
# the current logic error shown.
age = 60
has_senior_card = True

if age >= 65 or has_senior_card:
    print("You are eligible for a senior discount.")
else:
    print("You are not eligible for a senior discount.")
# Answer: Change the 'or' to 'and'

# Question 8-9: Evaluate Relational Operator

"Question 8"
gold_coins = 95
defeated_boss = True
difficulty = "medium"


if gold_coins >= 95 and defeated_boss:
    if difficulty == "hard":
        print("You are a winner!")
    else:
        print("Try a harder difficulty, bum!")
elif defeated_boss:
    print("Try to get more coins next time")
else:
    print("Better luck next time...")

"Question 9"
# Answer: Try a harder difficulty, bum!
# What is the output of the following program
a = True
b = True
c = False

print(a and b)
print(b or not c)

# Answer: True \n True
# Question 10: Evaluate Relational Operator (AP)
# Question 11: Equivalant Relational Operator (AP)
# Question 12: Syntax Error with if statement

"Quesiton 12"
# The following program segment has a syntax error.
# Which answer shows the syntax error and describes how to fix it.

lvl = 2
if lvl < 2:
    print("You are a white belt")
elif lvl < 3:
    print("You are a blue belt")
else lvl < 4:
    print("You are a purple belt")

# Answer: Line 256, remove the conditional statement
# Question 13-14: Evaluate Random

"Question 13"
# Arpita wants to simulate a program of a 4 segment spinner with equal changes to hit any section
# Which code segment must be inserted into the section # MISSING CODE #
spinner = random.random()
if spinner < 0.25:
    print("Section A!")
elif spinner < 0.5:
    print("Section B!")
elif # MISSING CODE #
    print("Section C!")
else:
    print("Section D!")
# Answer: spinner >= 0.25

"Question 14"
# Which of the following methods can be used to get a random integer?
# A. random.randint()
# B. random.randomint()
# C. random.randinteger()
# D. random.random()
# Answer A
# Question 15: Evaluate Random (randint vs. randrange)
num1 = random.randint(1, 5)
num2 = random.randrange(1, 5)

if num2 == 5 and num1 == 5:
    print("You're a winner!!")

# Question 16: Pick correct math function to complete program

"Question 16"
# Ngoc is writing a program that will output how many pizzas she would need to order
# She knows there are 6 people eating and there are 8 slices to a pizza
# She also knows that each person will want to eat at least 3 slices
# Which function would Ngoc need to use in order to correctly know how many pizzas to order
num_of_ppl = 6
slices_per_za = 8
slices_to_eat_per_ppl = 3

# How many total slices everyone will want to eat
total_slices_to_eat = num_of_ppl * slices_to_eat_per_ppl

# How many pizzas are needed to order
za_to_order = total_slices_to_eat / slices_per_za

# fix how many pizzas are needed to order
# need to round up
za_to_order_fixed = # MISSING CODE #

print(f"You will need to order {za_to_order_fixed} pizzas.")
# Answer: math.ceil()
# Question 17: Finish program with random / math module
# Luke wants to make a program that simulates a game of rock, paper and scissors against the computer
# There are a few code segments that are missing
# Follow the code and the given comments to finish each section
player = input("Rock, Paper or Scissors")
# for the computer Rock = 0, Paper = 1 and Scissors = 2
computer = random.randrange(0,3)
# Checks the logic on if the player typed Rock
if player == "Rock":
    # Computer picks Rock
    if computer == 0:
        print("Its a tie!")
    # Computer picks Paper
    elif computer == 1:
        print("Computer wins!")
    # Computer picks Scissors
    else:
        print("Player wins!")
elif player == "Paper":
    # Computer picks Rock
    if computer == 0:
        print("Player wins!")
    # Computer picks Paper
    elif computer == 1:
        print("Its a tie!")
    # Computer picks Scissors
    else:
        print("Computer wins!")
elif player == "Scissors":
    # Computer picks Rock
    if computer == 0:
        print("Computer wins!")
    # Computer picks Paper
    elif computer == 1:
        print("Player wins!")
    # Computer picks Scissors
    else:
        print("Its a tie!")
else:
    print("That is not an acceptable option, run the program again")

# Question 18: Finish program using boolean expressions

import math

# starting values, need to be identical
side_length = 4
radius = 4

# Calculate the area of a circle, then a square
circle_area = math.pi * radius ** 2
square_area = math.pow(side_length, 2)

# Area of a square will always be larger than a circle
if square_area <= circle_area:
    print("Thats not possible")
# force the areas such that square_area is smaller than circle_area
elif math.floor(square_area) <= math.ceil(circle_area):
    print("Unorthodox approach")
else:
    print("That is more like it")

loop_range = 5
for i in loop_range:
    print(i)




