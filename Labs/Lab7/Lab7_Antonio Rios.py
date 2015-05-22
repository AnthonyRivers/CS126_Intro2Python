# Antonio Rios
# October 15, 2014
# CS126 Lab
# Lab 7: Game Show
##############################


import random

# list of trivia questions, with answers and correct answer
# a list of dictionaries
questions = [{"question": "Who created Python?",
              "answers": ["Guido van Rossum",
                          "Louis G Wilson",
                          "Bill Gates",
                          "Steve Jobs"],
              "correct": 1},
             {"question": "When was Python created?",
              "answers": ["2005",
                          "2001",
                          "1995",
                          "1991"],
              "correct": 4},
             {"question": "What is the most recent stable release for Python?",
              "answers": ["2.7.4",
                          "1.7.6",
                          "3.4.1",
                          "8.6.9"],
              "correct": 3},
             {"question": "What is a valid file extension for Python?",
              "answers": [".ppt",
                          ".py",
                          ".doc",
                          ".exe"],
              "correct": 2},
             {"question": "How do we delimit blocks of code in Python?",
              "answers": ["curly braces",
                          "colons",
                          "whitespace indentation"],
              "correct": 3},
             {"question": "What is Python named after?",
              "answers": ["Monty Python",
                          "the snake",
                          "creator's alma mater's mascot",
                          "a short story"],
              "correct": 1},
             {"question": "What famous software was app created with Python?",
              "answers": ["Matlab",
                          "Dropbox"],
              "correct": 2},
             {"question": "What is the correct way to concatnate strings "
              "with numbers?",
              "answers": ["\"string\" + 123",
                          "123 + 123",
                          "\"string\" + str(123)",
                          "123 + \"string\""],
              "correct": 3},
             {"question": "What do tuples allow you to do?",
              "answers": ["Store a sequence of unrepetable values",
                          "Unpack variables",
                          "Change values later in the tuple",
                          "Store key value pairs"],
              "correct": 2},
             {"question": "Which of the following is a boolean value?",
              "answers": ["\"string\"",
                          "123",
                          "True",
                          "3.14"],
              "correct": 3},
             {"question": "Which programming language did python influence?",
              "answers": ["Visual Basic",
                          "Objective-C",
                          "Ruby",
                          "Java"],
              "correct": 3},
             {"question": "What is the formatting convention in Python?",
              "answers": ["PEP 20",
                          "PEP 4",
                          "PEP 8"],
              "correct": 3}]

# empty dictionary to keep track of high scores
high_scores = {}


def play_game():
    """
    The play_game() function is where the main game starts.
    Prompts the user with the questions and keeps track
    of the correct answers. When the user is done answering
    the questions the user is prompt for his/her name. The name
    and the count of correct answers is then passed to the
    add_high_score() function.

    """
    
    print("Welcome to our Python trivia game!")
    print("Win Billions! ... but not really...")
    print()
    
    # question_count counts the number of questions that have been asked.
    # It will be used to display how many questions the user got right
    # out of question_count.
    question_count = 1
    count_score = 0
    
    # shuffle questions
    random.shuffle(questions)
    for question in questions:

        print(question["question"])
        for i, choice in enumerate(question["answers"]):
            print(str(i + 1) + ". " + choice)
        answer = int(input("Choose an answer "
                           "1-{}: ".format(len(question["answers"]))))
        # user input validation loop
        # must have +1 after len(question["answers"] because
        # the range function is exclusive
        while answer not in range(len(question["answers"]) + 1):
            answer = int(input("Error! Please choose an answer "
                               "1-{}:".format(len(question["answers"]))))
        if answer == question["correct"]:
            print("Good job!")
            count_score += 1
        else:
            print("Not correct, sorry.")
        print("Your current score is {} out of "
              "{} question(s) asked.".format(count_score, question_count))
        question_count += 1
        print()
        
    name = input("What is your name?")
    add_high_score(name, count_score)


def add_high_score(name, count_score):
    """
    This function checks if the name is already in the
    high_scores dictionary. If not the name and the count score are added to
    the high_scores dictionary.

    parameters: STRING type 'name', INTEGER type 'count_score'
    returns: This function returns nothing.

    """
    
    if name in high_scores:
        if count_score > scores[name]:
            high_scores[name] = count_score
    else:
        high_scores[name] = count_score


def view_high_scores():
    """
    This function checks if there are any items in the dictionary
    to display. If there is items then the name and high scores are
    display to console.


    """
    if len(high_scores) == 0:
        print("There are currently no high scores to display.")
    else:
        message = "Scoreboard!"
        print('=' * len(message))
        print(message)
        print('=' * len(message))
        print("Player Name: \t Score")
        scores = list(high_scores.values())
        scores.sort()
        scores.reverse()
        for score in scores:
            for person in high_scores:
                if score == high_scores[person]:
                    print(person + "\t\t" + str(score))


def view_credits():
    """
    This function displays the credits to the console.

    """
    
    message = 'The Python trivia game was created by Antonio Rios.'
    print('=' * len(message))
    print(message)
    print('=' * len(message))


def thank_you():
    """
    This function prints out a thank you message to the console.

    """
    
    print("Thank for playing the Python trivia game!")


# while loop keeps the game going until the user
# decides to quit the game.
while True:
    
    menu = '''
    1 - Play the game
    2 - View game credits
    3 - View high scores
    4 - quit
    '''
    
    print(menu) # Prints the menu string to console

    # Prompts the user to choose an option and stores that choice
    # in the menu_choice variable
    menu_choice = int(input("Which do you choose? "))

    # based on the user's choice each function is called.
    if menu_choice == 1:
        play_game()
    elif menu_choice == 2:
        view_credits()
    elif menu_choice == 3:
        view_high_scores()
    elif menu_choice == 4:
        thank_you()
        break
