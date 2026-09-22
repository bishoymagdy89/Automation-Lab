# ==========================================================
# Lesson 029 - Set Methods Part Three
# ==========================================================

# In this lesson:
# 1- issuperset()
# 2- issubset()
# 3- isdisjoint()
#
# Important:
# These methods return Boolean values:
# True or False
#
# They DO NOT modify the sets.


# ==========================================================
# 1- issuperset()
# ==========================================================

# issuperset() checks:
# "Does the first set contain ALL items of the second set?"

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))
# True

print(a.issuperset(c))
# False


# Explanation:
#
# a = {1, 2, 3, 4}
# b = {1, 2, 3}
#
# a contains ALL elements of b.
#
# Therefore:
# a.issuperset(b) -> True
#
#
# c = {1, 2, 3, 4, 5}
#
# a does NOT contain 5.
#
# Therefore:
# a.issuperset(c) -> False


# Easy way to think about it:
#
# a.issuperset(b)
#
# Ask:
# "Does A contain everything inside B?"


# ==========================================================
# 2- issubset()
# ==========================================================

# issubset() is basically the opposite question.
#
# It checks:
# "Are ALL items of the first set inside the second set?"

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))
# False

print(d.issubset(f))
# True


# Explanation:
#
# d = {1, 2, 3, 4}
# e = {1, 2, 3}
#
# Is EVERYTHING from d inside e?
#
# No.
#
# Number 4 is missing from e.
#
# Therefore:
# d.issubset(e) -> False


# Now:
#
# d = {1, 2, 3, 4}
# f = {1, 2, 3, 4, 5}
#
# Everything from d exists inside f.
#
# Therefore:
# d.issubset(f) -> True


# ==========================================================
# issuperset() VS issubset()
# ==========================================================

# This is the easiest way to understand the difference:


# SUPERSET:
#
# a.issuperset(b)
#
# Ask:
# "Does A contain all of B?"
#
# Example:
#
# A = {1, 2, 3, 4}
# B = {1, 2}
#
# A contains everything in B.
#
# True


# SUBSET:
#
# b.issubset(a)
#
# Ask:
# "Is B completely inside A?"
#
# True


# So these two ideas are related:
#
# A.issuperset(B) == B.issubset(A)


# Example:

A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))
# True

print(B.issubset(A))
# True


# ==========================================================
# 3- isdisjoint()
# ==========================================================

# isdisjoint() checks whether two sets have
# NO common items.
#
# If they have ZERO common items:
# True
#
# If they have at least ONE common item:
# False


g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))
# False

print(g.isdisjoint(i))
# True


# Explanation:
#
# g = {1, 2, 3, 4}
# h = {1, 2, 3}
#
# They share:
# 1, 2, 3
#
# Therefore they are NOT disjoint.
#
# Result:
# False


# But:
#
# g = {1, 2, 3, 4}
# i = {10, 11, 12}
#
# They share NOTHING.
#
# Therefore:
# True


# ==========================================================
# Visual Understanding
# ==========================================================

# SUPERSET
#
# A = {1, 2, 3, 4}
# B = {1, 2}
#
# Think:
#
# A
# ┌─────────────────────┐
# │  3     4            │
# │     ┌─────────┐     │
# │     │  1   2  │ B   │
# │     └─────────┘     │
# └─────────────────────┘
#
# B is completely inside A.
#
# A.issuperset(B) -> True
# B.issubset(A)   -> True


# ==========================================================
# DISJOINT
# ==========================================================

# A = {1, 2, 3}
# B = {10, 20, 30}
#
# There is NO intersection between them.
#
# A.isdisjoint(B) -> True


# But:

# A = {1, 2, 3}
# B = {3, 10, 20}
#
# They share number 3.
#
# A.isdisjoint(B) -> False


# ==========================================================
# Quick Summary
# ==========================================================

# issuperset()
#
# A.issuperset(B)
#
# Question:
# "Does A contain ALL of B?"
#
# Example:
# A = {1, 2, 3, 4}
# B = {1, 2}
#
# Result:
# True


# ----------------------------------------------------------


# issubset()
#
# A.issubset(B)
#
# Question:
# "Is ALL of A inside B?"
#
# Example:
# A = {1, 2}
# B = {1, 2, 3, 4}
#
# Result:
# True


# ----------------------------------------------------------


# isdisjoint()
#
# A.isdisjoint(B)
#
# Question:
# "Do A and B have ZERO common items?"
#
# Example:
# A = {1, 2}
# B = {10, 20}
#
# Result:
# True


# ==========================================================
# Easy Memory Trick
# ==========================================================

# SUPERSET
# -> "I contain you."
#
# A.issuperset(B)
# -> Does A contain B?


# SUBSET
# -> "I am inside you."
#
# A.issubset(B)
# -> Is A inside B?


# DISJOINT
# -> "We have nothing in common."
#
# A.isdisjoint(B)
# -> Do A and B have NO common items?


# ==========================================================
# VERY SHORT REVISION
# ==========================================================

# issuperset()
# -> Does MY set contain ALL of the other set?


# issubset()
# -> Is MY set completely inside the other set?


# isdisjoint()
# -> Do the two sets have NO common elements?


# ==========================================================
# Final Example
# ==========================================================

network_devices = {"Router", "Switch", "Firewall", "AP"}

security_devices = {"Firewall"}

servers = {"Linux", "Windows"}


print(network_devices.issuperset(security_devices))
# True
# network_devices contains "Firewall"


print(security_devices.issubset(network_devices))
# True
# Everything in security_devices exists in network_devices


print(network_devices.isdisjoint(servers))
# True
# They have no common elements