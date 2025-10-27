"""
You could simplify this by doing the following
if grade_level == "ap":
    ...
elif grade_level == "honors":
    ...
else:
    ...
"""
grade_level = input("What level course? (level, honors, ap)")
if grade_level == "level":
    minor_weight = 0.4
    major_weight = 0.6
elif grade_level == "honors":
    minor_weight = 0.35
    major_weight = 0.65
elif grade_level == "ap":
    minor_weight = 0.3
    major_weight = 0.7
else:
    minor_weight = 0.4
    major_weight = 0.6

# average for each type of assignments
minor_average = float(input("Type in your minor assignment average: "))
major_average = float(input("Type in your major assignment average: "))

# total weighted average with the assignment weights
total_average = (minor_average * minor_weight) + (major_average * major_weight)

print(f"Your average score is: {total_average}")