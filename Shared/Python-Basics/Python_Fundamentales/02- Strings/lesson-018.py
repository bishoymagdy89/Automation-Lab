# ============================================================
# Lesson 018 - Strings Formatting - The New Ways
# ============================================================


# ------------------------------------------------------------
# 1) String Formatting Using .format()
# ------------------------------------------------------------

# The format() method allows us to insert values inside a string.
# We use {} as placeholders for the values.

name = "Osama"
age = 36
rank = 10


# Normal string concatenation using +
print("My Name is: " + name)

# Output:
# My Name is: Osama


# This will cause TypeError because age is an integer.
# Python cannot concatenate String + Integer directly.

# print("My Name is: " + name + " and My Age is: " + age)

# TypeError


# ------------------------------------------------------------
# Using .format()
# ------------------------------------------------------------

print("My Name is: {}".format("Osama"))

# {} will be replaced by "Osama"

# Output:
# My Name is: Osama


print("My Name is: {}".format(name))

# The value of the variable name replaces {}

# Output:
# My Name is: Osama


print("My Name is: {} My Age: {}".format(name, age))

# First {}  -> name
# Second {} -> age

# Output:
# My Name is: Osama My Age: 36


# ------------------------------------------------------------
# 2) Formatting Data Types
# ------------------------------------------------------------

# We can tell format() what type of data we expect.

# {:s} => String
# {:d} => Integer Number
# {:f} => Float


print(
    "My Name is: {:s} Age: {:d} & Rank is: {:f}".format(
        name, age, rank
    )
)

# name -> {:s} because name is String
# age  -> {:d} because age is Integer
# rank -> {:f} converts/displays the number as Float

# Output:
# My Name is: Osama Age: 36 & Rank is: 10.000000


# ------------------------------------------------------------
# Another Example
# ------------------------------------------------------------

n = "Osama"
l = "Python"
y = 10

print(
    "My Name is {} Iam {} Developer With {:d} Years Exp".format(
        n, l, y
    )
)

# {}   -> n = Osama
# {}   -> l = Python
# {:d} -> y = 10

# Output:
# My Name is Osama Iam Python Developer With 10 Years Exp


# ============================================================
# 3) Control Floating Point Number
# ============================================================

# {:f}
# Displays the number as a float.
# By default Python displays 6 digits after the decimal point.

myNumber = 10

print("My Number is: {:d}".format(myNumber))

# Output:
# My Number is: 10


print("My Number is: {:f}".format(myNumber))

# Output:
# My Number is: 10.000000


# We can control how many digits appear after the decimal point.
#
# {:.2f}
#
# .2 means -> 2 digits after decimal point
# f  means -> Float

print("My Number is: {:.2f}".format(myNumber))

# Output:
# My Number is: 10.00


# ============================================================
# 4) Truncate String
# ============================================================

# We can limit how many characters from a string are displayed.
#
# {:.5s}
#
# .5 means -> Maximum 5 characters
# s  means -> String


myLongString = "Hello Peoples of Elzero Web School I Love You All"

print("Message is {}".format(myLongString))

# Output:
# Message is Hello Peoples of Elzero Web School I Love You All


print("Message is {:.5s}".format(myLongString))

# Only the first 5 characters are displayed.

# Output:
# Message is Hello


print("Message is {:.13s}".format(myLongString))

# Only the first 13 characters are displayed.

# Output:
# Message is Hello Peoples


# ============================================================
# 5) Format Money
# ============================================================

myMoney = 500162350198


print("My Money in Bank Is: {:d}".format(myMoney))

# Normal integer without separators.

# Output:
# My Money in Bank Is: 500162350198


# ------------------------------------------------------------
# Add underscore _ as separator
# ------------------------------------------------------------

print("My Money in Bank Is: {:_d}".format(myMoney))

# Output:
# My Money in Bank Is: 500_162_350_198


# ------------------------------------------------------------
# Add comma , as separator
# ------------------------------------------------------------

print("My Money in Bank Is: {:,d}".format(myMoney))

# Output:
# My Money in Bank Is: 500,162,350,198


# ------------------------------------------------------------
# Invalid Separator
# ------------------------------------------------------------

# Python does NOT allow any random character as separator.

# print("My Money in Bank Is: {:&d}".format(myMoney))

# Output:
# ValueError: Invalid format specifier


# ============================================================
# 6) ReArrange Items
# ============================================================

# Normally format() inserts values in the same order
# they are passed to it.

a, b, c = "One", "Two", "Three"

print("Hello {} {} {}".format(a, b, c))

