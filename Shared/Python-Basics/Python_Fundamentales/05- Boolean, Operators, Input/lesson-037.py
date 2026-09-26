# --------------------------------
# -- Lesson 037: Type Conversion --
# --------------------------------

# Type Conversion means converting data from one data type to another.
# Common conversion functions:
# str()
# tuple()
# list()
# set()
# dict()


# ==================================
# 1. Convert To String => str()
# ==================================

a = 10

print(type(a))
# Output:
# <class 'int'>

print(type(str(a)))
# Output:
# <class 'str'>


a = 10.0

print(type(a))
# Output:
# <class 'float'>

print(type(str(a)))
# Output:
# <class 'str'>


# str() can convert values such as integers and floats into strings.


# ==================================
# 2. Convert To Tuple => tuple()
# ==================================

c = "Osama"              # String
d = [1, 2, 3, 4, 5]     # List
e = {"A", "B", "C"}      # Set
f = {"A": 1, "B": 2}     # Dictionary

print(tuple(c))
# Output:
# ('O', 's', 'a', 'm', 'a')

print(tuple(d))
# Output:
# (1, 2, 3, 4, 5)

print(tuple(e))
# Output may be:
# ('A', 'B', 'C')
# Set order is not guaranteed.

print(tuple(f))
# Output:
# ('A', 'B')

# Important:
# Converting a dictionary to tuple() returns the KEYS only.


# ==================================
# 3. Convert To List => list()
# ==================================

c = "Osama"              # String
d = (1, 2, 3, 4, 5)     # Tuple
e = {"A", "B", "C"}      # Set
f = {"A": 1, "B": 2}     # Dictionary

print(list(c))
# Output:
# ['O', 's', 'a', 'm', 'a']

print(list(d))
# Output:
# [1, 2, 3, 4, 5]

print(list(e))
# Output may be:
# ['A', 'B', 'C']
# Set order is not guaranteed.

print(list(f))
# Output:
# ['A', 'B']

# Important:
# Converting a dictionary to list() returns the KEYS only.


# ==================================
# 4. Convert To Set => set()
# ==================================

c = "Osama"              # String
d = (1, 2, 3, 4, 5)     # Tuple
e = ["A", "B", "C"]      # List
f = {"A": 1, "B": 2}     # Dictionary

print(set(c))
# Output may be:
# {'O', 's', 'a', 'm'}
#
# Notice:
# The repeated "a" appears only once because sets do not allow duplicates.

print(set(d))
# Output:
# {1, 2, 3, 4, 5}

print(set(e))
# Output may be:
# {'A', 'B', 'C'}

print(set(f))
# Output:
# {'A', 'B'}

# Important:
# - Sets remove duplicate values.
# - Sets are unordered.
# - Converting a dictionary to set() returns the KEYS only.


# ==================================
# 5. Convert To Dictionary => dict()
# ==================================

# dict() is different from the previous conversions.
# Python needs each element to contain TWO values:
#
# Key + Value


# ----------------------------------
# Wrong Example 1: String
# ----------------------------------

c = "Osama"

# print(dict(c))

# Error:
# ValueError

# Why?
# Python receives individual characters:
# O
# s
# a
# m
# a
#
# But a dictionary needs pairs:
# Key + Value


# ----------------------------------
# Wrong Example 2: Normal Tuple
# ----------------------------------

d = (1, 2, 3, 4, 5)

# print(dict(d))

# Error:
# TypeError

# Why?
# Each item is only one value.
# Python cannot determine:
#
# Key -> Value


# ----------------------------------
# Correct Tuple Conversion
# ----------------------------------

d = (("A", 1), ("B", 2), ("C", 3))

print(dict(d))

# Output:
# {'A': 1, 'B': 2, 'C': 3}

# Each inner tuple contains exactly TWO elements:
#
# ("A", 1)
#   |    |
#  Key  Value


# ----------------------------------
# Correct List Conversion
# ----------------------------------

e = [["One", 1], ["Two", 2], ["Three", 3]]

print(dict(e))

# Output:
# {'One': 1, 'Two': 2, 'Three': 3}

# Again, every inner list contains:
#
# [Key, Value]


# ----------------------------------
# Wrong Example: Simple List
# ----------------------------------

e = ["A", "B", "C"]

# print(dict(e))

# Error:
# ValueError

# Because each element does not provide a Key + Value pair.


# ----------------------------------
# Set Problem
# ----------------------------------

f = {"A", "B"}

# print(dict(f))

# Error:
# ValueError

# Why?
# "A" and "B" are individual values.
# They are NOT Key + Value pairs.


# ----------------------------------
# Important Set Limitation
# ----------------------------------

# You might think about doing this:

# f = {{"A", 1}, {"B", 2}}

# But this gives an error:
#
# TypeError: unhashable type: 'set'

# Because a set cannot contain another normal set.
# Sets are mutable and therefore cannot be elements inside another set.


# ==================================
# Quick Summary
# ==================================

# str()   -> Convert value to String
# tuple() -> Convert iterable to Tuple
# list()  -> Convert iterable to List
# set()   -> Convert iterable to Set
# dict()  -> Needs Key + Value pairs


# Dictionary conversion examples:

# This works:
# (("A", 1), ("B", 2))
#       ↓
# {"A": 1, "B": 2}

# This also works:
# [["A", 1], ["B", 2]]
#       ↓
# {"A": 1, "B": 2}

# This does NOT work:
# ("A", "B", "C")
#
# because dict() needs every element to provide:
#
# Key + Value


# ==================================
# Most Important Points
# ==================================

# Dictionary -> list / tuple / set
# returns dictionary KEYS by default.

# set()
# removes duplicates and does not guarantee order.

# dict()
# requires every input element to contain exactly:
# TWO elements => Key + Value

# Example:
# ("Name", "Bishoy")
#    Key      Value