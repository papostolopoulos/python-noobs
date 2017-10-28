# Test - Print line numbers #
# Write a program that reads a given file and
# write another file with the same lines as the first file,
# but adds the line number at the beginning of each line, and a dash.
# Do this for the first 6 lines. Save your program with the name test3.py
#
# You will need to use the function readline() to read a single line of the file.

from sys import argv
from os.path import exists

script, original_file, end_file = argv

def write_content(scrpt, original, end):
    start_file = open(original, "r")
    target_file = open(end, "w")

    for x in range(1, 7):
        target_file.write(str(x) + " - " + start_file.readline())


write_content(script, original_file, end_file)

#
# start_file = open(original_file, "r")
# target_file = open(end_file, "w")
#
# for x in range(1, 7):
#     target_file.write(str(x) + " - " + start_file.readline())
