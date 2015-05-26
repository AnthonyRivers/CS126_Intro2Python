# Antonio Rios
# November 5, 2014
# CS126 Section 2
# Lab 10: Casino Night, Test code 
####################################


# import the modules created for this program to work
from Card import Card
from Chipstack import ChipStack

# for loop to print all 52 cards
for i in range(52):
    print(Card(i))

# Store card 37 in the variable card
card = Card(37)

# print the card
print(card)

print(card.get_value())
print(card.get_suit())
print(card.get_rank())
card.face_down()
print(card)
card.face_up()
print(card)

cs = ChipStack(149)
print(cs)
cs.deposit(7)
print(cs.value)
print(cs)
print(cs.withdraw(84))
print(cs)
cs.deposit(120)
print(cs)
print(cs.withdraw(300))
