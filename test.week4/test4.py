# Test - count words #
# Write function that returns the number of words in a string.
# Save it in a file called test4.py and push it with sourcetree.

def countWords(str):
    if len(str) == 0:
        return 0
    result = 1;
    for letter in str:
        if letter == " ":
            result += 1
    return result


def word_counter_program():
    print "Let's count the words you will enter."
    user_input = raw_input("Please enter your sentence here: ")
    print "The sentence: \"" + user_input + "\" has " + str(countWords(user_input)) + " words."

word_counter_program()
