# =========================
# -- Numbers --
# =========================

# Integer
# أرقام صحيحة بدون decimal point

print(type(1))      # <class 'int'>
print(type(100))    # <class 'int'>
print(type(10))     # <class 'int'>
print(type(-10))    # <class 'int'>
print(type(-110))   # <class 'int'>


# Float
# أرقام تحتوي على decimal point

print(type(1.500))   # <class 'float'>
print(type(100.99))  # <class 'float'>
print(type(-10.99))  # <class 'float'>
print(type(0.99))    # <class 'float'>
print(type(-0.99))   # <class 'float'>


# Complex
# Complex Number = Real Part + Imaginary Part

myComplexNumber = 5 + 6j

print(type(myComplexNumber))  # <class 'complex'>

print("Real Part Is: {}".format(myComplexNumber.real))
# Real Part Is: 5.0

print("Imaginary Part Is: {}".format(myComplexNumber.imag))
# Imaginary Part Is: 6.0