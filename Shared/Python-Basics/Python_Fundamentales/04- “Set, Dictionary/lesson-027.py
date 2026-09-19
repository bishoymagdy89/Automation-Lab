# ==========================================================
# Lesson 027 - Set Methods Part 1
# ==========================================================


# ==========================================================
# 1. clear()
# ==========================================================

# clear() removes ALL items from the Set.
# The Set itself still exists, but it becomes empty.

a = {1, 2, 3}

a.clear()

print(a)

# Output:
# set()

# Important:
# Empty Set is displayed as:
#
# set()
#
# NOT:
# {}
#
# Because {} represents an empty Dictionary in Python.


# ==========================================================
# 2. union()
# ==========================================================

# union() combines two or more Sets together.
#
# Because Sets contain unique values,
# duplicate items will appear only once.

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}


# ----------------------------------------------------------
# Method 1: Using | Operator
# ----------------------------------------------------------

print(b | c)

# Possible Output:
# {'One', 'Two', 'Three', '1', '2', '3'}

# | means UNION when used between Sets.


# ----------------------------------------------------------
# Method 2: Using union()
# ----------------------------------------------------------

print(b.union(c, x))

# Possible Output:
# {'One', 'Two', 'Three', '1', '2', '3', 'Zero', 'Cool'}

# union() can combine more than two Sets at once.
#
# Here:
#
# b + c + x
#
# are combined into ONE new Set.


# Important:
# union() DOES NOT change the original Set b.
#
# It RETURNS a new Set containing the combined items.

# Think about it like:
#
# b.union(c, x)
#
#            b
#          /   \
#         c     x
#          \   /
#        New Set


# ==========================================================
# 3. add()
# ==========================================================

# add() adds ONE item to a Set.

d = {1, 2, 3, 4}

d.add(5)
d.add(6)

print(d)

# Output:
# {1, 2, 3, 4, 5, 6}


# ----------------------------------------------------------
# Important: add() Takes ONE Argument Only
# ----------------------------------------------------------

# This is WRONG:

# d.add(5, 6)

# Error:
# TypeError: add() takes exactly one argument (2 given)


# Correct:

d.add(5)
d.add(6)

# So:
#
# add(5)       ✅
# add(6)       ✅
#
# add(5, 6)    ❌


# ==========================================================
# 4. copy()
# ==========================================================

# copy() creates a copy of the Set.

e = {1, 2, 3, 4}

f = e.copy()

print(e)
print(f)

# Output:
#
# {1, 2, 3, 4}
# {1, 2, 3, 4}


# ----------------------------------------------------------
# The Copy Is Independent
# ----------------------------------------------------------

e.add(6)

print(e)
print(f)

# Output:
#
# {1, 2, 3, 4, 6}
# {1, 2, 3, 4}


# Notice:
#
# We added 6 to e.
#
# e changed:
# {1, 2, 3, 4, 6}
#
# But f did NOT change:
# {1, 2, 3, 4}
#
# Because f is a COPY of e.
#
# After copying:
#
#       e                       f
# {1, 2, 3, 4}          {1, 2, 3, 4}
#       |                       |
#    separate                separate
#
# Changing e does not change f.


# ==========================================================
# 5. remove()
# ==========================================================

# remove() removes a specific item from a Set.

g = {1, 2, 3, 4}

g.remove(1)

print(g)

# Output:
# {2, 3, 4}


# ----------------------------------------------------------
# What If The Item Does NOT Exist?
# ----------------------------------------------------------

# g.remove(7)

# Error:
# KeyError: 7


# This is VERY important:
#
# remove() expects the item to exist.
#
# Existing item:
#
# g.remove(1)
# ✅ Removes it
#
#
# Non-existing item:
#
# g.remove(7)
# ❌ KeyError


# ==========================================================
# 6. discard()
# ==========================================================

# discard() is similar to remove().
# It removes an item from the Set.

h = {1, 2, 3, 4}

h.discard(1)

print(h)

# Output:
# {2, 3, 4}


# ----------------------------------------------------------
# Difference Between remove() And discard()
# ----------------------------------------------------------

# If the item DOES NOT exist:

h.discard(7)

print(h)

# Output:
# {2, 3, 4}

# NO ERROR happens.


# remove():
#
# Existing Item     -> Removes it
# Missing Item      -> KeyError
#
#
# discard():
#
# Existing Item     -> Removes it
# Missing Item      -> Does nothing


# Easy way to remember:
#
# remove()  = "The item MUST be there."
#
# discard() = "Remove it if you find it,
#              otherwise don't worry."


# ==========================================================
# 7. pop()
# ==========================================================

