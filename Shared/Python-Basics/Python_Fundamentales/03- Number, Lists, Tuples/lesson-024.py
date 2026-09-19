# ---------------------------------
# -- Tuple and Methods Part One --
# ---------------------------------

# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuples Are Ordered => You Can Use Index To Access Items
# [4] Tuples Are Immutable => You Can't Add, Delete, or Edit Items
# [5] Tuple Items Are Not Unique => Duplicate Values Are Allowed
# [6] Tuples Can Have Different Data Types
# [7] Operators Used With Strings and Lists Are Available With Tuples

# ---------------------------------
# Tuple Syntax & Type Test
# ---------------------------------

myAwesomeTupleOne = ("Osama", "Ahmed")
myAwesomeTupleTwo = "Osama", "Ahmed"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# Output:
# ('Osama', 'Ahmed')
# ('Osama', 'Ahmed')
# <class 'tuple'>
# <class 'tuple'>


# ---------------------------------
# Tuple Indexing
# ---------------------------------

myAwesomeTupleThree = (1, 2, 3, 4, 5)

print(myAwesomeTupleThree[0])   # 1
print(myAwesomeTupleThree[-1])  # 5
print(myAwesomeTupleThree[-3])  # 3


# ---------------------------------
# Tuple Assign Values
# ---------------------------------

myAwesomeTupleFour = (1, 2, 3, 4, 5)

# The following line will cause an error because Tuple is Immutable:
# myAwesomeTupleFour[2] = "Three"

print(myAwesomeTupleFour)

# Error if we try to modify it:
# TypeError: 'tuple' object does not support item assignment


# ---------------------------------
# Tuple Items
# ---------------------------------

myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)

# Tuple can contain duplicate values
print(myAwesomeTupleFive[1])   # Osama

# Tuple can contain different data types
print(myAwesomeTupleFive[-1])  # True