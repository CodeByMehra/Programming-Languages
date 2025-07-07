# -------------------------------------------
# 🟦 PYTHON CONDITIONAL STATEMENTS - NOTES
# -------------------------------------------

# ✅ What are Conditionals?
# Conditional statements control the flow of your program.
# They allow the program to take decisions based on conditions (True/False).

# -------------------------------------------
# ✅ if Statement
# -------------------------------------------
# Executes a block of code if a condition is True.

age = 18

if age >= 18:
    print("You are eligible to vote.")

# -------------------------------------------
# ✅ if-else Statement
# -------------------------------------------
# Executes one block if condition is True, another if False.

marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# -------------------------------------------
# ✅ if-elif-else Statement
# -------------------------------------------
# Used to check multiple conditions one by one.

score = 85

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Grade F")

# -------------------------------------------
# ✅ Nested if Statement
# -------------------------------------------
# An if inside another if. Useful for multi-level decisions.

num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not Positive")

# -------------------------------------------
# ✅ Short Hand (Ternary) if-else
# -------------------------------------------
# For simple conditions in one line.

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# -------------------------------------------
# ✅ Logical Operators in Conditionals
# -------------------------------------------
# and  → All conditions must be True
# or   → At least one condition is True
# not  → Reverses the boolean value

x = 10
y = 5

# Using 'and'
if x > 5 and y < 10:
    print("Both conditions are true")

# Using 'or'
if x > 15 or y < 10:
    print("At least one condition is true")

# Using 'not'
if not x < 5:
    print("x is NOT less than 5")

# -------------------------------------------
# ✅ Comparison Operators in Conditionals
# -------------------------------------------
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to

a = 7
b = 3

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True

# -------------------------------------------
# ✅ Membership and Identity in Conditionals
# -------------------------------------------
# Membership Operators: in, not in
# Identity Operators: is, is not

fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")

if "mango" not in fruits:
    print("Mango is not in the list")

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True (same memory)
print(x is z)      # False (different memory)
print(x == z)      # True (same values)

# -------------------------------------------
# ✅ Best Practices
# -------------------------------------------
# - Always use proper indentation (4 spaces)
# - Avoid deeply nested ifs; use elif or combine conditions
# - Keep conditions simple and readable

# -------------------------------------------
# ✅ Summary
# -------------------------------------------
# if, elif, and else are used to control program flow.
# Combine with logical and comparison operators for powerful decision-making.
# Practice writing clean and readable conditionals.

