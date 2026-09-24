# ============================================================
# Lesson 034 - Boolean Operators
# ============================================================

# Boolean Operators:
#
# and
# or
# not
#
# بنستخدمهم لما يكون عندنا أكثر من Condition
# وعايزين نربطهم ببعض.


age = 36
country = "Egypt"
rank = 10


# ============================================================
# and
# ============================================================

# and means:
# ALL conditions must be True.
#
# لو Condition واحد فقط False
# النتيجة كلها تصبح False.


print(age > 16 and country == "Egypt" and rank > 0)

# True and True and True
#
# Output:
# True


print(age > 16 and country == "KSA" and rank > 0)

# True and False and True
#
# Output:
# False


# Easy Rule:
#
# True  and True  -> True
# True  and False -> False
# False and True  -> False
# False and False -> False
#
# AND = كل الشروط لازم تتحقق.


# ============================================================
# or
# ============================================================

# or means:
# At least ONE condition must be True.
#
# مش لازم كل الشروط تتحقق.
# Condition واحد True كفاية.


print(age > 40 or country == "KSA" or rank > 20)

# False or False or False
#
# Output:
# False


print(age > 40 or country == "Egypt" or rank > 20)

# False or True or False
#
# Output:
# True


# Easy Rule:
#
# True  or True  -> True
# True  or False -> True
# False or True  -> True
# False or False -> False
#
# OR = شرط واحد True كفاية.


# ============================================================
# not
# ============================================================

# not reverses the Boolean result.
#
# True  -> False
# False -> True


print(age > 16)

# 36 > 16
#
# Output:
# True


print(not age > 16)

# age > 16 = True
# not True = False
#
# Output:
# False


print(not country == "KSA")

# country == "KSA" -> False
# not False         -> True
#
# Output:
# True


# ============================================================
# Network Automation Example
# ============================================================

device_reachable = True
credentials_valid = True

print(device_reachable and credentials_valid)

# Output:
# True
#
# الجهاز Reachable والـ Credentials صحيحة.
# إذن نقدر نكمل الـ automation.


device_reachable = True
credentials_valid = False

print(device_reachable and credentials_valid)

# Output:
# False
#
# AND تحتاج الاثنين True.


# Another Example:

primary_link_up = False
backup_link_up = True

print(primary_link_up or backup_link_up)

# Output:
# True
#
# طالما واحد من الـ links شغال
# فالـ OR ترجع True.


# ============================================================
# Quick Summary
# ============================================================

# and
# ----
# ALL conditions must be True.
#
# True and True  -> True
# True and False -> False


# or
# ---
# At least ONE condition must be True.
#
# False or True  -> True
# False or False -> False


# not
# ---
# Reverses the result.
#
# not True  -> False
# not False -> True


# Easy Memory:
#
# AND = كلهم
# OR  = واحد على الأقل
# NOT = العكس