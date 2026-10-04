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


# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10 + 9j)
print(int(10 + 9j))  # Error: Cannot Convert Complex To Int