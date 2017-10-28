#Exercise 17: More Files
print "--- EXERCISE 17: MORE FILES ---"

# Short version
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
in_file = open(from_file).read()

print "The input file is %d bytes long" %len(in_file)
print "Does the output file exist? %r" % exists(to_file)

out_file = open(to_file, 'w').write(in_file)

print "Alright, all done."
out_file.close()


#Longer version
# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print "Copying from %s to %s" % (from_file, to_file)
#
# in_file = open(from_file)
# indata = in_file.read()
# # we could do these two on one line too, how?
#
# print "The input file is %d bytes long" %len(in_file)
# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()
#
# out_file = open(to_file, 'w')
# out_file.write(in_file)
#
# print "Alright, all done."
# out_file.close()
# in_file.close()
