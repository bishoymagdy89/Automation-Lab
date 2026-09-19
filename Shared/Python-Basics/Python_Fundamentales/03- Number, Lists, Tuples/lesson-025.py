# ==========================================
# Tuple - Part 2
# ==========================================


# ------------------------------------------
# [1] Tuple With One Element
# ------------------------------------------

# To create a tuple with ONE item,
# you must add a comma (,).
# The comma is what makes it a Tuple, not the parentheses.

myTuple1 = ("Osama",)
myTuple2 = "Osama",

print(myTuple1)
print(myTuple2)

print(type(myTuple1))   # <class 'tuple'>
print(type(myTuple2))   # <class 'tuple'>

print(len(myTuple1))    # 1
print(len(myTuple2))    # 1


# ------------------------------------------
# [2] Tuple Concatenation
# ------------------------------------------

# + joins Tuples together and creates a new Tuple.

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
# (1, 2, 3, 4, 5, 6)

print(d)
# (1, 2, 3, 4, "A", "B", True, 5, 6)


# ------------------------------------------
# [3] Tuple, List, String Repeat (*)
# ------------------------------------------

# * repeats the content multiple times.

myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
# OsamaOsamaOsamaOsamaOsamaOsama

print(myList * 6)
# [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

print(myTuple * 6)
# ("A", "B", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B")


# ------------------------------------------
# [4] Tuple Method => count()
# ------------------------------------------

# count(value)
# Returns how many times a value exists in the Tuple.

a = (1, 3, 7, 8, 2, 6, 5, 8)

print(a.count(8))
# 2


# ------------------------------------------
# [5] Tuple Method => index()
# ------------------------------------------

# index(value)
# Returns the Index position of the value.
# Remember: Index starts from 0.

b = (1, 3, 7, 8, 2, 6, 5)

# Value:  1  3  7  8  2  6  5
# Index:  0  1  2  3  4  5  6

print(b.index(7))
# 2


# ------------------------------------------
# [6] Printing index() With Text
# ------------------------------------------

# This causes an Error:
#
# print("The Position of Index Is: " + b.index(7))
#
# Because:
# "The Position..." = String
# b.index(7)        = Integer
#
# Python cannot concatenate String + Integer directly.


# Method 1 => format()

print("The Position of Index Is: {:d}".format(b.index(7)))

# Output:
# The Position of Index Is: 2


# Method 2 => f-string
# Easier and commonly used.

print(f"The Position of Index Is: {b.index(7)}")

# Output:
# The Position of Index Is: 2


# ------------------------------------------
# [7] Tuple Destruct / Tuple Unpacking
# ------------------------------------------

# We can take Tuple values and assign them
# to separate variables.

a = ("A", "B", "C")

x, y, z = a

# Python assigns them in order:
#
# "A" -> x
# "B" -> y
# "C" -> z

print(x)   # A
print(y)   # B
print(z)   # C


# ------------------------------------------
# [8] Ignore A Value While Unpacking
# ------------------------------------------

a = ("A", "B", 4, "C")

x, y, _, z = a

# The underscore _ means:
# "I don't need this value."
#
# "A" -> x
# "B" -> y
#  4  -> _   (Ignored)
# "C" -> z

print(x)   # A
print(y)   # B
print(z)   # C


# ==========================================
# QUICK SUMMARY
# ==========================================

# ("A",)        => Tuple with one item
#
# tuple1 + tuple2
#                => Concatenation
#
# tuple * 3
#                => Repeat
#
# .count(value)
#                => How many times does the value exist?
#
# .index(value)
#                => Where is the value?
#
# x, y, z = tuple
#                => Tuple Unpacking
#
# x, _, z = tuple
#                => Ignore a value while unpacking
#
# Tuple is Immutable:
# You can read/access its values,
# but you cannot change, add, or delete its items.
# ==========================================