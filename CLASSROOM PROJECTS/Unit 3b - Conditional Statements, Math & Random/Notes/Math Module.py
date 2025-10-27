# Day 4: The Math Module
# A module is a collection of pre-written functions and code.
# The 'math' module provides access to many useful mathematical functions.
# To use a module, you must 'import' it first.

# The Math Module: Key Functions for AP CSP

# You must import the math module to use its functions.
import math

# --- 1. math.sqrt() ---
# Returns the square root of a number.
num_sqrt = 64
result_sqrt = math.sqrt(num_sqrt)
print(f"The square root of {num_sqrt} is {result_sqrt}.")

# --- 2. math.pow() ---
# Returns the value of x raised to the power of y.
base = 2
power = 5
result_pow = math.pow(base, power)
print(f"{base} to the power of {power} is {result_pow}.")

# --- 3. math.floor() ---
# Rounds a number down to the nearest integer.
num_floor = 7.9
result_floor = math.floor(num_floor)
print(f"The floor of {num_floor} is {result_floor}.")

# --- 4. math.ceil() ---
# Rounds a number up to the nearest integer.
num_ceil = 7.1
result_ceil = math.ceil(num_ceil)
print(f"The ceiling of {num_ceil} is {result_ceil}.")

# --- 5. math.gcd() ---
# Returns the greatest common divisor of two integers.
num1_gcd = 48
num2_gcd = 18
result_gcd = math.gcd(num1_gcd, num2_gcd)
print(f"The greatest common divisor of {num1_gcd} and {num2_gcd} is {result_gcd}.")

# --- 6. math.pi ---
# A constant representing the value of pi.
radius = 5
circumference = 2 * math.pi * radius
print(f"The circumference of a circle with a radius of {radius} is {circumference:.2f}.")

print("aksdnfi \is\"")