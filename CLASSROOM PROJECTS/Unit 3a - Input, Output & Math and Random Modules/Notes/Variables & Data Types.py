"""
Variables and Data Types in Python

What is a Variable?

In Python, a **variable** is a named container for storing data. Think of a
variable as a label attached to a box. You can put different types of data,
like numbers or text, inside the box, and you can change its contents at any
time. The name on the label is how you refer to the data inside.

### Correct Variable Naming

To make your code easy to read and understand, it's important to follow
these naming rules:
- Names must start with a letter (a-z, A-Z) or an underscore (_).
- Names cannot start with a number.
- They can only contain letters, numbers, and underscores.
- Names are **case-sensitive**. For example, `age`, `Age`, and `AGE` are
  considered three different variables.
- You can't use Python's reserved keywords (like `print`, `if`, `for`) as
  variable names.

A good practice is to use lowercase with words separated by underscores
This naming convention is referred to as "snake case"
(e.g., `user_name`).

Examples:
"""
first_name = "Alice"
_user_id = 101
total_score = 95.5
correct_answer = True

"""
### Printing a Variable

To see the value stored in a variable, you can use the `print()` function.
You simply place the variable's name inside the parentheses.

Examples:
"""
# Storing a name in a variable, user_name
user_name = "Bob"
# Printing the value of the variable, user_name
print(user_name)

# Storing an age in a variable, age
age = 25
# Printing the value of the variable, age
print(age)

# Combining text and a variable in a print statement
# This is referred to as an f-string
print(f"Hello, my name is {user_name}")
print(f"I am {age} years old.")

"""
--------------------------------------------------------------------------------

What are Data Types?

Every piece of data has a **data type**, which tells Python what kind of
data it is. Python automatically figures out the data type of a variable
when you assign a value to it.

The most common data types you'll work with are:

- **String (`str`):** Used for storing **text**. A string is a sequence of
  characters enclosed in either single (`' '`) or double (`" "`) quotes.

  Examples:
"""
student_name = "Charlie"
school = 'Central High School'
welcome_message = "Hello, world!"

"""
- **Integer (`int`)::** A **whole number**, positive or negative, with no
  decimal point. Integers are used for counting.

  Examples:
"""
age = 25
number_of_students = 30
year = 2023

"""
- **Float (`float`):** A number that has a **decimal point**. Floats are
  used for measurements or values that need a fractional part.

  Examples:
"""
price = 19.99
pi_value = 3.14159
temperature = -5.5

"""
- **Boolean (`bool`):** A value that stores True or False for a **conditional statement**.
    These will be used later for if statements in Unit 3b.
    True and False ** Must ** be capitalized, otherwise you will get an error

  Examples:
"""
is_valid = True
is_running = False
a = True