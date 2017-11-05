# Exercise 35: Branches and Functions
print "---EXERCISE 35: BRANCHES AND FUNCTIONS"

from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    abc = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()[]{,.<>}/?|"

    next = raw_input("> ")
    for item in next:
        if item.lower() in abc:
            dead("Man, learn to type a number.")

    how_much = int(next)

    # if "0" in next or "1" in next:
    #     how_much = int(next)
    # else:
    #     dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy. you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    print """
    1. Take the honey
    2. Taunt the bear
    3. Try to open the door
    """
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "1":
            dead("The bear looks at you then slaps your face off.")
        elif next == "2" and not bear_moved:
            print "The bear has moved from the door. You can go through it now. What do you do next?"
            print """
            1. Take the honey
            2. Taunt the bear
            3. Try to open the door
            """
            bear_moved = True
        elif next == "2" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "3" and not bear_moved:
            dead("The bear bites your head off.")
        elif next == "3" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means. Try again. What do you do?"
            print """
            1. Take the honey
            2. Taunt the bear
            3. Try to open the door
            """


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "he, it, whatever stares at you and you go insane."
    print """Do you:
    1. flee for your life or
    2. eat your head?"""
    next = raw_input("> ")

    if "1" in next:
        start()
    elif "2" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "You lost."
    exit(0)


def start():
    print """You are in a dark room.
    There is a door to your right and left.
    Which one do you take?
    """

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
