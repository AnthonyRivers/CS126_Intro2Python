# Antonio Rios
# September 7, 2014
# CS 126
# Lab 1: Madlib
######################################

# Declare variables and assign the user input
name = input("Enter a name: ")
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
second_name = input("Enter a second name: ")
second_adjective = input("Enter a second adjective: ")
second_noun = input("Enter a second noun: ")
verb = input("Enter a verb: ")
second_verb = input("Enter a present verb:")
third_noun = input("Enter a third noun: ")
third_adjective = input("Enter a third adjective: ")
number = input("Enter a number: ")
second_number = input("Enter a second number: ")
            
print()         # print a blank line


# Print out the string with the variables to 
# create the madlib
print("There once was a captain of a " + adjective +
      " submarine that ventured the seven seas," +
      "\non his ship there was a prized "
      + noun + " and many other pirates wanted it \nespecially comander "
      + second_name + " him and captain " + name + " had a "
      + second_adjective +
      " rivalry. \nEven though " + second_name +
      " had a equally prized " + second_noun + " ,he wanted the " + noun +
      " ,they where both willing to " + verb +
      " to the end of the world \nfor the others posession. While captian "
      + name +
      " was " + second_verb +
      " ,comander " + second_name + " launched a massive "
      + third_noun + " at captain " + name +
      " ship \nin a " + third_adjective +
      " eruption the ship exploded into " + number + " peices and "
      + second_number +
      " flew into " + name + " chest,\nslaying him "
      "comander " + second_name +
      " finnaly got the prized items he was searching for his whole life.")
