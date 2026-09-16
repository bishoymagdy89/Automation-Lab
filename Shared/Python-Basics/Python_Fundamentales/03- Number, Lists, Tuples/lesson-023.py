# ============================================
# Lesson 023 - Lists Methods Part 2
# ============================================


# ============================================
# clear()
# ============================================

# clear() removes ALL items from the list.
# The list itself still exists, but becomes empty.

a = [1, 2, 3, 4]

a.clear()

print(a)

# Output:
# []


# ============================================
# copy()
# ============================================

# copy() creates a copy of the list.
# The copied list is separate from the original list.

b = [1, 2, 3, 4]

c = b.copy()

print(b)  # Main List
print(c)  # Copied List

# Output:
# [1, 2, 3, 4]
# [1, 2, 3, 4]


# --------------------------------------------
# Changing the original list after copy()
# --------------------------------------------

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# Output:
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4]

# Important:
# Adding 5 to "b" does NOT add it to "c".
# Because c is a copy of b.


# ============================================
# count()
# ============================================

# count() returns how many times
# a specific value exists in the list.

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]

print(d.count(1))

# Output:
# 3

# Number 1 appears 3 times.


# ============================================
# index()
# ============================================

# index() returns the index of the FIRST
# occurrence of a specific value.

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]

print(e.index("Ramy"))

# Output:
# 3

# Indexes:
# Osama -> 0
# Ahmed -> 1
# Sayed -> 2
# Ramy  -> 3
# Ahmed -> 4
# Ramy  -> 5

# Important:
# "Ramy" exists twice.
# index("Ramy") returns the FIRST occurrence -> index 3.


# ============================================
# insert()
# ============================================

# insert(index, value)
# Adds a value at a specific index.

f = [1, 2, 3, 4, 5, "A", "B"]

f.insert(0, "Test")

print(f)

# Output:
# ['Test', 1, 2, 3, 4, 5, 'A', 'B']

# insert(0, "Test")
# puts "Test" at index 0 (the beginning).


# --------------------------------------------
# insert() with negative index
# --------------------------------------------

f = [1, 2, 3, 4, 5, "A", "B"]

f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# Output:
# ['Test', 1, 2, 3, 4, 5, 'A', 'Test', 'B']

# -1 points to the position before the last item.
# So "Test" is inserted BEFORE "B".


# ============================================
# pop()
# ============================================

# pop(index) removes an item using its INDEX
# and RETURNS the removed item.

g = [1, 2, 3, 4, 5, "A", "B"]

print(g.pop(-1))

# Output:
# B

# -1 means the last item.
# So pop(-1) removes "B" and returns it.


# --------------------------------------------
# pop() also changes the original list
# --------------------------------------------

g = [1, 2, 3, 4, 5, "A", "B"]

removed_item = g.pop(-1)

print(removed_item)
print(g)

# Output:
# B
# [1, 2, 3, 4, 5, 'A']


# ============================================
# Quick Summary
# ============================================

# clear()
# Removes ALL items from the list.

# copy()
# Creates a copy of the list.

# count(value)
# Counts how many times a value exists.

# index(value)
# Returns the index of the FIRST matching value.

# insert(index, value)
# Inserts a value at a specific position.

# pop(index)
# Removes an item by INDEX and returns that item.


# ============================================
# Important Comparison
# ============================================

# remove(value)
# -> Remove by VALUE
#
# Example:
# x.remove("Osama")


# pop(index)
# -> Remove by INDEX
#
# Example:
# x.pop(2)


# insert(index, value)
# -> Add at a specific position
#
# Example:
# x.insert(0, "Test")


# append(value)
# -> Add at the END
#
# Example:
# x.append("Test")