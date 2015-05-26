# Antonio Rios
# November 19, 2014
# CS126 Lab Section 2
# Lab 11: BlackJack
#############################


# import the necessary modules
from Card import Card
from Chipstack import ChipStack
import random


def hand_str(hand):
    """
    The hand_str() function dea

    paramaters: Takes in a hand of Cards.
    return: Returns a string representation of Card hand

    """
    
    hand_to_str = ''

    for card in hand:
        if card == '<facedown>':
            hand_to_str += '<facedown>'
        hand_to_str += card.get_rank() + ' ' + card.get_suit() + ','

    return hand_to_str


def hand_value(hand):
    """
    The hand_value() function calculates the
    the worth of the hand and returns the sum.


    parameters: Takes in a hand of Cards
    returns: Returns the sum of the values of the Card hand.

    """
    sum_of_hand = 0

    for card in hand:
        if card == '<facedown>':
            pass
        else:
            sum_of_hand += card.get_value()

    return sum_of_hand


class BlackJack:
    """
    The BlackJack class implements the functionality
    of a black jack game.
    

    """
    
    def __init__(self, num_decks, chips):
        """
        The constructor initializes the BlackJack game taking in
        an integer a value representing a number of deck of cards and
        the starting amount of chips to play.

        
        parameters: INTEGER number of decks, INTEGER amount of chips
        
        """

        self.chip_stack = ChipStack(chips)

        self.num_decks = num_decks

        self.cards = []
        self.discard_pile = []

        for num in range(num_decks):
            for i in range(52):
                self.cards.append(Card(i))

        random.shuffle(self.cards)

        self.live_game = True
        self.dealer_hand = []
        self.player_hand = []
        self.wager = 0

    def draw(self):
        """
        The draw() method draws a Card from the deck of cards.

        parameters: Takes no parameters
        return: Returns a Card drawn from the deck.
        """

        drawn_card = 0

        if self.cards == []:
            random.shuffle(self.discard_pile)
            drawn_card = self.discard_pile.pop()
        else:
            drawn_card = self.cards.pop()
            
        #print('drawn card',drawn_card)
        return drawn_card

    def new_hand(self, wager):
        """
        The new_hand() method takes in a wager as a parameter
        and checks if there is a winner or the game must keep going.

        parameter: Takes in amount representing a wager
        returns: This method returns nothing, however, it sets
        the live_game variable to True if no winner, loser, or a tie
        has occur.

        """

        self.dealer_hand = [self.draw(), self.draw()]
        self.player_hand = [self.draw(), self.draw()]

        self.wager = self.chip_stack.withdraw(wager)
        print('Your starting hand: ', end=' ')
        print(hand_str(self.player_hand))
        print('dealers starting hand: ', end='')
        print('<facedown>', ',', str(self.dealer_hand[0]))

        if (hand_value(self.dealer_hand) == 21) \
                and (hand_value(self.player_hand) == 21):
            self.cleanup("push")

        elif hand_value(self.dealer_hand) == 21:
            print(hand_str(self.dealer_hand))
            self.cleanup("lose")

        elif hand_value(self.player_hand) == 21:
            self.cleanup("win")
            self.chip_stack.deposit(self.wager * 2)
            print(self.chip_stack)

        self.live_game = True

    def hit(self):
        """
        The hit() method draws a new card and appends it
        to the player's hand. It also checks if the hand has
        exceed 21 or equals 21.
        
        """

        self.player_hand.append(self.draw())
        print('Player new hand')
        print(hand_str(self.player_hand))

        if hand_value(self.player_hand) > 21:
            self.cleanup("lose")
        elif hand_value(self.player_hand) == 21:
            self.stand()

    def stand(self):
        """
        The stand() method displays the Dealer's hand and
        draws a Card if the hand value is less than 16. It also
        checks if the dealer wins or busts.

        """
        # for card in self.dealer_hand:
        #     card.face_up()
        print("Dealer's hand: ", hand_str(self.dealer_hand))
        #print(hand_str(self.dealer_hand))

        if hand_value(self.dealer_hand) <= 16:
            while hand_value(self.dealer_hand) <= 16:
                dealer_draws_card = self.draw()
                print("Dealer's draws a ", dealer_draws_card)
                self.dealer_hand.append(dealer_draws_card)
                print("Dealer's hand is now ", hand_str(self.dealer_hand))

            if (hand_value(self.dealer_hand)) > 21:
                print('Dealer busts, you win!')
                self.cleanup("win")
            elif hand_value(self.dealer_hand) == hand_value(self.player_hand):
                print('Your hand and the dealer is the same. No one wins.')
                print(hand_str(self.player_hand), hand_str(self.dealer_hand))
                self.cleanup("push")
            elif hand_value(self.dealer_hand) > hand_value(self.player_hand):
                print('The dealer beats your hand!')
                self.cleanup("lose")
            elif hand_value(self.dealer_hand) < hand_value(self.player_hand):
                print('Your hand is higher than the dealer\'s')
                self.cleanup("win")

        elif (hand_value(self.dealer_hand)) > 21:
                print(hand_str(self.dealer_hand), 'is over 21.')
                self.cleanup("win")
        elif hand_value(self.dealer_hand) == hand_value(self.player_hand):
            print('Your hand and the dealer is the same. No one wins.')
            print(hand_str(self.player_hand), hand_str(self.dealer_hand))
            self.cleanup("push")
        elif hand_value(self.dealer_hand) > hand_value(self.player_hand):
            print(hand_str(self.dealer_hand), 'is higher than yours.')
            self.cleanup("lose")
        elif hand_value(self.dealer_hand) < hand_value(self.player_hand):
            print('Your hand is higher than the dealer\'s')
            self.cleanup("win")

    def cleanup(self, outcome):
        '''This method is called when a winner has been
        determined. The cleanup metod is passed a string
        parameter called outcome which should be equal to
        either "win", "lose", or "push". If the player wins
        they will be given double their wager back. A push
        will refund the original wager. A lose will result
        in no money being deposited.
        Cleanup is also responsible for moving the cards in
        both hands in to the discard pile and setting the
        two hands and the wager back to None.'''

        if outcome == 'win':
            print('You are a winner!')
            self.chip_stack.deposit(2*self.wager)
        elif outcome == 'lose':
            print('You loose!')
            pass
        elif outcome == 'push':
            self.chip_stack.deposit(self.wager)

        self.live_game = False

        # Implementation of moving the cards
        # to the discard pile still needs to
        # be implemented and setting the
        # two hands and the wager back to None.
        self.discard_pile += self.cards
        self.dealer_hand = None
        self.player_hand = None
        self.wager = None

    def game_active(self):
        '''Returns True or False, indicating
        if there is a current hand in play.

        Return True when new_hand() has been called,
        and cleanup() has not yet been called to
        close the game.'''

        return self.live_game


if __name__ == '__main__':
    blackjack = BlackJack(4, 250)

    while blackjack.chip_stack.value > 0:
        print()
        print("Your remaining chips: " + str(blackjack.chip_stack))
        wager = int(input("How much would you like to wager?"))
        blackjack.new_hand(wager)

        while blackjack.game_active():
            choice = input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
    print()
    print("Out of money! The Casino wins!")
