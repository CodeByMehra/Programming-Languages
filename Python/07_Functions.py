# -------------------------------------------
# 🟦 PYTHON FUNCTIONS AND RECURSION - NOTES
# -------------------------------------------

# ✅ WHAT IS A FUNCTION?
# A function is a reusable block of code that performs a specific task.
# It helps in modular programming and avoids code repetition.

# -------------------------------------------
# ✅ DEFINING AND CALLING FUNCTIONS
# -------------------------------------------
# Syntax:
# def function_name(parameters):
#     block of code

def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()

# --- Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")   # Output: Hello, Alice!

# --- Function with return value
def add(x, y):
    return x + y

result = add(5, 3)
print(result)         # Output: 8

# -------------------------------------------
# ✅ TYPES OF FUNCTION PARAMETERS
# -------------------------------------------

# 1. Required Arguments
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Bob")  # Must pass an argument

# 2. Default Arguments
def greet(name="Guest"):
    print(f"Hi, {name}")

greet()               # Output: Hi, Guest
greet("Sara")         # Output: Hi, Sara

# 3. Keyword Arguments
def profile(name, age):
    print(f"Name: {name}, Age: {age}")

profile(age=25, name="Tom")

# 4. Variable Length Arguments
# *args → Non-keyword variable-length arguments (tuple)
def total_marks(*marks):
    return sum(marks)

print(total_marks(70, 85, 90))  # Output: 245

# **kwargs → Keyword variable-length arguments (dict)
def student_info(**info):
    print(info)

student_info(name="John", age=20)

# -------------------------------------------
# ✅ SCOPE OF VARIABLES
# -------------------------------------------

# Local Variable → Defined inside a function
# Global Variable → Defined outside all functions

x = 10  # Global

def show():
    x = 5  # Local
    print("Inside function:", x)

show()
print("Outside function:", x)

# To use global variable inside function
def modify():
    global x
    x = 20

modify()
print("Modified global x:", x)  # Output: 20

# -------------------------------------------
# ✅ LAMBDA (ANONYMOUS) FUNCTION
# -------------------------------------------
# A one-line function with no name

square = lambda x: x * x
print(square(5))  # Output: 25

# Multiple arguments
add = lambda a, b: a + b
print(add(3, 4))   # Output: 7

# -------------------------------------------
# ✅ RECURSION IN PYTHON
# -------------------------------------------
# A function calling itself is known as recursion.
# Every recursive function must have a **base case**.

# --- Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:        # Base Case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive Case

print(factorial(5))  # Output: 120

# --- Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8

# -------------------------------------------
# ✅ ADVANTAGES OF FUNCTIONS
# -------------------------------------------
# - Reusability of code
# - Improved readability
# - Easier debugging
# - Makes code modular and organized

# ✅ ADVANTAGES OF RECURSION
# -------------------------------------------
# - Useful for problems like tree traversal, factorial, fibonacci, etc.
# - Reduces code complexity for divide-and-conquer algorithms

# ⚠️ Disadvantages of Recursion:
# - Can be slower than loops
# - High memory usage due to function call stack
# - Risk of infinite recursion without base case

# -------------------------------------------
# ✅ SUMMARY
# -------------------------------------------
# 🔹 Use functions to avoid code repetition
# 🔹 Use recursion for problems that break into sub-problems
# 🔹 Always include a base case in recursion
# 🔹 Use *args and **kwargs for flexible parameters
