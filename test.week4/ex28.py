# Exercise 28: Boolean Practice
print "---EXERCISE 28: BOOLEAN PRACTICE---"



boolean_list = [
["True and True", True and True],
["False and True", False and True],
['1==1 and 2==1', 1==1 and 2==1],
['"test" == "test"', "test" == "test"],
['1==1 or 2!=1', 1==1 or 2!=1],
['True and 1==1', True and 1==1],
['False and 0 != 0', False and 0 != 0],
['True or 1==1', True or 1==1],
['"test" == "testing"', "test" == "testing"],
['1!=0 and 2==1', 1!=0 and 2==1],
['"test" != "testing"', "test" != "testing"],
['"test" == 1', "test" == 1],
['not (True and False)', not (True and False)],
['not (1==1 and 0!=1)', not (1==1 and 0!=1)],
['not (10 == 1 or 1000 == 1000)', not (10 == 1 or 1000 == 1000)],
['not (1!=10 or 3==4)', not (1!=10 or 3==4)],
['not ("testing" == "testing" and "Zed" == "Cool Guy")', not ("testing" == "testing" and "Zed" == "Cool Guy")],
['1==1 and not ("testing"==1or1==0)', 1==1 and not ("testing"==1 or 1==0)],
['"chunky" == "bacon" and not (3 == 4 or 3 == 3)', "chunky" == "bacon" and not (3 == 4 or 3 == 3)],
['3 == 3 and not ("testing" == "testing" or "Python" == "Fun")', 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")]
]

def boolean_test(compare_list):
    print "Hello there. Let's do some boolean practice. This test has %s questions. Good luck!" % len(compare_list)
    print ""
    final_score = 0

    x = 0
    while(x < len(compare_list)):
        question = raw_input("Question " + str(x + 1) + ": What is the value for " + str(compare_list[x][0]) + "? ")
        user_answer = question.lower().capitalize()
        print user_answer
        if(user_answer == str(compare_list[x][1])):
            print "That is correct! " + compare_list[x][0] + " has a boolean value of " + str(compare_list[x][1]) + "\n"
            final_score += 1
            x += 1
        elif(user_answer == "False" and str(compare_list[x][1]) == "True" or user_answer == "True" and str(compare_list[x][1]) == "False"):
            print "Sorry, that is incorrect. " + compare_list[x][0] + " has a boolean value of " + str(compare_list[x][1]) + "\n"
            x += 1
        else:
            print "Sorry, you enter something other than \"True\"or \"False\". Please try again"

    print "Out of the " + str(len(compare_list)) + " questions, you got " + str(final_score) + " correct! \nThanks for playing!"


boolean_test(boolean_list)

# x = raw_input("")
# print x
# print type(bool(x))

# 1. True and True
# 2. False and True
# 3. 1==1and2==1
# 4. "test" == "test"
# 5. 1==1or2!=1
# 6. Trueand1==1
# 7. False and 0 != 0
# 8. Trueor1==1
# 9. "test" == "testing"
# 10. 1!=0and2==1
# 11. "test" != "testing"
# 12. "test" == 1
# 13. not (True and False)
# 14. not(1==1and0!=1)
# 15. not (10 == 1 or 1000 == 1000)
# 16. not(1!=10or3==4)
# 17. not ("testing" == "testing" and "Zed" == "Cool Guy")
# 18. 1==1andnot("testing"==1or1==0)
# 19. "chunky" == "bacon" and not (3 == 4 or 3 == 3)
# 20. 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
