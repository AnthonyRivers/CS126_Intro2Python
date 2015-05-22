#############################
# Antonio Rios
# October 8, 2014
# CS126 LAB
# Lab6: Banners
#############################


# Dictionary storing the symbolized
# letter in ascii art form
letters = {'A': {0: '  xx  ',
                 1: ' x  x ',
                 2: ' xxxx ',
                 3: ' x  x ',
                 4: ' x  x ',
                 5: '      '},
           'B': {0: 'xxxxx ',
                 1: 'x    x',
                 2: 'xxxxx ',
                 3: 'x    x',
                 4: 'xxxxx ',
                 5: '       '},
           'C': {0: 'xxxxxx',
                 1: 'x     ',
                 2: 'x     ',
                 3: 'x     ',
                 4: 'XXXXXX',
                 5: '      '},
           'D': {0: 'xxxxx ',
                 1: 'x    x',
                 2: 'x    x',
                 3: 'x    x',
                 4: 'xxxxx ',
                 5: '      '},
           'E': {0: 'xxxxxx',
                 1: 'x     ',
                 2: 'xxxxx ',
                 3: 'x     ',
                 4: 'xxxxxx',
                 5: '      '},
           'F': {0: 'xxxxxx',
                 1: 'x     ',
                 2: 'xxxxx ',
                 3: 'x     ',
                 4: 'x     ',
                 5: '      '},
           'G': {0: 'xxxxx ',
                 1: 'x     ',
                 2: 'x  xxx',
                 3: 'x    x',
                 4: 'xxxxx ',
                 5: '      '},
           'H': {0: 'x    x',
                 1: 'x    x',
                 2: 'xxxxxx',
                 3: 'x    x',
                 4: 'x    x',
                 5: '      '},
           'I': {0: 'xxxxxx',
                 1: '   x  ',
                 2: '   x  ',
                 3: '   x  ',
                 4: 'xxxxxx',
                 5: '      '},
           'J': {0: 'xxxxxx',
                 1: '   x  ',
                 2: '   x  ',
                 3: '   x  ',
                 4: 'xxx   ',
                 5: '      '},
           'K': {0: 'x    x',
                 1: 'x x x ',
                 2: 'x  x  ',
                 3: 'x   x ',
                 4: 'x    x',
                 5: '      '},
           'L': {0: 'x     ',
                 1: 'x     ',
                 2: 'x     ',
                 3: 'x     ',
                 4: 'xxxxxx',
                 5: '      '},
           'M': {0: 'x    x',
                 1: 'xx  xx',
                 2: 'x xx x',
                 3: 'x    x',
                 4: 'x    x',
                 5: '      '},
           'N': {0: 'x    x',
                 1: 'xx   x',
                 2: 'x x  x',
                 3: 'x  x x',
                 4: 'x    x',
                 5: '      '},
           'O': {0: 'xxxxxx',
                 1: 'x    x',
                 2: 'x    x',
                 3: 'x    x',
                 4: 'xxxxxx',
                 5: '      '},
           'P': {0: 'xxxxxx',
                 1: 'x    x',
                 2: 'xxxxxx',
                 3: 'x     ',
                 4: 'x     ',
                 5: '      '},
           'Q': {0: 'xxxxxx',
                 1: 'x    x',
                 2: 'x  x x',
                 3: 'x   xx',
                 4: 'xxxxxx',
                 5: '      x'},
           'R': {0: 'xxxxx ',
                 1: 'x   x ',
                 2: 'xxxxx ',
                 3: 'x x   ',
                 4: 'x  x  ',
                 5: '      '},
           'S': {0: ' xxxxx',
                 1: ' x    ',
                 2: ' xxxx ',
                 3: '    x ',
                 4: ' xxxx ',
                 5: '      '},
           'T': {0: 'xxxxxx',
                 1: '  x   ',
                 2: '  x   ',
                 3: '  x   ',
                 4: '  x   ',
                 5: '      '},
           'U': {0: 'x    x',
                 1: 'x    x',
                 2: 'x    x',
                 3: 'x    x',
                 4: 'xxxxxx',
                 5: '      '},
           'V': {0: 'x    x',
                 1: 'x    x',
                 2: 'x    x',
                 3: ' x  x ',
                 4: '  xx  ',
                 5: '      '},
           'W': {0: 'x    x',
                 1: 'x    x',
                 2: 'x xx x',
                 3: 'xx  xx ',
                 4: 'x    x',
                 5: '      '},
           'X': {0: 'x    x',
                 1: ' x  x ',
                 2: '  xx  ',
                 3: ' x  x ',
                 4: 'x    x',
                 5: '      '},
           'Y': {0: 'x    x',
                 1: ' x  x ',
                 2: '  xx  ',
                 3: '  x   ',
                 4: '  x   ',
                 5: '      '},
           'Z': {0: 'xxxxxx',
                 1: '    x ',
                 2: '   x  ',
                 3: '  x   ',
                 4: ' xxxxx',
                 5: '      '},
           ' ': {0: '      ',
                 1: '      ',
                 2: '      ',
                 3: '      ',
                 4: '      ',
                 5: '      '}}


def print_banner(message, orientation):
    '''This function converts the string message
       passed to it and converts it into it's
       ascii art form representation. Then it prints
       the message in the chosen orientation
       vertically or horizontally.

       parameters: STRING type 'message' and 'orientation'
       returns: This function returns nothing.

       '''


    # Make all the letters in the message uppercase
    # to match the keys in the dictionary.
    message = message.upper()

    # Check the user choice for orientation if they enter anything
    # other than vertical the letters will print horizontally.
    if orientation in ['vertical', 'v', 'V', 'Vertical', 'VERTICAL']:

        for letter in message:
            for item in letters[letter]:
                print(letters[letter][item])

    else:
        
        for i in range(6):
            line = " "
            for j in message:
                line = line + letters[j][i] + ' '
            print(line)


# prompt the user for orientation and the message they want to print
orientation = input("Orientation of message? (Vertical or Horizontal):")
message = input("Enter a message to convert: ")

# call the function to print the ascii representation of the message
print_banner(message, orientation)
