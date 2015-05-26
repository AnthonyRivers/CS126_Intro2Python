# Antonio Rios
# November 5, 2014
# CS126 Lab Section 2
# Lab 10: Casino Night
##############################


class ChipStack:
    '''This class represents the stack of chips
    and will contain the value of chips.'''

    def __init__(self, value):
        '''Creates a new ChipStack object with
        an initial monetary value passed in as value.'''

        # value - Numeric value to start the chip stack at.
        self.value = value

    def withdraw(self, amount):
        '''Reduces the value of the ChipStack by the given amount.
        If amount is greater than the remaining value, then
        amount is reduced from the remaining value.
        The function returns the amount actually withdrawn.'''

        if self.value < amount:
            amount = self.value
            self.value -= amount
            return amount
        else:
            self.value -= amount
            return amount

    def deposit(self, amount):
        '''Increases the value of the ChipStack by the given
        amount. Does not return a value.'''

        self.value += amount

    def __str__(self):
        '''Returns the object in as a string describing the different
        chips held as well as the total value. The number of chips
        listed is the minimum number representing the total value.'''

        black_chips = self.value // 100
        remaining_amount = self.value - (black_chips * 100)
        green_chips = (remaining_amount // 25)
        remaining_amount -= green_chips * 25
        red_chips = remaining_amount // 5
        remaining_amount -= red_chips * 5
        blue_chips = remaining_amount // 1

        return '{0} blacks, {1} greens, {2} reds, ' \
            '{3} blues - totaling ${4}'.format(
                black_chips, green_chips, red_chips, blue_chips, self.value)


#Test code
if __name__ == '__main__':

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
