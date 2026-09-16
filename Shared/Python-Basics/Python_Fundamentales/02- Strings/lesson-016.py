# -----------------------------------
# -- String Methods - Part 4
# -----------------------------------


# =========================
# replace(Old Value, New Value, Count)
# =========================
# Replaces a specific value inside the string with another value.
#
# Old Value -> The text we want to replace.
# New Value -> The new text.
# Count     -> Optional: How many occurrences we want to replace.
#
# If Count is not specified, ALL occurrences are replaced.

a = "Hello One Two Three One One"

print(a.replace("One", "1"))
# Hello 1 Two Three 1 1
# Replaces ALL "One" with "1"

print(a.replace("One", "1", 1))
# Hello 1 Two Three One One
# Replaces only the FIRST occurrence

print(a.replace("One", "1", 2))
# Hello 1 Two Three 1 One
# Replaces only the FIRST TWO occurrences


# =========================
# join(Iterable)
# =========================
# Joins multiple strings together into ONE string.
#
# The string before .join() is used as the separator
# between the items.
#
# Very useful when we have a List of strings
# and want to combine them into one String.

myList = ["Osama", "Mohamed", "Elsayed"]

print("-".join(myList))
# Osama-Mohamed-Elsayed

print(" ".join(myList))
# Osama Mohamed Elsayed

print(", ".join(myList))
# Osama, Mohamed, Elsayed


# join() returns a String.

print(type(", ".join(myList)))
# <class 'str'>


# =========================
# Important Idea
# =========================

# split() and join() can be thought of as opposite operations:
#
# split()
# String -> List
#
# join()
# List of Strings -> String


# Example:

names = "Osama,Mohamed,Elsayed"

names_list = names.split(",")
print(names_list)
# ['Osama', 'Mohamed', 'Elsayed']

names_string = " - ".join(names_list)
print(names_string)
# Osama - Mohamed - Elsayed


# =========================
# Quick Summary
# =========================

# replace(old, new)
# -> Replace ALL occurrences of old text with new text.
#
# replace(old, new, count)
# -> Replace only a specific number of occurrences.
#
# join(iterable)
# -> Join multiple strings together into ONE String.
#
# "-".join(myList)
# -> Osama-Mohamed-Elsayed
#
# " ".join(myList)
# -> Osama Mohamed Elsayed
#
# ", ".join(myList)
# -> Osama, Mohamed, Elsayed
#
# split() -> String -> List
# join()  -> List of Strings -> String