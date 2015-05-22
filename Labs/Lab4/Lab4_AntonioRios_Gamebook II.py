# Antonio Rios
# September 24, 2014
# CS126 Lab
# Lab 4- Gamebook II
# =============================


def intro_page():
    """ Introduces the story and prompts for the first decision"""

    print("It was a dark and stormy night in the city.")

    direction = input("Do you HAIL A CAB, STAY INSIDE, or go on a WALK? ")

    if direction.lower() == 'hail a cab':
        bad_outcome()

    elif direction.lower() == 'stay inside':
        good_outcome()

    elif direction.lower() == 'walk':
        death_page()


def bad_outcome():
    """ Second page with a bad outcome """

    print()
    print("You get in to the cab.")
    print("You notice something creepy about the driver.")
    print("The cab starts heading in the opposite direction you want.")

    print("Do you STOP the cab, TRUST the driver, or ")
    cab = input("tell the driver to go BACK? ")

    if cab.lower() == 'stop':
        print("The cab stops and the driver asks for his money.")
        print("Do you pay the driver more than five dollars ")
        print("or pay him less than five dollars?")

        payment = float(input("How much do you pay: "))

        if payment < 5:
            death_page()

        elif payment > 5:
            survival_page()

    elif cab.lower() == 'trust':
        print("You reluctanlty trust the driver and end up in the boonies")
        death_page()

    elif cab.lower() == 'back':
        detour_page()


def good_outcome():
    """This is the most survivable outcome."""

    print()
    print("You are home, alone at night watching tv.")
    print("All of the sudden the door bell rings.")
    print("You aren't expecting any guests, who is it?")

    answer = input("Do you ANSWER the door or NOT? ")

    if answer.lower() == 'answer':
        door_bell()

    elif answer.lower() == 'not':
        survival_page()


def door_bell():
    print("You have answered the door.")
    print("There is someone standing there with a machete and a mask.")
    print("He lunges at you.")

    action = input("Do you Freeze up or RUN away? ")

    if action.lower() == 'freeze':
        death_page()

    elif action.lower() == 'run':
        survival_page()


def detour_page():
    """ The user has chosen to detour back to home."""

    print()
    print("The cab stops and the driver asks for his money.")
    print("Do you pay the driver more than eight dollars ")
    print("or pay him less than eight dollars?")

    payment = float(input("How much do you pay: "))

    if payment < 8:
        death_page()

    elif payment > 8:
        good_outcome()


def death_page():
    """This is the loosing page where the user dies."""

    print()
    print("You die, a horrible death!")
    print("Would you like to try again?")

    answer = input("(Yes or No)")

    if answer.lower() == 'yes':
        intro_page()

    elif answer.lower() == 'no':
        print("GAME OVER")


def survival_page():
    """ This is the winning page where the user survives."""

    print()
    print("You manage to survive the night.")
    print("Good job! Would you like to try again?")

    answer = input("(Yes or No)")

    if answer.lower() == 'yes':
        intro_page()
    elif answer.lower() == 'no':
        print("GAME OVER")


intro_page()
