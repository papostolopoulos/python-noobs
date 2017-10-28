# Test2 - Function to capitalize and count name characters #
# Change last week's program (test2.py) and make a function
# capitalizeAndCount(first_name, last_name) that return two values:
# capitalized first and last name, and count of letters.
# Then ask first and last name as before, call your function and print the results as before.

first_name = raw_input("What is your first name? ")
last_name = raw_input("What is your last name? ")

def capitalizeAndCount(first, last):
    fullName = first + " " + last
    nameLength = len(fullName) - 1
    return fullName.upper(), str(nameLength)


print "Your name (%s) has %s letters" %capitalizeAndCount(first_name, last_name)
print "Your name (" + capitalizeAndCount(first_name, last_name)[0] + ") has " + capitalizeAndCount(first_name, last_name)[1] + " letters"
