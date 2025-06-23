# -------------------------------------------
# 🟦 PYTHON DICTIONARIES AND SETS - NOTES
# -------------------------------------------

# ✅ DICTIONARIES IN PYTHON
# A dictionary is an unordered, mutable collection of key-value pairs.
# Keys must be unique and immutable (like strings, numbers, or tuples).
# Syntax: {key: value}

# --- Creating a Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "country": "India"
}

# --- Accessing Values
print(person["name"])          # Output: Alice
print(person.get("age"))       # Output: 25
print(person.get("gender", "N/A"))  # Returns 'N/A' if key not found

# --- Modifying and Adding
person["age"] = 26             # Modify value
person["email"] = "a@x.com"    # Add new key-value pair

# --- Removing Elements
person.pop("country")          # Removes specified key
person.popitem()               # Removes the last inserted item
del person["name"]             # Deletes key 'name'

# --- Dictionary Methods
keys = person.keys()           # Returns a list of keys
values = person.values()       # Returns a list of values
items = person.items()         # Returns a list of (key, value) tuples
person.clear()                 # Removes all items from dictionary

# --- Looping through a Dictionary
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key} => {value}")

# --- Nested Dictionary
students = {
    "101": {"name": "John", "age": 20},
    "102": {"name": "Sara", "age": 21}
}
print(students["102"]["name"])  # Output: Sara

# --- Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1:1, 2:4, 3:9, 4:16, 5:25}

# -------------------------------------------
# 🟩 SETS IN PYTHON
# -------------------------------------------
# A Set is an unordered collection of unique items.
# Sets are mutable but only store immutable (hashable) elements.

# --- Creating a Set
fruits = {"apple", "banana", "mango"}
empty_set = set()      # NOT {} → that creates an empty dictionary

# --- Adding and Removing Elements
fruits.add("orange")
fruits.update(["grape", "apple"])  # Adds multiple items (ignores duplicates)
fruits.remove("banana")       # Removes item, raises error if not found
fruits.discard("pear")        # Removes item if exists, no error if not found
fruits.pop()                  # Removes a random item
fruits.clear()                # Clears the set

# --- Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))        # {1, 2, 3, 4, 5, 6}
print(A.intersection(B)) # {3, 4}
print(A.difference(B))   # {1, 2}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}

# --- Set Comparison
print(A.issubset(B))     # False
print(A.issuperset(B))   # False
print(A.isdisjoint(B))   # False (they have 3,4 in common)

# --- Set Comprehension
even_squares = {x*x for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # Output: {4, 16, 36, 64, 100}

# -------------------------------------------
# ✅ DIFFERENCES BETWEEN DICTIONARY AND SET
# -------------------------------------------
# | Feature       | Dictionary                 | Set                     |
# |---------------|----------------------------|--------------------------|
# | Structure     | Key-value pairs            | Only values (unique)     |
# | Mutable       | Yes                        | Yes                      |
# | Syntax        | {"key": "value"}           | {"value1", "value2"}     |
# | Indexing      | No indexing                | No indexing              |
# | Use Case      | When data has relationships| When uniqueness matters  |
# | Duplicate     | Keys are unique            | All elements are unique  |

# -------------------------------------------
# ✅ When to Use Dictionary vs Set?
# -------------------------------------------
# - Use a Dictionary when: You want to associate keys with values.
# - Use a Set when: You need to store unique items and perform set operations.

