# ============================================================
# Lesson 033 - Boolean
# ============================================================

# Boolean has only two values:
# True
# False
#
# بنستخدمهم علشان نعرف هل condition معين متحقق ولا لأ.


# ============================================================
# Boolean Result From Methods
# ============================================================

name = ""

print(name.isspace())

# Output:
# False

# isspace() checks if the String contains ONLY spaces.
# هنا الـ String فاضي تماماً، لذلك النتيجة False.


name = " "

print(name.isspace())

# Output:
# True

# هنا فيه Space فعلاً، لذلك النتيجة True.


# ============================================================
# Boolean Result From Comparisons
# ============================================================

print(100 > 200)

# Output:
# False
# 100 is NOT greater than 200


print(100 > 100)

# Output:
# False
# 100 is equal to 100, not greater than it


print(100 > 90)

# Output:
# True
# 100 is greater than 90


# ============================================================
# bool()
# ============================================================

# bool() tells us whether a value is considered:
# True or False


# ============================================================
# True Values
# ============================================================

# بشكل عام:
# أي Value فيها Data تعتبر True.


print(bool("Osama"))

# Output:
# True
# Non-empty String


print(bool(100))

# Output:
# True
# Non-zero Integer


print(bool(100.95))

# Output:
# True
# Non-zero Float


print(bool(True))

# Output:
# True


print(bool([1, 2, 3, 4, 5]))

# Output:
# True
# Non-empty List


# Examples:

print(bool("Fortinet"))
# True

print(bool(-10))
# True

print(bool({"hostname": "FGT-01"}))
# True


# IMPORTANT:
# حتى الـ Negative Number يعتبر True
# طالما الرقم مش Zero.

print(bool(-1))

# Output:
# True


# ============================================================
# False Values
# ============================================================

# أشهر القيم اللي Python تعتبرها False:


print(bool(0))

# Output:
# False
# Zero


print(bool(""))

# Output:
# False
# Empty String


print(bool(''))

# Output:
# False
# Empty String


print(bool([]))

# Output:
# False
# Empty List


print(bool(False))

# Output:
# False


print(bool(()))

# Output:
# False
# Empty Tuple


print(bool({}))

# Output:
# False
# Empty Dictionary


print(bool(None))

# Output:
# False


# ============================================================
# Important Difference
# ============================================================

print(bool(""))

# False
# Empty String


print(bool(" "))

# True
# String contains one Space


# مهم جداً:
#
# ""  = Empty String       -> False
# " " = String with Space  -> True


# ============================================================
# Network Automation Example
# ============================================================

device_ip = "10.0.0.1"

print(bool(device_ip))

# Output:
# True


# لأن الـ variable يحتوي على قيمة.


device_ip = ""

print(bool(device_ip))

# Output:
# False


# وده هيفيدنا جداً بعدين مع if:

device_ip = "10.0.0.1"

if device_ip:
    print("Device IP exists")

# Output:
# Device IP exists


# Python هنا تقريباً بتعمل:
#
# if bool(device_ip):
#
# وبما إن:
#
# bool("10.0.0.1") -> True
#
# فالـ code يشتغل.


# ============================================================
# Quick Summary
# ============================================================

# Boolean:
#
# True
# False


# Comparisons return Boolean values:
#
# 100 > 90   -> True
# 100 > 200  -> False


# True Values:
#
# bool("Osama")       -> True
# bool(100)           -> True
# bool(100.95)        -> True
# bool(-1)            -> True
# bool([1, 2, 3])     -> True


# False Values:
#
# bool(0)       -> False
# bool("")      -> False
# bool([])      -> False
# bool(())      -> False
# bool({})      -> False
# bool(False)   -> False
# bool(None)    -> False


# Easy Rule:
#
# Empty / Zero / None  -> False
# Most other values    -> True