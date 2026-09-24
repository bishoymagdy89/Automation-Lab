# ============================================================
# Lesson 035 - Assignment Operators
# ============================================================

# Assignment Operators are used to:
# Assign values to variables
# and update existing variable values.


# Main Assignment Operators:
#
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=


# ============================================================
# Basic Assignment =
# ============================================================

x = 10
y = 20

# = assigns a value to a variable.

z = x + y

print(z)

# 10 + 20 = 30
#
# Output:
# 30


# ============================================================
# Updating a Variable
# ============================================================

x = 10
y = 20

x = x + y

print(x)

# x = 10 + 20
# x = 30
#
# Output:
# 30


# ============================================================
# += Assignment Operator
# ============================================================

# Instead of writing:
#
# x = x + y
#
# We can write:
#
# x += y


x = 10
y = 20

x += y

print(x)

# Same as:
# x = x + y
#
# 10 + 20 = 30
#
# Output:
# 30


# ============================================================
# -= Assignment Operator
# ============================================================

x = 10
y = 20

x -= y

print(x)

# Same as:
# x = x - y
#
# 10 - 20 = -10
#
# Output:
# -10


# ============================================================
# Other Assignment Operators
# ============================================================

# *=
# x *= y
#
# Same as:
# x = x * y


# /=
# x /= y
#
# Same as:
# x = x / y


# **=
# x **= y
#
# Same as:
# x = x ** y


# %=
# x %= y
#
# Same as:
# x = x % y


# //=
# x //= y
#
# Same as:
# x = x // y


# ============================================================
# General Rule
# ============================================================

# Long Way:
#
# variable = variable [operator] value


# Short Way:
#
# variable [operator]= value


# Examples:
#
# x = x + 5    ->    x += 5
# x = x - 5    ->    x -= 5
# x = x * 5    ->    x *= 5
# x = x / 5    ->    x /= 5
# x = x ** 5   ->    x **= 5
# x = x % 5    ->    x %= 5
# x = x // 5   ->    x //= 5


# ============================================================
# Simple Network Automation Example
# ============================================================

failed_attempts = 0

failed_attempts += 1
failed_attempts += 1
failed_attempts += 1

print(failed_attempts)

# Output:
# 3

# Every failed connection increases the counter by 1.
#
# Instead of:
# failed_attempts = failed_attempts + 1
#
# We use:
# failed_attempts += 1


# ============================================================
# Quick Summary
# ============================================================

# =    -> Assign a value
# +=   -> Add and assign
# -=   -> Subtract and assign
# *=   -> Multiply and assign
# /=   -> Divide and assign
# **=  -> Power and assign
# %=   -> Modulus and assign
# //=  -> Floor divide and assign


# Most Important Idea:
#
# x += y
#
# is just a shorter way of writing:
#
# x = x + y
#
# The same idea applies to the other Assignment Operators.