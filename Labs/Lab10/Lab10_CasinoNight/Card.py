# Antonio Rios
# November 5, 2014
# CS126 Section 2
# Lab 10: Casino Night
#####################################


class Card:

    def __init__(self, card_num):
        '''Method accepts a card_num parameter and stores
         that value in the object.'''

        self.card_num = card_num
        self.face_up()

    def get_suit(self):
        '''Method returns the suit of the card as a string
        and contains Spades, Hearts, Clubs or Diamonds depending
        on the card.'''
        
        #print(self.card_num in range(40,53))

        if self.card_num in range(0, 13):
            self.suit = 'Spades'
        elif self.card_num in range(13, 26):
            self.suit = 'Hearts'
        elif self.card_num in range(26, 39):
            self.suit = 'Clubs'
        elif self.card_num in range(39, 52):
            self.suit = 'Diamonds'
        else:
            print('Number not a card in the deck.')

        return self.suit

    def get_rank(self):
        '''This method returns the rank of the card
        as a string, and contains the number of the card
        or 'Ace', 'Jack', 'Queen', or 'King' depending
        on which card it is.'''

        if self.card_num % 13 == 0:
            self.rank = 'Ace'

        elif self.card_num % 13 == 1:
            self.rank = '2'
        elif self.card_num % 13 == 2:
            self.rank = '3'
        elif self.card_num % 13 == 3:
            self.rank = '4'
        elif self.card_num % 13 == 4:
            self.rank = '5'
        elif self.card_num % 13 == 5:
            self.rank = '6'
        elif self.card_num % 13 == 6:
            self.rank = '7'
        elif self.card_num % 13 == 7:
            self.rank = '8'
        elif self.card_num % 13 == 8:
            self.rank = '9'
        elif self.card_num % 13 == 9:
            self.rank = '10'
        elif self.card_num % 13 == 10:
            self.rank = 'Jack'
        elif self.card_num % 13 == 11:
            self.rank = 'Queen'
        elif self.card_num % 13 == 12:
            self.rank = 'King'

        return self.rank

    def get_value(self):
        '''This method returns a numeric
        value depending on the point value
        of the card at hand. Face cards
        have a value of 10. Aces are valued
        at 11, and other cards are valued
        at their numeric rank.'''

        if self.rank == 'Ace':
            self.value = 11
        elif self.rank in ['Jack', 'Queen', 'King']:
            self.value = 10
        else:
            self.value = self.card_num

        return self.value

    def face_down(self):
        '''This method flips the card
        face-down storing the string
        '<facedown>' in the instance variable
        self.face which is called by the
        __str__ method. This method returns
        nothing'''

        self.face = "<facedown>"

    def face_up(self):
        '''This method flips the card face-up
        and stores the string '<faceup>' in the
        instance variable self.face which is
        called by the __str__method. This
        method returns nothing.'''

        self.face = '<faceup>'

    def __str__(self):

        if self.face == '<facedown>':
            return self.face
        elif self.face == '<faceup>':

            self.get_rank()
            self.get_suit()
            self.face = (self.rank + " of " + self.suit)

            return self.face


# Code to test the Card class
# when executing this module on its own
if __name__ == '__main__':
    
    card = Card(51)
#
    print(card.get_suit())
    print(card.get_rank())
    print(card.get_value())
    card.face_up()
    card.face_down()
    print(card.get_suit())
# print(card)
