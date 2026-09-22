# ==========================================================
# Lesson 028 - Set Methods Part Two
# ==========================================================

# In this lesson:
# 1- difference()
# 2- difference_update()
# 3- intersection()
# 4- intersection_update()
# 5- symmetric_difference()
# 6- symmetric_difference_update()


# ==========================================================
# 1- difference()
# ==========================================================

# difference() returns the items that exist in the FIRST set
# but do NOT exist in the second set.
#
# Important:
# It DOES NOT change the original set.

a = {1, 2, 3, 4}
b = {1, 2, "Osama", "Ahmed"}

print(a)

print(a.difference(b))
# Same idea as:
# print(a - b)

print(a)


# Output:
# {1, 2, 3, 4}
# {3, 4}
# {1, 2, 3, 4}


# Explanation:
#
# a = {1, 2, 3, 4}
# b = {1, 2, "Osama", "Ahmed"}
#
# 1 and 2 exist in both sets.
# 3 and 4 exist only in a.
#
# So:
# a - b = {3, 4}
#
# The original set "a" stays unchanged.


# ==========================================================
# 2- difference_update()
# ==========================================================

# difference_update() does the same comparison as difference(),
# BUT it changes the original set itself.

c = {1, 2, 3, 4}
d = {1, 2, 3, "Osama", "Ahmed"}

print(c)

c.difference_update(d)
# Same concept as:
# c = c - d

print(c)


# Output:
# {1, 2, 3, 4}
# {4}


# Explanation:
#
# Common items:
# 1, 2, 3
#
# Only 4 exists in c but not in d.
#
# difference_update() modifies c itself.
#
# Before:
# c = {1, 2, 3, 4}
#
# After:
# c = {4}


# ==========================================================
# difference() VS difference_update()
# ==========================================================

# difference()
# -> Returns the difference.
# -> Original set does NOT change.
#
# difference_update()
# -> Calculates the difference.
# -> Original set IS changed.


# ==========================================================
# 3- intersection()
# ==========================================================

# intersection() returns ONLY the items that exist
# in BOTH sets.
#
# It does NOT change the original set.

e = {1, 2, 3, 4, "X"}
f = {"Osama", "X", 2}

print(e)

print(e.intersection(f))
# Same idea as:
# print(e & f)

print(e)


# Output:
# {1, 2, 3, 4, 'X'}
# {2, 'X'}
# {1, 2, 3, 4, 'X'}


# Explanation:
#
# e = {1, 2, 3, 4, "X"}
# f = {"Osama", "X", 2}
#
# Common items:
# 2
# "X"
#
# Result:
# {2, "X"}
#
# e stays unchanged.


# ==========================================================
# 4- intersection_update()
# ==========================================================

# intersection_update() keeps ONLY the common items
# and modifies the original set.

g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}

print(g)

g.intersection_update(h)
# Same concept as:
# g = g & h

print(g)


# Output:
# {1, 2, 3, 4, 'X', 'Osama'}
# {2, 'X', 'Osama'}


# Explanation:
#
# Common items between g and h:
# 2
# "X"
# "Osama"
#
# Because we used intersection_update(),
# g itself becomes:
#
# {2, "X", "Osama"}


# ==========================================================
# intersection() VS intersection_update()
# ==========================================================

# intersection()
# -> Returns common items.
# -> Original set does NOT change.
#
# intersection_update()
# -> Keeps common items.
# -> Original set IS changed.


# ==========================================================
# 5- symmetric_difference()
# ==========================================================

# symmetric_difference() returns items that exist
# in either set BUT NOT in both.
#
# In simple words:
# Remove the common items and keep everything else.
#
# It does NOT change the original set.

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4}

print(i)

print(i.symmetric_difference(j))
# Same idea as:
# print(i ^ j)

print(i)


# Let's analyze it:
#
# i = {1, 2, 3, 4, 5, "X"}
# j = {"Osama", "Zero", 1, 2, 4}
#
# Common:
# 1, 2, 4
#
# Remove common items.
#
# From i we keep:
# 3, 5, "X"
#
# From j we keep:
# "Osama", "Zero"
#
# Result:
# {3, 5, "X", "Osama", "Zero"}
#
# i itself remains unchanged.


# ==========================================================
# 6- symmetric_difference_update()
# ==========================================================

# symmetric_difference_update() does the same thing,
# BUT modifies the original set.

k = {1, 2, 3, 4, 5, "X"}
l = {"Osama", "Zero", 1, 2, 4, "X"}

print(k)

k.symmetric_difference_update(l)
# Same concept as:
# k = k ^ l

print(k)


# Common items:
# 1
# 2
# 4
# "X"
#
# They are removed.
#
# Remaining from k:
# 3, 5
#
# Remaining from l:
# "Osama", "Zero"
#
# k becomes:
# {3, 5, "Osama", "Zero"}


# ==========================================================
# IMPORTANT IDEA
# ==========================================================

# Think about the methods like this:


# DIFFERENCE
#
# A = {1, 2, 3, 4}
# B = {1, 2}
#
# A - B
#
# "What exists in A but NOT in B?"
#
# Result:
# {3, 4}


# INTERSECTION
#
# A = {1, 2, 3, 4}
# B = {1, 2}
#
# A & B
#
# "What exists in BOTH?"
#
# Result:
# {1, 2}


# SYMMETRIC DIFFERENCE
#
# A = {1, 2, 3, 4}
# B = {1, 2, 5, 6}
#
# A ^ B
#
# "Remove everything common and keep the differences."
#
# Common:
# {1, 2}
#
# Result:
# {3, 4, 5, 6}


# ==========================================================
# NORMAL METHOD VS _update METHOD
# ==========================================================

# This is the MOST IMPORTANT pattern in this lesson.


# Normal:
#
# difference()
# intersection()
# symmetric_difference()
#
# They return a NEW result.
# The original set remains unchanged.


# Update versions:
#
# difference_update()
# intersection_update()
# symmetric_difference_update()
#
# They MODIFY the original set itself.


# Example:

test_a = {1, 2, 3, 4}
test_b = {1, 2}

print(test_a.difference(test_b))
# {3, 4}

print(test_a)
# {1, 2, 3, 4}
# test_a did NOT change


test_a.difference_update(test_b)

print(test_a)
# {3, 4}
# test_a changed


# ==========================================================
# Quick Summary
# ==========================================================

# difference()
# A - B
# Items in A that are NOT in B.
# Does NOT modify A.


# difference_update()
# A - B
# Items in A that are NOT in B.
# MODIFIES A.


# intersection()
# A & B
# Items common between A and B.
# Does NOT modify A.


# intersection_update()
# A & B
# Keeps common items only.
# MODIFIES A.


# symmetric_difference()
# A ^ B
# Items that are NOT common between the two sets.
# Does NOT modify A.


# symmetric_difference_update()
# A ^ B
# Keeps items that are NOT common.
# MODIFIES A.


# ==========================================================
# Easy Memory Trick
# ==========================================================

# difference
# -> "What do I have that you don't?"

# intersection
# -> "What do we both have?"

# symmetric_difference
# -> "What is different between us?"

# _update
# -> "Change my original set"


# ==========================================================
# VERY SHORT REVISION
# ==========================================================

# difference()                  -> A - B
# difference_update()           -> A = A - B

# intersection()                -> A & B
# intersection_update()         -> A = A & B

# symmetric_difference()        -> A ^ B
# symmetric_difference_update() -> A = A ^ B


# Note:
# Sets are unordered, so the order of items in the output
# may be different when you run the code.