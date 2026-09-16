# -----------------------------------
# -- String Methods - Part 3
# -----------------------------------


# =========================
# index(SubString, Start, End)
# =========================
# Returns the index position of the substring.
# If the substring is NOT found, it raises an Error.

a = "I Love Python"

print(a.index("P"))        # 7
print(a.index("P", 0, 10)) # 7

# print(a.index("P", 0, 5))
# Error because "P" does not exist between index 0 and 5.


# =========================
# find(SubString, Start, End)
# =========================
# Same idea as index(), but if the substring is NOT found,
# it returns -1 instead of raising an Error.

b = "I Love Python"

print(b.find("P"))        # 7
print(b.find("P", 0, 10)) # 7
print(b.find("P", 0, 5))  # -1


# Important Difference:
# index() -> Not Found = Error
# find()  -> Not Found = -1


# =========================
# rjust(Width, Fill Character)
# =========================
# Makes the string reach a specific width.
# Adds characters to the LEFT side.

c = "Osama"

print(c.rjust(10))
# "     Osama"

print(c.rjust(10, "#"))
# "#####Osama"


# =========================
# ljust(Width, Fill Character)
# =========================
# Makes the string reach a specific width.
# Adds characters to the RIGHT side.

d = "Osama"

print(d.ljust(10))
# "Osama     "

print(d.ljust(10, "#"))
# "Osama#####"


# Quick Reminder:
# rjust() -> Fill LEFT
# ljust() -> Fill RIGHT


# =========================
# splitlines()
# =========================
# Splits a multi-line string into a List.
# Every line becomes one item.

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

# Output:
# ['First Line', 'Second Line', 'Third Line']


f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# Output:
# ['First Line', 'Second Line', 'Third Line']


# =========================
# expandtabs(TabSize)
# =========================
# Controls the spacing created by \t (Tab).

g = "Hello\tWorld\tI\tLove\tPython"

print(g.expandtabs(2))

# \t means Tab.
# expandtabs(2) sets tab stops every 2 positions.


# =========================
# istitle()
# =========================
# Checks whether the string follows Title Case rules.
# Returns True or False.

one = "I Love Python And 3G"
two = "I Love Python And 3g"

print(one.istitle())  # True
print(two.istitle())  # False

# 3G -> valid title-style cased part
# 3g -> lowercase letter after the number


# =========================
# isspace()
# =========================
# Checks if the string contains ONLY whitespace characters.
# Returns True or False.

three = " "
four = ""

print(three.isspace()) # True
print(four.isspace())  # False

# Space only -> True
# Empty string -> False


# =========================
# islower()
# =========================
# Checks if all cased letters are lowercase.
# Returns True or False.

five = "i love python"
six = "I Love Python"

print(five.islower()) # True
print(six.islower())  # False


# =========================
# isidentifier()
# =========================
# Checks if the string can be used as a valid Python identifier.
# Useful for checking valid variable/function/class names.

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier()) # True
print(eight.isidentifier()) # True
print(nine.isidentifier())  # False

# "_" is allowed.
# "-" is NOT allowed in Python identifiers.


# =========================
# isalpha()
# =========================
# Checks if the string contains ONLY alphabetic letters.
# No numbers, spaces, or symbols.

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"

print(x.isalpha()) # True
print(y.isalpha()) # False


# =========================
# isalnum()
# =========================
# Checks if the string contains ONLY:
# Letters + Numbers
#
# No spaces or special characters.

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"

print(u.isalnum()) # True
print(z.isalnum()) # True


# =========================
# Quick Summary
# =========================

# index()        -> Find position; Not Found = Error
# find()         -> Find position; Not Found = -1
#
# rjust()        -> Fill from LEFT
# ljust()        -> Fill from RIGHT
#
# splitlines()   -> Multi-line String -> List of lines
# expandtabs()   -> Control tab spacing
#
# istitle()      -> Check Title Case
# isspace()      -> Check whitespace only
# islower()      -> Check lowercase
# isidentifier() -> Check valid Python identifier
# isalpha()      -> Letters only
# isalnum()      -> Letters and/or numbers only