# -----------------------------------
# -- Arithmetic Operators
# -----------------------------------


# =========================
# Arithmetic Operators
# =========================
# Arithmetic operators are used to perform mathematical operations.

# [+]  Addition
# [-]  Subtraction
# [*]  Multiplication
# [/]  Division
# [%]  Modulus
# [**] Exponent
# [//] Floor Division


# =========================
# Addition +
# =========================
# Adds numbers together.

print(10 + 30)     # 40
print(-10 + 20)    # 10
print(1 + 2.66)    # 3.66
print(1.2 + 1.2)   # 2.4

# int + int     -> int
# int + float   -> float
# float + float -> float


# =========================
# Subtraction -
# =========================
# Subtracts the second number from the first number.

print(60 - 30)      # 30
print(-30 - 20)     # -50
print(-30 - -20)    # -10
print(5.66 - 3.44)  # 2.22

# Important:
# -30 - -20
#
# Subtracting a negative number is like adding:
# -30 + 20 = -10


# =========================
# Multiplication *
# =========================
# Multiplies numbers together.

print(10 * 3)          # 30
print(5 + 10 * 100)    # 1005
print((5 + 10) * 100)  # 1500


# =========================
# Operator Priority
# =========================
# Python follows mathematical operator precedence.
#
# Multiplication happens BEFORE Addition.

print(5 + 10 * 100)
# 10 * 100 = 1000
# 1000 + 5 = 1005


# Parentheses () have higher priority.

print((5 + 10) * 100)
# 5 + 10 = 15
# 15 * 100 = 1500


# =========================
# Division /
# =========================
# Divides one number by another.
#
# Normal division / returns a Float.

print(100 / 20)       # 5.0

# Even though the mathematical answer is 5,
# Python returns 5.0 because / returns a Float.


# We can convert the result to Integer using int().

print(int(100 / 20))  # 5


# =========================
# Modulus %
# =========================
# Returns the REMAINDER after division.

print(8 % 2)   # 0
print(9 % 2)   # 1
print(20 % 5)  # 0
print(22 % 5)  # 2


# Example:
# 22 / 5
#
# 5 * 4 = 20
# Remaining = 2
#
# Therefore:
# 22 % 5 = 2


# =========================
# Useful Modulus Example
# =========================
# Modulus can be used to check
# whether a number is Even or Odd.

print(10 % 2)  # 0 -> Even
print(11 % 2)  # 1 -> Odd

# If number % 2 == 0 -> Even
# If number % 2 != 0 -> Odd


# =========================
# Exponent **
# =========================
# Exponent means raising a number to a power.

print(2 ** 5)  # 32

# 2 ** 5 means:
# 2 * 2 * 2 * 2 * 2
#
# Result = 32

print(2 * 2 * 2 * 2 * 2)  # 32


print(5 ** 4)  # 625

# 5 ** 4 means:
# 5 * 5 * 5 * 5
#
# Result = 625

print(5 * 5 * 5 * 5)  # 625


# Important:
# ** does NOT mean normal multiplication.
#
# *  -> Multiplication
# ** -> Exponent / Power


# =========================
# Floor Division //
# =========================
# Floor Division performs division
# and rounds the result DOWN to the lower integer.

print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7


# Example:
#
# Normal Division:
# 119 / 20 = 5.95
#
# Floor Division:
# 119 // 20 = 5
#
# It removes the fractional part
# by flooring the result.


# =========================
# Division vs Floor Division
# =========================

print(119 / 20)   # 5.95
print(119 // 20)  # 5

# /  -> Normal Division
# // -> Floor Division


# =========================
# Quick Summary
# =========================

# +  -> Addition
# -  -> Subtraction
# *  -> Multiplication
# /  -> Division
# %  -> Remainder after Division
# ** -> Exponent / Power
# // -> Floor Division
#
#
# Examples:
#
# 10 + 5  -> 15
# 10 - 5  -> 5
# 10 * 5  -> 50
#
# 10 / 5  -> 2.0
#
# 22 % 5  -> 2
# Remainder = 2
#
# 2 ** 5  -> 32
# Same as: 2 * 2 * 2 * 2 * 2
#
# 119 / 20  -> 5.95
# 119 // 20 -> 5
#
#
# Important:
#
# / always performs normal Division.
#
# % gives the REMAINDER.
#
# ** means Power / Exponent.
#
# // means Floor Division.
#
# () can be used to control
# the order of mathematical operations.