# Antonio Rios
# Lab 2 - Gamebook
# September 10, 2014
####################################


# Introduction to the game
print("Anakin and Obi-wan are fighting on Mustafar.")
print("Eventually, they end up at a pivotal point \n\
in the fight and master Kenobi gains the high ground.")
print("Anakin becomes greatly vexed by the jedi scum.")
print("There, Anakin needs to make a choice of what to do.")
print()

# First decision point
choice = input("Does Anakin try to jump OVER or to the SIDE of Obi-wan?")

if choice == "OVER" or choice == "over":
    print("Obi-wan cuts his limbs.")
    print("Anakin becomes the cyborg, Darth Vader.")
    print("Padme dies in the emergency room after giving birth.")
    print("Episode 4,5 and 6 occur.")
    print("George Lucas replaces the original Darth Vader \n\
with Hayden Christensen in episode 6.")
    print("The fans are angry with the decision.")

    # Nested decision point
    choice = input("Do they PROTEST or HUSH about it? ")

    if choice == "PROTEST" or choice == "protest":
        print()
        print("The hardcore fans protest about Hayden.")
        print("They find more things to protest about.")
        print("They protest about Jar Jar Binks.")
        print("George Lucas sells LucasArts to Disney.")
        print("Episode 7, 8 and 9 will come out after 2015.")

    elif choice == "HUSH" or choice == "hush":
        print()
        print("No one says anything.")
        print("LucasArts continues to make low quality video games.")
        print("All the LucasArts fans buy them all for no reason.")
        print("Star Trek becomes more popular.")

elif choice == "SIDE" or choice == "side":
    print("Anakin jumps to the side and continues the fight.")
    print("After a long strenuous battle, Anakin gets the upper hand.")
    print("He swiftly defeats Obi-wan.")
    print("He then returns to Darth Sidious.")
    print("Darth Sidious offers Anakin to rule the galaxy together.")
    print()

    # second nested decision point
    choice = input("Does Anakin rule WITH Darth Sidious or ALONE?")

    if choice == "WITH" or choice == "with":
        print("Anakin keeps his limbs and rules the galaxy together.")
        print("He also gets to see his family.")
        print("Padme is in the emergency room with the twins.")
        print("But his family is enslaved by the emperor.")

    elif choice == "ALONE" or choice == "alone":
        print("Anakin kills the emperor and rules alone.")
        print("He gets to see his family.")
        print("Anakin visits Padme in the emergency room.")
        print("There, he finds her with twin babies, his children.")
        print("He claims the throne to the galaxy, but has a problem.")
        print("He only wants one heir to his throne.")
        print()

        choice = input("Does he keep LUKE or LEIA or BOTH? ")

        # third nested decision point
        if choice == "LUKE" or choice == "luke":
            print()
            print("He exiles Leia to a farming family.")
            print("There she lived happily.")
            print("Luke became the next emperor.")
            print("There was peace and order in the galaxy.")

        elif choice == "LEIA" or choice == "leia":
            print()
            print("Luke is exile to a farming family.")
            print("There he lived unfulfilled.")
            print("He joins the rebels and organizes a revolution.")
            print()

            # Numeric decision point
            matches = int(input("How many years does he \
train with Yoda."))

            if matches < 5:
                print()
                print("He fails and dies.")
                print("Leia becomes the empress.")
                print("The rebelion is crushed.")
                print("Peace and order returns to the galaxy.")

            elif matches >= 5:
                print()
                print("Luke breaches the inner walls of the Death Star.")
                print("There he has a duel with Darth Vader.")
                print("Darth Vader tells him he is his father.")
                print("It's a trap.")
                print("Darth Vader and Luke keep fighting.")
                print("Luke and Vader continue the fight for the galaxy.")

        elif choice == "BOTH" or choice == "both":
            print("The siblings enjoy a royal life.")
            print("There is peace and order in the galaxy.")
            print("Until they grow up and become greedy for the throne.")
            print("Luke claims the throne because he is male.")
            print("Leia has to marry into a different family.")
