#Exercise 15: Reading files
print "--- EXERCISE 15: READING FILES ---"

#Import the arguments from command line
from sys import argv

#Define two parameters, one where the script resides
#and one that relates to the file where the content comes from
script, filename = argv

#Define variable that opens the filename
txt = open(filename)

print "Here's your file %r:" % filename

#Read the file and print the content
print txt.read()

print "Type the filename again:"

#Enter again the name of the file (or any file)
file_again = raw_input("> ")

#Define variable and open the file
txt_again = open(file_again)

#Read the content of the file
print txt_again.read()

txt_again.close()
