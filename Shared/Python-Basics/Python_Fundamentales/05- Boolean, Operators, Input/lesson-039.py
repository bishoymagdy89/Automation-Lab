# -----------------------------------
# -- Lesson 039: Practical Slice Email
# -----------------------------------

# Practical application of Indexing, Slicing, and String Methods
# Extract the username and website from an email address.


# -----------------------------------
# -- 1. Basic Indexing
# -----------------------------------

email = "Osama@elzero.org"

print(email[0])  # O => Get the first character (Index 0)


# -----------------------------------
# -- 2. Basic Slicing
# -----------------------------------

email = "Osama@elzero.org"

print(email[0:5])  # Osama => Get characters from Index 0 to 4

# Slicing Syntax: [Start:End]
# Start => Included
# End   => Excluded


# -----------------------------------
# -- 3. Find Character Position Using index()
# -----------------------------------

email = "Osama_Elzero@elzero.org"

print(email.index("@"))  # 12

# index("@") => Returns the position of the @ character
# Useful when the username length is not fixed


# -----------------------------------
# -- 4. Extract Username Using Slicing + index()
# -----------------------------------

email = "Osama_Elzero@elzero.org"

print(email[0:email.index("@")])  # Osama_Elzero

# Start from Index 0
# Stop before the @ character
# The @ character is excluded from the result

# Shorter version:
print(email[:email.index("@")])  # Osama_Elzero


# -----------------------------------
# -- 5. Get User Input
# -----------------------------------

theName = input("What's Your Name ?")
theEmail = input("What's Your Email ?")

print(f"Hello {theName} Your Email Is {theEmail}")

# input() => Gets data from the user
# f-string => Inserts variables directly inside a string


# -----------------------------------
# -- 6. Extract Username From User Email
# -----------------------------------

theName = input("What's Your Name ?")
theEmail = input("What's Your Email ?")

theUsername = theEmail[:theEmail.index("@")]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} and Your Website Is ")

# Example Input:
# Name  => Osama
# Email => osama@elzero.org

# Output:
# Hello Osama Your Email Is osama@elzero.org
# Your Username Is osama and Your Website Is


# -----------------------------------
# -- 7. Extract Website From Email
# -----------------------------------

theEmail = "osama@elzero.org"

theUsername = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]

print(theUsername)  # osama
print(theWebsite)   # elzero.org

# Username:
# [:theEmail.index("@")]
# Extract everything before @

# Website:
# [theEmail.index("@") + 1:]
# Start immediately after @ and continue to the end

# +1 => Skips the @ character
# Empty End => Continue until the end of the string


# -----------------------------------
# -- 8. Clean User Input Using String Methods
# -----------------------------------

theName = input("What's Your Name ?").strip().capitalize()
theEmail = input("What's Your Email ?").strip()

# strip() => Removes leading and trailing spaces
# capitalize() => Makes the first character uppercase
#                 and the remaining characters lowercase

# Example:
# Name Input  => "   OSAMA   "
# Name Result => "Osama"

# Email Input  => "   Osama@Elzero.org   "
# Email Result => "Osama@Elzero.org"


# -----------------------------------
# -- 9. Final Practical Application
# -----------------------------------

theName = input("What's Your Name ?").strip().capitalize()
theEmail = input("What's Your Email ?").strip()

theUsername = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} and Your Website Is {theWebsite}")


# Example Input:
# What's Your Name ? OSAMA
# What's Your Email ? Osama@Elzero.org

# Output:
# Hello Osama Your Email Is Osama@Elzero.org
# Your Username Is Osama and Your Website Is Elzero.org


# -----------------------------------
# -- Quick Summary
# -----------------------------------

# [0]                   => Access the first character
# [0:5]                 => Extract characters from Index 0 to 4
# [:5]                  => Slice from the beginning to Index 4
# [5:]                  => Slice from Index 5 to the end
# index("@")            => Find the position of @
# [:email.index("@")]   => Extract the username before @
# [email.index("@")+1:] => Extract the domain after @
# input()               => Get input from the user
# strip()               => Remove spaces from both ends
# capitalize()          => Capitalize the first character
# f-string              => Format strings using variables

# Main Idea:
# Combine Slicing and index() to extract dynamic parts
# of a string without knowing their exact positions.