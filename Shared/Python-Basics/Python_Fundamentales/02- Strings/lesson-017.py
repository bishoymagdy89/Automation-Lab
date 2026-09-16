# -----------------------------------
# -- Strings Formatting - Old Way
# -----------------------------------


# =========================
# String Concatenation
# =========================
# We can combine Strings using the + operator.

name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)

# Output:
# My Name is: Osama


# But we cannot concatenate a String directly with a Number.

# print("My Name is: " + name + " and My Age is: " + age)

# TypeError
# Because:
# name -> String
# age  -> Integer


# =========================
# Old String Formatting
# =========================
# Python provides an old formatting method using:
#
# %
#
# We put placeholders inside the String,
# then provide the values after %.


print("My Name is: %s" % "Osama")

# Output:
# My Name is: Osama


print("My Name is: %s" % name)

# Output:
# My Name is: Osama


# =========================
# Multiple Values
# =========================
# If we have multiple placeholders,
# we put the values inside ( ).

print("My Name is: %s and My Age is: %d" % (name, age))

# Output:
# My Name is: Osama and My Age is: 36


print(
    "My Name is: %s and My Age is: %d and My Rank is: %f"
    % (name, age, rank)
)

# Output:
# My Name is: Osama and My Age is: 36 and My Rank is: 10.000000


# =========================
# Formatting Placeholders
# =========================

# %s -> String
# %d -> Integer Number
# %f -> Floating Point Number


# Example:

n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Output:
# My Name is Osama Iam Python Developer With 10 Years Exp


# =========================
# Control Floating Point
# =========================
# By default, %f displays 6 digits after the decimal point.

myNumber = 10

print("My Number is: %d" % myNumber)
# My Number is: 10

print("My Number is: %f" % myNumber)
# My Number is: 10.000000


# We can control how many digits appear
# after the decimal point using:

# %.1f -> 1 digit after decimal
# %.2f -> 2 digits after decimal
# %.3f -> 3 digits after decimal


print("My Number is: %.1f" % myNumber)

# Output:
# My Number is: 10.0


print("My Number is: %.2f" % myNumber)

# Output:
# My Number is: 10.00


# =========================
# Truncate String
# =========================
# We can limit how many characters are displayed
# from a String using:
#
# %.Ns
#
# N = Maximum number of characters.


myLongString = "Hello Peoples of Elzero Web School I Love You All"

print("Message is %s" % myLongString)

# Output:
# Message is Hello Peoples of Elzero Web School I Love You All


print("Message is %.5s" % myLongString)

# Output:
# Message is Hello


# %.5s means:
# Take only the first 5 characters from the String.


# =========================
# Important Idea
# =========================

# %s
# -> Insert a String

# %d
# -> Insert an Integer

# %f
# -> Insert a Float

# %.2f
# -> Float with exactly 2 digits after decimal

# %.5s
# -> Display maximum 5 characters from a String


# =========================
# Quick Summary
# =========================

# +              -> Can concatenate String + String
#
# String + Number
# -> TypeError unless we convert the Number first
#
# %s             -> String
# %d             -> Integer
# %f             -> Float
#
# %.1f           -> Float with 1 decimal place
# %.2f           -> Float with 2 decimal places
#
# %.5s           -> First / Maximum 5 characters of String
#
# Multiple values:
#
# "%s %d" % (name, age)
#
# Old Formatting Structure:
#
# "Text %s %d %f" % (string_value, integer_value, float_value)
#
# Example:
#
# name = "Osama"
# age = 36
#
# print("My Name is %s and My Age is %d" % (name, age))
#
# Output:
# My Name is Osama and My Age is 36