# Antonio Rios
# John Causey
# September 17, 2014
# CS126 Lab Section 2
# Lab03 - MathQuiz
# =====================

from random import randint

# initialize the counter, keeps track of right answers
correct = 0
number_difficulty = 0

# Prompt the user for the amount of questions they want to answer
question_amount = int(input("Enter the amount of " +
                            "questions you want to answer: "))

# Prompt the user for the level they want to start on
level = input("Enter the level you want to begin at: "
              + "(Beginner, Intermediate, Advance) ").lower()

# Set difficulty level
if level == "beginner":
    number_difficulty = 10
elif level == "intermediate":
    number_difficulty = 25
elif level == "advanced":
    number_difficulty = 100


def multiplication(number_difficulty):
    '''Generates a multiplication question'''

    n1 = randint(1, number_difficulty)
    n2 = randint(1, number_difficulty)
    answer = n1 * n2
    student_answer = int(input("What is %g times %g? " % (n1, n2)))

    if student_answer == answer:
        print("That is correct!")
        global correct
        correct += 1
    else:
        print("No, I'm afraid the answer is %g " % answer)


def addition(number_difficulty):
    '''Generates an addition question'''

    n1 = randint(1, number_difficulty)
    n2 = randint(1, number_difficulty)
    answer = n1 + n2
    student_answer = int(input("What is %g plus %g? " % (n1, n2)))

    if student_answer == answer:
        print("That is correct!")
        global correct
        correct += 1
    else:
        print("No, I'm afraid the answer is %g" % answer)


def subtraction(number_difficulty):
    '''Generates a subtraction question'''

    n1 = randint(1, number_difficulty)
    n2 = randint(1, number_difficulty)
    answer = n1 - n2
    student_answer = int(input("What is %g minus %g? " % (n1, n2)))

    if student_answer == answer:
        print("That is correct!")
        global correct
        correct += 1
    else:
        print("No, I'm afraid the answer is %g" % answer)

# Generate quiz
for i in range(question_amount):
    print("What type of question would you like?")
    q_type = input("(Subtraction, Addition, or Multiplication)? ").lower()

    if q_type == "multiplication":
        multiplication(number_difficulty)
    elif q_type == "subtraction":
        subtraction(number_difficulty)
    elif q_type == "addition":
        addition(number_difficulty)

# Generate results
amount_correct = (correct / question_amount)
print("\nI asked you %g questions. You got %g of them right."
      % (question_amount, correct))

if amount_correct > (2/3):
    print("Well done!")
elif amount_correct < (1/3):
    print("Please ask your math teacher for help!")
else:
    print("You need more practice")
