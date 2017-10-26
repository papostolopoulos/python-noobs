#  Test #
# Write a program (test2.py) that asks your first name,
# then asks your last name, then prints your full name
# in capital letters and the number of letters in your name
# in the following fashion:
#
# What is your first name? Joe
# What is your last name? Smith
# Your name (JOE SMITH) has 8 letters.
# You will need the function that returns the length of a string: len.
# You can use it like this: variable = len(string).

firstName = raw_input("What is your first name?")
lastName = raw_input("What is your last name?")
fullName = firstName + " " + lastName
nameLength = len(fullName) - 1
print("Your name (" + fullName.upper() + ") has " + str(nameLength) + " letters")
