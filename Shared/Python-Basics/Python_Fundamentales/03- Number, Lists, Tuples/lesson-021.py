# ---------------------------------
# -- Lists --
# ---------------------------------

# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# ---------------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)
# ['One', 'Two', 'One', 1, 100.5, True]


# ---------------------------------
# Access List Items With Index
# ---------------------------------

print(myAwesomeList[1])
# Two

print(myAwesomeList[-1])
# True

print(myAwesomeList[-3])
# 1


# ---------------------------------
# List Slicing
# ---------------------------------

print(myAwesomeList[1:4])
# ['Two', 'One', 1]

print(myAwesomeList[:4])
# ['One', 'Two', 'One', 1]

print(myAwesomeList[1:])
# ['Two', 'One', 1, 100.5, True]


# ---------------------------------
# Slicing With Steps
# ---------------------------------

print(myAwesomeList[::1])
# ['One', 'Two', 'One', 1, 100.5, True]

print(myAwesomeList[::2])
# ['One', 'One', 100.5]


# ---------------------------------
# Index Out Of Range
# ---------------------------------

# print(myAwesomeList[150])
# IndexError: list index out of range


# ---------------------------------
# Modify List Items
# ---------------------------------

print(myAwesomeList)

myAwesomeList[1] = 2
myAwesomeList[-1] = False

print(myAwesomeList)
# ['One', 2, 'One', 1, 100.5, False]


# ---------------------------------
# Delete Items Using Slicing
# ---------------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

myAwesomeList[0:3] = []

print(myAwesomeList)
# [1, 100.5, True]


# ---------------------------------
# Replace Multiple Items
# ---------------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

myAwesomeList[0:3] = ["A", "B", "C"]

print(myAwesomeList)
# ['A', 'B', 'C', 1, 100.5, True]


# ---------------------------------
# Replace Multiple Items With One
# ---------------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

myAwesomeList[0:3] = ["A"]

print(myAwesomeList)
# ['A', 1, 100.5, True]