# --------------------
# -- User Input --
# --------------------

# input() allows the user to enter data during program execution.
# The input() function always returns a string (str).

input("Hello Python")

# Output:
# Hello Python dfdfdf


# ---------------------------------
# Store User Input in Variables
# ---------------------------------

fName = input("What's Is Your First Name? ")
mName = input("What's Is Your Middle Name? ")
lName = input("What's Is Your Last Name? ")

# Display the full name using an f-string.

print(f"Hello {fName} {mName} {lName} Happy To See You.")


# ---------------------------------
# Remove Extra Spaces Using strip()
# ---------------------------------

# strip() removes leading and trailing spaces.

fName = fName.strip()
mName = mName.strip()
lName = lName.strip()

print(f"Hello {fName} {mName} {lName} Happy To See You.")


# ---------------------------------
# Method Chaining: strip() + capitalize()
# ---------------------------------

# strip() removes extra spaces from both ends.
# capitalize() makes the first character uppercase
# and converts the remaining characters to lowercase.

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName} {lName} Happy To See You.")

# Example Input:
# First Name: oSaMA
# Middle Name: mOHaMED
# Last Name: ELSAYED

# Output:
# Hello Osama Mohamed Elsayed Happy To See You.


# ---------------------------------
# Display Only the First Character
# ---------------------------------

# :.1s displays only the first character of a string.
# Useful for displaying the middle name as an initial.

print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")

# Output:
# Hello Osama M Elsayed Happy To See You.