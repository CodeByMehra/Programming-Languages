# Here are the important points about the strings

#Strings are immutable means these cannot be changed

# Slicing of strings:- 

name = "Vishal Mehra"
print(len(name))  # to get the length of string

# slice = name[index_start:index_end] - Slicing syntax 

shortname= name[7:12] #From 7 to 12 excluding 12
print(shortname)

# Slicing with skip value:-

# strname[index_start:index_end:skip value] - skip Slicing syntax 

string= "0123456789"
print(string[0:8:2])

#String functions:-
# sr  function          Syntax            example
# 1.   length       len(stringName)      len(name)
# 2.  endswith                           name.startswith("ra")
# 3.  startswith                         name.endswith("Vi")  -will give true or false (case sensitive)
# 3. lower()
# Converts all uppercase characters in a string to lowercase.
text = "HELLO"
print(text.lower())  # Output: hello

# 4. upper()
# Converts all lowercase characters in a string to uppercase.
text = "hello"
print(text.upper())  # Output: HELLO

# 5. strip()
# Removes leading and trailing whitespaces from the string.
text = "  hello  "
print(text.strip())  # Output: "hello"

# 6. replace()
# Replaces a substring with another substring.
text = "Hello World"
print(text.replace("World", "Python"))  # Output: Hello Python

# 7. find()
# Returns the index of the first occurrence of the substring. Returns -1 if not found.
text = "Learn Python"
print(text.find("Python"))  # Output: 6

# 8. count()
# Returns the number of times a substring appears in the string.
text = "banana"
print(text.count("a"))  # Output: 3

# 9. split()
# Splits the string into a list using the specified separator.
text = "apple,banana,mango"
print(text.split(","))  # Output: ['apple', 'banana', 'mango']

# 10. join()
# Joins a list of strings into a single string using the specified separator.
fruits = ["apple", "banana", "mango"]
print(",".join(fruits))  # Output: apple,banana,mango

# 11. isalpha()
# Returns True if all characters in the string are alphabets (no spaces or numbers).
text = "Python"
print(text.isalpha())  # Output: True

# 12. isnumeric()
# Returns True if all characters in the string are numeric.
text = "12345"
print(text.isnumeric())  # Output: True
