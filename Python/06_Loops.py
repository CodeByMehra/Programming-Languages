# -------------------------------------------
# 🟦 PYTHON LOOPS - DETAILED NOTES
# -------------------------------------------

# ✅ What are Loops?
# Loops are used to repeat a block of code multiple times.
# Python has two types of loops: for and while.

# -------------------------------------------
# ✅ FOR LOOP
# -------------------------------------------
# Used to iterate over a sequence (like list, tuple, string, or range)

# --- Using range()
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# --- Custom range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # Output: 1 3 5 7 9

# --- Iterating over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# --- Iterating over a string
for char in "hello":
    print(char)

# --- Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# -------------------------------------------
# ✅ WHILE LOOP
# -------------------------------------------
# Repeats as long as the condition is True.

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# --- Infinite Loop (be careful!)
# while True:
#     print("This runs forever unless you break it")

# -------------------------------------------
# ✅ BREAK STATEMENT
# -------------------------------------------
# Used to exit the loop immediately.

for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0 1 2 3 4

# -------------------------------------------
# ✅ CONTINUE STATEMENT
# -------------------------------------------
# Skips the current iteration and goes to the next one.

for i in range(6):
    if i == 3:
        continue
    print(i)  # Output: 0 1 2 4 5

# -------------------------------------------
# ✅ ELSE with LOOPS
# -------------------------------------------
# The else part runs only if the loop finishes normally (not via break).

for i in range(5):
    print(i)
else:
    print("Loop finished successfully")

# If break is used, else will not run:
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This would not print")

# -------------------------------------------
# ✅ LOOPING with ENUMERATE()
# -------------------------------------------
# Returns index and value when looping through a list.

names = ["John", "Sara", "Mike"]
for index, name in enumerate(names):
    print(index, name)

# -------------------------------------------
# ✅ LOOPING with ZIP()
# -------------------------------------------
# Used to loop over two or more sequences simultaneously.

subjects = ["Math", "Physics", "Chemistry"]
marks = [90, 85, 95]

for sub, mark in zip(subjects, marks):
    print(f"{sub}: {mark}")

# -------------------------------------------
# ✅ LIST COMPREHENSION (Loop in One Line)
# -------------------------------------------
# Creates a new list by applying a loop and condition.

squares = [x*x for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

even_nums = [x for x in range(10) if x % 2 == 0]
print(even_nums)  # Output: [0, 2, 4, 6, 8]

# -------------------------------------------
# ✅ Best Practices
# -------------------------------------------
# - Use for loops when iterating over sequences
# - Use while loops when you don’t know how many times to loop
# - Always make sure loops have a condition that ends them
# - Avoid deeply nested loops; use functions or logic separation
# - Use `enumerate()` or `zip()` for cleaner multi-list loops

# -------------------------------------------
# ✅ Summary
# -------------------------------------------
# 🔁 for → loops over a known sequence
# 🔁 while → loops until a condition becomes False
# 🔁 break → exits the loop
# 🔁 continue → skips current iteration
# 🔁 else → executes when loop ends normally
# 🔁 list comprehension → for-loop in one line
