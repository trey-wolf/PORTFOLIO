"""
Challenge Problems 10/16

Before you have a heart attack, pick TWO challenge problems and complete them.
It does not matter which two you pick out of complexity.
If you want to do more (or all of them) that is your decision.

If you want the two that I think are the easiest to do -> Multiplication Table / Temperature Conversion Table

Easy
    Simple Interest Growth: Ask for a principal amount, interest rate, and number of years. Use a for loop to show how the investment grows year by year over 30 years.
    Multiplication Table: Ask the user for a number and print its multiplication table from 1 to 12.
    Random Shapes Drawer (with Turtle): Use a for loop to run 6 times. In each iteration, pick a random number of sides (3-8) and a random color, then use another for loop to draw that shape in a random location.
    Temperature Conversion Table: Ask the user for a starting temperature in Celsius. Use a for loop to print a conversion table to Fahrenheit for the next 10 degrees. (Formula: F = C * 9/5 + 32).

Medium
    Rock, Paper, Scissors: Play a "best of 5" game against the computer. The for loop runs 5 times. The computer makes a random choice, the user makes a choice, and an if/elif/else structure determines the winner of each round.
    Fantasy Character Stat Roller: In many role-playing games, a character's stats are created by rolling three 6-sided dice. Use a for loop to generate 6 different stats for a character.
    Tip Calculator Table: Ask for the total amount of a restaurant bill. Use a for loop to display the total bill amount with a 15%, 18%, 20%, and 23% tip.

Some of these are rather open-ended, go as in detail as you want.
These are due at the end of class.
"""
a = 0
b = 1
for n in range(1, 4):
    a += n
    b *= n
print(a + b)

# Question 11
def sayStuff():
    print("What")
    print("In")

print("The")
sayStuff()
print("World")

# Question 12
def go(x):
    x = 16
    print(x)

x = 8
go(x)

# Question 13
def go(x):
    x = 16

x = 8
go(x)

print(x)

# Question 14
def getChange(cost, paid):
    # MISSING CODE #

getChange(5.00, 2.00)

# Question 15
def triplet(word):
    print(word * 3)

triplet("pass")

# Question 16
def buyCar(make, model, year):
    message = f"Congratulations on buying a {year} {make} {model}"
    if year < 1970:
        message = f"Congratulations on buying a classic {make} {model}"

    return message

print(buyCar("Chevrolet", "Camaro", 1969))
print(buyCar("Chevrolet", "Bolt", 2024))

# Question 17
def function1():
    print("Happy")
    print("Birthday")

def function2():
    function1()
    print("to")

print("You")
function2()

# Question 18
def calculate(num1, num2):
    print(num1)
    return(num1)
    print(num2)

statement = calculate(10, 20)
print(statement)

number = 1
total = 0

while number <= 4:
    number += 1
    if total >= 10:
        continue
    total += number
print(total)