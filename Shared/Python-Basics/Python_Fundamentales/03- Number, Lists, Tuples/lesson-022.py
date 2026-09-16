# ============================================
# Lesson 022 - Lists Methods Part 1
# ============================================


# ============================================
# append()
# ============================================

# append() adds ONE item to the end of the list.

myFriends = ["Osama", "Ahmed", "Sayed"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)

print(myFriends)

# Output:
# ['Osama', 'Ahmed', 'Sayed', 'Alaa', 100, 150.2, True]


# --------------------------------------------
# append() can add another list as ONE item
# --------------------------------------------

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)

# Output:
# ['Osama', 'Ahmed', 'Sayed', 'Alaa', 100, 150.2, True,
# ['Haytham', 'Samah', 'Ali']]


# --------------------------------------------
# Accessing items after appending a list
# --------------------------------------------

print(myFriends[2])
# Output:
# Sayed

print(myFriends[6])
# Output:
# True

print(myFriends[7])
# Output:
# ['Haytham', 'Samah', 'Ali']

print(myFriends[7][2])
# Output:
# Ali

# myFriends[7]    -> The nested list
# myFriends[7][2] -> Item index 2 inside the nested list


# ============================================
# extend()
# ============================================

# extend() adds the ITEMS of another list
# individually to the end of the current list.

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# Output:
# [1, 2, 3, 4, 'A', 'B', 'C', 'One', 'Two']


# --------------------------------------------
# append() vs extend()
# --------------------------------------------

# append()
# Adds the whole list as ONE item.
#
# Example:
# a.append(b)
#
# Result:
# [1, 2, 3, 4, ['A', 'B', 'C']]


# extend()
# Adds every item separately.
#
# Example:
# a.extend(b)
#
# Result:
# [1, 2, 3, 4, 'A', 'B', 'C']


# ============================================
# remove()
# ============================================

# remove() removes the FIRST matching value.

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]

x.remove("Osama")

print(x)

# Output:
# [1, 2, 3, 4, 5, True, 'Osama', 'Osama']

# Important:
# "Osama" exists 3 times.
# remove("Osama") removes ONLY the first occurrence.


# ============================================
# sort()
# ============================================

# sort() sorts numbers from smallest to largest
# by default.

y = [1, 2, 100, 120, -10, 17, 29]

y.sort()

print(y)

# Output:
# [-10, 1, 2, 17, 29, 100, 120]


# --------------------------------------------
# sort(reverse=True)
# --------------------------------------------

# reverse=True sorts from largest to smallest.

y = [1, 2, 100, 120, -10, 17, 29]

y.sort(reverse=True)

print(y)

# Output:
# [120, 100, 29, 17, 2, 1, -10]


# --------------------------------------------
# Sorting Strings
# --------------------------------------------

y = ["A", "Z", "C"]

y.sort(reverse=True)

print(y)

# Output:
# ['Z', 'C', 'A']


# --------------------------------------------
# Important: int + str cannot be sorted together
# --------------------------------------------

# y = [1, 2, 100, 120, -10, 17, 29, "Osama"]
# y.sort(reverse=True)
# print(y)

# Output:
# TypeError:
# '<' not supported between instances of 'int' and 'str'

# Python cannot compare numbers and strings
# to decide which one should come first.


# ============================================
# reverse()
# ============================================

# reverse() does NOT sort the list.
# It only reverses the CURRENT order.

z = [10, 1, 9, 80, 100, "Osama", 100]

z.reverse()

print(z)

# Output:
# [100, 'Osama', 100, 80, 9, 1, 10]


# ============================================
# Important Differences
# ============================================

# append()
# Adds ONE item to the end.

# extend()
# Adds multiple items from another iterable.

# remove()
# Removes the FIRST matching value.

# sort()
# Sorts the values.

# sort(reverse=True)
# Sorts in descending order.

# reverse()
# Does NOT sort.
# It only reverses the existing order.