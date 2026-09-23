# ============================================================
# Lesson 032 - Dictionary Methods Part Two
# ============================================================


# ============================================================
# 1) setdefault()
# ============================================================

# setdefault() searches for a key inside the dictionary.
#
# If the key EXISTS:
# - It returns the current value.
# - It does NOT change the value.
#
# If the key DOES NOT exist:
# - It adds the key with the default value we provide.
# - It returns that new value.
#
# Syntax:
# dictionary.setdefault(key, default_value)


user = {
    "name": "Osama"
}

print(user)
# Output:
# {'name': 'Osama'}


# ------------------------------------------------------------
# Example 1: The key already exists
# ------------------------------------------------------------

print(user.setdefault("name", "Ahmed"))

# "name" already exists and its value is "Osama".
# Therefore Python will NOT replace it with "Ahmed".
#
# Output:
# Osama

print(user)

# Output:
# {'name': 'Osama'}


# ------------------------------------------------------------
# Example 2: The key does NOT exist
# ------------------------------------------------------------

user = {
    "name": "Osama"
}

print(user)
# Output:
# {'name': 'Osama'}

print(user.setdefault("age", 36))

# "age" does not exist.
# Python adds:
# "age": 36
#
# And setdefault() returns the value 36.
#
# Output:
# 36

print(user)

# Output:
# {'name': 'Osama', 'age': 36}


# ------------------------------------------------------------
# Example 3: No default value is provided
# ------------------------------------------------------------

user = {
    "name": "Osama"
}

print(user.setdefault("age"))

# "age" does not exist and we did not specify a default value.
# Python uses None automatically.
#
# Output:
# None

print(user)

# Output:
# {'name': 'Osama', 'age': None}


# IMPORTANT:
#
# setdefault() is different from directly assigning a value.
#
# user["name"] = "Ahmed"
# -> Changes the existing value.
#
# user.setdefault("name", "Ahmed")
# -> Keeps the old value if "name" already exists.


print("=" * 40)


# ============================================================
# 2) popitem()
# ============================================================

# popitem() removes the LAST inserted item from the dictionary
# and returns it as a tuple:
#
# (key, value)


member = {
    "name": "Osama",
    "skill": "PS4"
}

print(member)

# Output:
# {'name': 'Osama', 'skill': 'PS4'}


member.update({"age": 36})

# Now the dictionary becomes:
# {
#     "name": "Osama",
#     "skill": "PS4",
#     "age": 36
# }


print(member.popitem())

# "age" was the last inserted item.
# popitem() removes it AND returns it.
#
# Output:
# ('age', 36)


# After popitem(), member becomes:
# {'name': 'Osama', 'skill': 'PS4'}


# IMPORTANT:
# popitem() modifies the original dictionary.


print("=" * 40)


# ============================================================
# 3) items()
# ============================================================

# items() returns a view containing all dictionary items
# as (key, value) pairs.
#
# Each pair looks like:
# ('name', 'Osama')
#
# The important point:
# The returned view is connected to the original dictionary.
# If the dictionary changes, the view reflects that change.


view = {
    "name": "Osama",
    "skill": "XBox"
}


allItems = view.items()


print(view)

# Output:
# {'name': 'Osama', 'skill': 'XBox'}


# Add a new item AFTER creating allItems

view["age"] = 36


print(allItems)

# Even though allItems was created BEFORE adding "age",
# it reflects the new dictionary content.
#
# Output:
# dict_items([
#     ('name', 'Osama'),
#     ('skill', 'XBox'),
#     ('age', 36)
# ])


# This is because view.items() returns a dynamic VIEW,
# not a completely independent copy.


# ============================================================
# 4) fromkeys()
# ============================================================

# fromkeys() creates a NEW dictionary from a collection of keys.
#
# All keys receive the same value.
#
# Syntax:
# dict.fromkeys(keys, value)


a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")

b = "X"


print(dict.fromkeys(a, b))

# Python takes every item from tuple "a" and makes it a key.
# Then it gives every key the value stored in "b".
#
# Output:
# {
#     'MyKeyOne': 'X',
#     'MyKeyTwo': 'X',
#     'MyKeyThree': 'X'
# }


# Another way to understand it:
#
# Keys:
# MyKeyOne
# MyKeyTwo
# MyKeyThree
#
# Shared value:
# X
#
# Result:
# MyKeyOne   -> X
# MyKeyTwo   -> X
# MyKeyThree -> X


# If we don't provide the second argument:

example = dict.fromkeys(a)

print(example)

# Python uses None as the default value.
#
# Output:
# {
#     'MyKeyOne': None,
#     'MyKeyTwo': None,
#     'MyKeyThree': None
# }


# ============================================================
# QUICK SUMMARY
# ============================================================

# setdefault(key, value)
# -> If key exists:
#       returns its current value and changes nothing.
# -> If key doesn't exist:
#       adds key:value and returns the new value.
# -> If value isn't provided:
#       default value = None
#
# Example:
# user.setdefault("age", 36)


# popitem()
# -> Removes the LAST inserted item.
# -> Returns it as a tuple (key, value).
#
# Example:
# member.popitem()
# Output:
# ('age', 36)


# items()
# -> Returns all dictionary key/value pairs.
# -> Returns a dynamic view connected to the dictionary.
#
# Example:
# view.items()
#
# Output:
# dict_items([('name', 'Osama'), ('skill', 'XBox')])


# fromkeys(keys, value)
# -> Creates a NEW dictionary.
# -> Uses the provided collection as keys.
# -> Gives every key the same value.
#
# Example:
# dict.fromkeys(("A", "B", "C"), "X")
#
# Output:
# {'A': 'X', 'B': 'X', 'C': 'X'}


# ============================================================
# SUPER SHORT MEMORY
# ============================================================

# setdefault() -> Get existing value OR add a default
# popitem()    -> Remove + return the last item
# items()      -> Get key/value pairs as a dynamic view
# fromkeys()   -> Create dictionary from keys with same value