i = {"A", True, 1, 2, 3, 4, 5}

print(i.pop())

# pop() removes AND returns an item from the Set.


# IMPORTANT:
#
# With List:
#
# list.pop()
#
# normally removes the last item.
#
# But Set is UNORDERED.
#
# So with a Set we should NOT depend on pop()
# removing a specific item.


# Example:
#
# removedItem = i.pop()
#
# One item is removed and returned.
#
# But you should NOT write code assuming which specific
# Set item will be returned.


# ==========================================================
# 8. update()
# ==========================================================

# update() adds multiple items to an existing Set.

j = {1, 2, 3}

k = {1, "A", "B", 2}

j.update(k)

print(j)

# Possible Output:
# {1, 2, 3, 'A', 'B'}


# Notice:
#
# j originally:
#
# {1, 2, 3}
#
# k:
#
# {1, "A", "B", 2}
#
# 1 and 2 already exist in j.
#
# Because Set items are UNIQUE,
# they will NOT be duplicated.
#
# Result:
#
# {1, 2, 3, "A", "B"}


# ----------------------------------------------------------
# update() Can Also Take Other Iterables
# ----------------------------------------------------------

j = {1, 2, 3}

j.update(["Html", "Css"])

print(j)

# Possible Output:
# {1, 2, 3, 'Html', 'Css'}

# Here we passed a List to update().
#
# update() takes the ITEMS inside the iterable
# and adds them individually to the Set.


# We can also combine this with another Set:

j = {1, 2, 3}
k = {1, "A", "B", 2}

j.update(["Html", "Css"])
j.update(k)

print(j)

# Possible Output:
# {1, 2, 3, 'Html', 'Css', 'A', 'B'}


# ==========================================================
# add() VS update()
# ==========================================================

# add()
# -----
# Adds ONE item.

mySet = {1, 2, 3}

mySet.add(4)

# Result:
# {1, 2, 3, 4}


# update()
# --------
# Adds MULTIPLE items from another iterable.

mySet.update([5, 6, 7])

# Result:
# {1, 2, 3, 4, 5, 6, 7}


# Think:
#
# add()       -> ONE ITEM
#
# update()    -> MULTIPLE ITEMS


# ==========================================================
# union() VS update()
# ==========================================================

setOne = {1, 2, 3}
setTwo = {3, 4, 5}


# union()
# -------
# Creates/returns a NEW Set.
# It does NOT modify setOne.

result = setOne.union(setTwo)

# setOne:
# {1, 2, 3}
#
# result:
# {1, 2, 3, 4, 5}


# update()
# --------
# Changes the original Set directly.

setOne.update(setTwo)

# Now setOne becomes:
#
# {1, 2, 3, 4, 5}


# Easy Rule:
#
# union()  -> Give me the combined result
#
# update() -> Update THIS Set with those items


# ==========================================================
# Quick Summary - Set Methods Part 1
# ==========================================================

# clear()
# --------
# Removes ALL items.
#
# a.clear()
#
# {1, 2, 3}
#      ↓
# set()


# ----------------------------------------------------------

# union()
# --------
# Combines Sets and RETURNS a new Set.
#
# a.union(b)
#
# OR
#
# a | b


# ----------------------------------------------------------

# add()
# -----
# Adds ONE item.
#
# a.add(5)


# ----------------------------------------------------------

# copy()
# ------
# Creates an independent copy.
#
# b = a.copy()


# ----------------------------------------------------------

# remove()
# --------
# Removes an item.
#
# a.remove(5)
#
# Item exists     -> Removed
# Item missing    -> ❌ KeyError


# ----------------------------------------------------------

# discard()
# ----------
# Removes an item if it exists.
#
# a.discard(5)
#
# Item exists     -> Removed
# Item missing    -> No Error


# ----------------------------------------------------------

# pop()
# -----
# Removes AND returns an item.
#
# a.pop()
#
# Because Set is unordered,
# don't depend on WHICH item will be returned.


# ----------------------------------------------------------

# update()
# --------
# Adds multiple items and modifies the original Set.
#
# a.update(b)
#
# or:
#
# a.update([4, 5, 6])


# ==========================================================
# Most Important Differences
# ==========================================================

# add() vs update()
#
# add()       -> ONE item
# update()    -> MULTIPLE items


# remove() vs discard()
#
# remove()    -> Missing item = ERROR
# discard()   -> Missing item = NO ERROR


# union() vs update()
#
# union()     -> Returns a NEW combined Set
# update()    -> Modifies the ORIGINAL Set


# ==========================================================
# Lesson 027 Finished
# ==========================================================