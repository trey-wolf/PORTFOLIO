# Day 2: Else-If (elif) & Boolean Operators
# The 'elif' statement allows you to check for multiple conditions sequentially.
# It is a shortcut for "else if".

# Boolean operators are used to combine or modify boolean expressions.
# 'and': returns True if BOTH conditions are true.
# 'or': returns True if AT LEAST ONE condition is true.
# 'not': reverses the boolean value. True -> False // False -> True

# Example 1: Grading a score with elif and a boolean operator
score = 85
has_extra_credit = True

if score >= 90 and has_extra_credit:
    print("You got an A+! Amazing.")
elif score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
else:
    print("You need to study more.")

# Example 2: Using 'or' and 'not'
is_sunny = False
is_cold = True

if not is_sunny or is_cold:
    print("You should bring a jacket.")

# Example 3: Using 'and'
is_sunny = False
is_cold = True
if is_sunny and is_cold:
    print("You might need a jacket.")