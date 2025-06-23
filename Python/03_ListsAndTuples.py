# -------------------------------------------
# 🟦 PYTHON LISTS AND TUPLES - DETAILED NOTES
# -------------------------------------------

# ✅ LISTS IN PYTHON
# A List is a mutable (changeable), ordered collection of items.
# Lists can hold items of different data types.

# --- Creating a List
my_list = [10, 20, 30, 40]
mixed_list = [1, "hello", 3.14, True]

# --- Accessing Elements
print(my_list[0])     # Output: 10
print(my_list[-1])    # Output: 40 (last element)

# --- Modifying Elements
my_list[1] = 25
print(my_list)        # Output: [10, 25, 30, 40]

# --- List Methods
my_list.append(50)         # Adds element at the end
my_list.insert(2, 100)     # Inserts 100 at index 2
my_list.remove(25)         # Removes first occurrence of 25
my_list.pop()              # Removes and returns last item
my_list.sort()             # Sorts the list in ascending order
my_list.reverse()          # Reverses the list
my_list.clear()            # Removes all items from the list

# --- List Functions
length = len(my_list)      # Returns number of elements
maximum = max([5, 2, 9])   # Returns max value (9)
minimum = min([5, 2, 9])   # Returns min value (2)
total = sum([5, 2, 9])     # Returns sum (16)

# --- List Slicing
nums = [10, 20, 30, 40, 50]
print(nums[1:4])      # Output: [20, 30, 40]
print(nums[:3])       # Output: [10, 20, 30]
print(nums[::2])      # Output: [10, 30, 50]

# --- List Comprehension
squares = [x**2 for x in range(1, 6)]  # Output: [1, 4, 9, 16, 25]

# -------------------------------------
# 🟩 TUPLES IN PYTHON
# -------------------------------------
# A Tuple is an immutable (unchangeable), ordered collection of items.
# Tuples are faster than lists and used when data should not change.

# --- Creating a Tuple
my_tuple = (10, 20, 30)
single_item = (5,)     # Comma is required for single-element tuple

# --- Accessing Elements
print(my_tuple[1])     # Output: 20

# --- Tuple Methods
count = my_tuple.count(10)    # Counts number of times 10 appears
index = my_tuple.index(30)    # Returns index of 30

# --- Immutability
# my_tuple[0] = 100  ❌ This will raise an error (tuples can't be changed)

# --- Tuple Packing and Unpacking
person = ("Alice", 25, "India")
name, age, country = person
print(name)     # Output: Alice
print(age)      # Output: 25

# --- Use Cases
# Tuples are often used to:
# ✅ Protect data (read-only)
# ✅ Return multiple values from a function
# ✅ Use as dictionary keys (since they are hashable)

# -------------------------------------
# ✅ DIFFERENCES BETWEEN LIST AND TUPLE
# -------------------------------------
# | Feature          | List               | Tuple              |
# |------------------|--------------------|---------------------|
# | Mutability       | Mutable            | Immutable           |
# | Syntax           | [1, 2, 3]          | (1, 2, 3)           |
# | Performance      | Slower             | Faster              |
# | Use Cases        | Dynamic data       | Fixed data          |
# | Methods Available| More methods       | Fewer methods       |

# -------------------------------------
# ✅ When to use List vs Tuple?
# -------------------------------------
# - Use List when: You need to modify, append, or delete data.
# - Use Tuple when: Your data should remain constant or you want performance.