# {} -> a
# {} -> b
# {} -> c

# Output:
# Hello One Two Three


# ------------------------------------------------------------
# We can use indexes to change the order.
#
# a -> index 0
# b -> index 1
# c -> index 2
# ------------------------------------------------------------

print("Hello {1} {2} {0}".format(a, b, c))

# {1} -> b -> Two
# {2} -> c -> Three
# {0} -> a -> One

# Output:
# Hello Two Three One


print("Hello {2} {0} {1}".format(a, b, c))

# {2} -> c -> Three
# {0} -> a -> One
# {1} -> b -> Two

# Output:
# Hello Three One Two


# ============================================================
# ReArrange Numbers
# ============================================================

x, y, z = 10, 20, 30

print("Hello {} {} {}".format(x, y, z))

# Output:
# Hello 10 20 30


# We can rearrange the numbers using indexes
# and specify their data type.

print("Hello {1:d} {2:d} {0:d}".format(x, y, z))

# {1:d} -> y -> 20
# {2:d} -> z -> 30
# {0:d} -> x -> 10

# Output:
# Hello 20 30 10


# ------------------------------------------------------------
# ReArrange Numbers and Convert Them to Float
# ------------------------------------------------------------

print("Hello {2:f} {0:f} {1:f}".format(x, y, z))

# {2:f} -> 30.000000
# {0:f} -> 10.000000
# {1:f} -> 20.000000

# Output:
# Hello 30.000000 10.000000 20.000000


# ------------------------------------------------------------
# Control Floating Point Precision While Rearranging
# ------------------------------------------------------------

print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# {2:.2f}
# index 2 = z = 30
# show 2 digits after decimal
# -> 30.00

# {0:.4f}
# index 0 = x = 10
# show 4 digits after decimal
# -> 10.0000

# {1:.5f}
# index 1 = y = 20
# show 5 digits after decimal
# -> 20.00000

# Output:
# Hello 30.00 10.0000 20.00000


# ============================================================
# 7) Format in Version 3.6+ => f-Strings
# ============================================================

# Starting from Python 3.6, we can use f-strings.
#
# Put the letter f before the string:
#
# f"..."
#
# Then put the variable directly inside {}.


myName = "Osama"
myAge = 36


# Without f before the string:
print("My Name is : {myName} and My Age is : {myAge}")

# Python treats {myName} and {myAge} as normal text.

# Output:
# My Name is : {myName} and My Age is : {myAge}


# With f-string:
print(f"My Name is : {myName} and My Age is : {myAge}")

# Python reads the variables inside {} and inserts their values.

# Output:
# My Name is : Osama and My Age is : 36


# ============================================================
# QUICK SUMMARY
# ============================================================

# .format()
# ---------
# Inserts values inside a string using {}.
#
# Example:
# "My Name is {}".format(name)


# {}
# --
# Normal placeholder.
#
# Example:
# "{} {}".format(name, age)


# {:s}
# ----
# Format value as String.
#
# Example:
# "{:s}".format(name)


# {:d}
# ----
# Format value as Integer.
#
# Example:
# "{:d}".format(age)


# {:f}
# ----
# Format value as Float.
# Default = 6 decimal places.
#
# Example:
# "{:f}".format(10)
#
# Output:
# 10.000000


# {:.2f}
# ------
# Control number of decimal places.
#
# Example:
# "{:.2f}".format(10)
#
# Output:
# 10.00


# {:.5s}
# ------
# Truncate a string to maximum 5 characters.
#
# Example:
# "{:.5s}".format("Hello World")
#
# Output:
# Hello


# {:,d}
# -----
# Add comma separators to large numbers.
#
# Example:
# "{:,d}".format(500162350198)
#
# Output:
# 500,162,350,198


# {:_d}
# -----
# Add underscore separators.
#
# Example:
# "{:_d}".format(500162350198)
#
# Output:
# 500_162_350_198


# {0} {1} {2}
# -----------
# Control / rearrange the order of values.
#
# Example:
# "{2} {0} {1}".format("One", "Two", "Three")
#
# Output:
# Three One Two


# {2:.2f}
# --------
# 2  -> index of the value
# .2 -> number of decimal places
# f  -> Float
#
# Example:
# "{2:.2f}".format(10, 20, 30)
#
# Output:
# 30.00


# f-Strings
# ---------
# Available from Python 3.6+
# Put f before the string and write variables directly inside {}.
#
# Example:
#
# name = "Osama"
# age = 36
#
# print(f"My Name is {name} and My Age is {age}")
#
# Output:
# My Name is Osama and My Age is 36