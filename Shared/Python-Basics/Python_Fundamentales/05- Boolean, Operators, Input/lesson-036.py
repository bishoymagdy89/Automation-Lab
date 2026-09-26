# ============================================================
# Lesson 036 - Comparison Operators
# ============================================================

# Comparison Operators compare two values.
# The result is always a Boolean value:
# True or False


# Main Comparison Operators:
#
# ==   Equal
# !=   Not Equal
# >    Greater Than
# <    Less Than
# >=   Greater Than or Equal
# <=   Less Than or Equal


# ============================================================
# Equal ==
# ============================================================

print(100 == 100)
# Output:
# True

print(100 == 200)
# Output:
# False

print(100 == 100.00)
# Output:
# True


# Important:
#
# =   -> Assignment Operator
# ==  -> Comparison Operator
#
# x = 100
# Means: assign 100 to x
#
# x == 100
# Means: is x equal to 100?


# ============================================================
# Not Equal !=
# ============================================================

print(100 != 100)
# Output:
# False

print(100 != 200)
# Output:
# True

print(100 != 100.00)
# Output:
# False


# != asks:
# "Are these two values different?"


# ============================================================
# Greater Than >
# ============================================================

print(100 > 100)
# Output:
# False

print(100 > 200)
# Output:
# False

print(100 > 100.00)
# Output:
# False

print(100 > 40)
# Output:
# True


# > means the left value must be strictly greater.
#
# 100 > 100 is False
# because they are equal, not greater.


# ============================================================
# Less Than <
# ============================================================

print(100 < 100)
# Output:
# False

print(100 < 200)
# Output:
# True

print(100 < 100.00)
# Output:
# False

print(100 < 40)
# Output:
# False


# < means the left value must be strictly smaller.


# ============================================================
# Greater Than or Equal >=
# ============================================================

print(100 >= 100)
# Output:
# True

print(100 >= 200)
# Output:
# False

print(100 >= 100.00)
# Output:
# True

print(100 >= 40)
# Output:
# True


# >= accepts TWO possibilities:
#
# Greater Than OR Equal
#
# So:
# 100 > 100   -> False
# 100 >= 100  -> True


# ============================================================
# Less Than or Equal <=
# ============================================================

print(100 <= 100)
# Output:
# True

print(100 <= 200)
# Output:
# True

print(100 <= 100.00)
# Output:
# True

print(100 <= 40)
# Output:
# False


# <= accepts TWO possibilities:
#
# Less Than OR Equal


# ============================================================
# Integer and Float Comparison
# ============================================================

print(100 == 100.00)
# Output:
# True

# Python compares their numeric values here.
# Although:
#
# 100      -> int
# 100.00   -> float
#
# Their numeric values are equal.


# ============================================================
# Simple Network Automation Example
# ============================================================

latency = 85
latency_limit = 100

print(latency <= latency_limit)

# Output:
# True

# Meaning:
# The current latency is within the allowed limit.


packet_loss = 7
packet_loss_limit = 5

print(packet_loss > packet_loss_limit)

# Output:
# True

# Meaning:
# Packet loss exceeded the allowed threshold.


# ============================================================
# Quick Summary
# ============================================================

# ==   -> Equal
# !=   -> Not Equal
# >    -> Greater Than
# <    -> Less Than
# >=   -> Greater Than or Equal
# <=   -> Less Than or Equal


# Comparison Operators always return:
#
# True
# or
# False


# ============================================================
# Most Important Points
# ============================================================

# 1. = is assignment
#    == is comparison
#
# 2. > and < do NOT include equality.
#
# 3. >= and <= DO include equality.
#
# 4. Comparison results are Boolean:
#    True or False.
#
# 5. 100 == 100.00 -> True
#    because their numeric values are equal.