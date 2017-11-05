# Test - Print line numbers (II) #
# Revisit your test from Week 3 and do the same thing
# for all the lines in the input file.
# Edit the same file test3.py to make your changes.

#Not sure I understand what the request is. This is what I had written last week

from sys import argv
from os.path import exists

script, original_file, end_file = argv

def write_content(scrpt, original, end):
    start_file = open(original, "r")
    target_file = open(end, "w")

    for x in range(1, 7):
        target_file.write(str(x) + " - " + start_file.readline())


write_content(script, original_file, end_file)
