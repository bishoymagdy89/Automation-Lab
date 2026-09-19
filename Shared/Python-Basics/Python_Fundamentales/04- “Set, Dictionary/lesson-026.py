# ==========================================================
# Lesson 026 - Set
# ==========================================================

# ----------------------------------------------------------
# What is a Set?
# ----------------------------------------------------------

# Set is a collection of items.
#
# [1] Set Items Are Enclosed in Curly Braces {}
#
# [2] Set Items Are Not Ordered And Not Indexed
#
# [3] Set Indexing And Slicing Can't Be Done
#
# [4] Set Has Only Immutable Data Types
#     Examples allowed:
#     - Numbers
#     - Strings
#     - Tuples
#
#     Mutable types like List and Dictionary cannot be
#     placed directly inside a Set.
#
# [5] Set Items Are Unique
#     Duplicate values are automatically removed.


# ==========================================================
# 1. Not Ordered And Not Indexed
# ==========================================================

mySetOne = {"Osama", "Ahmed", 100}

print(mySetOne)

# Possible Output:
# {'Ahmed', 'Osama', 100}
#
# IMPORTANT:
# A Set is NOT ordered.
# This means we should not depend on the position/order
# in which the items are printed.
#
# The output could appear in a different order.


# ----------------------------------------------------------
# We cannot access a Set item using an Index
# ----------------------------------------------------------

# print(mySetOne[0])

# Error:
# TypeError: 'set' object is not subscriptable

# Why?
# Because Sets do not have indexes.
#
# In a List or Tuple we can do:
#
# myList[0]
# myTuple[0]
#
# But with Set:
#
# mySetOne[0]
#
# ❌ This is not allowed because Set is not indexed.


# ==========================================================
# 2. Slicing Can't Be Done
# ==========================================================

mySetTwo = {1, 2, 3, 4, 5, 6}

# print(mySetTwo[0:3])

# Error:
# TypeError: 'set' object is not subscriptable

# Slicing depends on indexes.
#
# Example with a List:
#
# [1, 2, 3, 4, 5, 6][0:3]
#
# Output:
# [1, 2, 3]
#
# But a Set has no indexes.
# Therefore slicing cannot be used with Sets.


# ==========================================================
# 3. Set Has Only Immutable Data Types
# ==========================================================

# A Set can contain immutable values such as:
# - String
# - Integer
# - Float
# - Boolean
# - Tuple


# ----------------------------------------------------------
# Example with List -> NOT Allowed
# ----------------------------------------------------------

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]}

# Error:
# TypeError: unhashable type: 'list'

# [1, 2, 3] is a List.
#
# A List is mutable, meaning its contents can be changed.
# Therefore a List cannot be an item inside a Set.


# ----------------------------------------------------------
# Example with Tuple -> Allowed
# ----------------------------------------------------------

mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Example Output:
# {True, 100.5, 100, (1, 2, 3), 'Osama'}

# (1, 2, 3) is a Tuple.
#
# Tuple is immutable, so it CAN be placed inside a Set.
#
# Again:
# The order of the output is not guaranteed because Sets
# are unordered.


# ==========================================================
# 4. Set Items Are Unique
# ==========================================================

mySetFour = {1, 2, "Osama", "One", "Osama", 1}

print(mySetFour)

# Output will contain only unique values.
#
# Example:
# {1, 2, 'One', 'Osama'}
#
# Notice:
#
# "Osama" appears twice in the original Set.
# 1 appears twice in the original Set.
#
# But the Set automatically removes duplicates.


# ----------------------------------------------------------
# Original:
# ----------------------------------------------------------

# {1, 2, "Osama", "One", "Osama", 1}
#
#                 ↓
#
# Duplicate "Osama" removed
# Duplicate 1 removed
#
#                 ↓
#
# {1, 2, "Osama", "One"}


# ==========================================================
# Important Comparison
# ==========================================================

# LIST
# []
# Ordered
# Indexed
# Supports Slicing
# Allows Duplicate Items
# Mutable
#
# Example:
myList = [1, 2, 2, 3]


# TUPLE
# ()
# Ordered
# Indexed
# Supports Slicing
# Allows Duplicate Items
# Immutable
#
# Example:
myTuple = (1, 2, 2, 3)


# SET
# {}
# Not Ordered
# Not Indexed
# Does NOT Support Slicing
# Does NOT Keep Duplicate Items
#
# Example:
mySet = {1, 2, 2, 3}

print(mySet)

# Output:
# {1, 2, 3}


# ==========================================================
# Quick Summary
# ==========================================================

# Set syntax:
#
# mySet = {item1, item2, item3}


# 1) Set uses curly braces:
#
# {"Osama", "Ahmed", 100}


# 2) Set is NOT ordered:
#
# We cannot depend on the position of an item.


# 3) Set is NOT indexed:
#
# mySet[0]       ❌


# 4) Set does NOT support slicing:
#
# mySet[0:3]     ❌


# 5) Set items must be immutable/hashable:
#
# "Osama"        ✅ String
# 100            ✅ Integer
# 100.5          ✅ Float
# True           ✅ Boolean
# (1, 2, 3)      ✅ Tuple
#
# [1, 2, 3]      ❌ List


# 6) Set items are unique:
#
# {1, 2, 1, 2, 3}
#
# becomes:
#
# {1, 2, 3}


# ==========================================================
# Easy Rule To Remember
# ==========================================================

# List  = Ordered + Changeable + Duplicates
#
# Tuple = Ordered + Immutable + Duplicates
#
# Set   = Unordered + No Index + Unique Items
#
# ==========================================================