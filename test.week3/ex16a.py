# Exercise 16a: Reading And Writing Files
print "--- EXERCISE 16a: READING AND WRITING FILES ---"

print "I am going to open and read the contents of a file"
from sys import argv
script, filename = argv

print "I am going to print the file: %r" % filename
# open_file = open(filename)
# print(open_file.read())
print(open(filename, "r").read())

print "Now I am going to close the file"
# open_file.close()
