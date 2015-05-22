# Antonio Rios
# CS126
# Lab 8: Midterm Grade Estimator
# October 22, 2014
#####################################


def gather_grade_categories():
    '''Prompts user to enter each category and
       then 'done' when there are no more categories'''

    categories = []

    while True:

        print("Enter a category you are graded in ", end='')
        category = input("or 'done' once you are finished:")

        if category.lower() == 'done':
            break
        else:
            categories.append(category)

    # Return a list of categories representing
    # the differents areas of the class
    return categories


def collect_points(category, points_type):
    '''Prompts user to enter a comma seperated list of possible
       OR earned points for the given category.'''

    print("\nEnter " + points_type + " point values for " + category +
          " seperated by commas: ", end='')

    points = input().split(',')
    points = [int(i) for i in points]

    # returns a list of possible points for the given category
    return points


def set_weight(category):
    '''Prompts user to enter the weight for a given category.'''

    points = int(input('Enter the percentage of your overall course grade for '
                       + category + ':'))

    # Returns a number representing the percentage of 100
    return points


def calc_grade(category, possible, earned, weight):
    '''Calculates the total weight
       points earned for a given category.'''

    total_possible = 0
    total_earned = 0

    for points_possible in possible:
        total_possible += points_possible

    for point in earned:
        total_earned += point

    print('For ' + category + ' there were a total of ' + str(total_possible) +
          ' possible points.')
    print('You earned a total of ' + str(total_earned) + ' points.')
    print('The ' + category + ' category has a weight of ' + str(weight) + '.')

    points = (total_earned / total_possible) * int(weight)

    print('Thus, you have earned %.2f pts in the %s category\n'
          % (points, category))

    # Returns points weighted score for the category
    # and also prints the total possible points,
    # the total points earned and
    # then weight score.
    return points


def show_letter(grade):
    '''Turns a numberical grade into a letter grade,
        and should do so without using any conditional
        statements.'''

    letter = {9: 'A',
              8: 'B',
              7: 'C',
              6: 'D',
              5: 'F',
              4: 'F',
              3: 'F',
              2: 'F',
              1: 'F',
              0: 'F'}

    # returns A,B,C,D or F according
    # to the traditional grading scale
    return letter[grade//10]


# Main logic of the program which makes
# use of the functions to calculate the
# grade.
grade = {}
total_earned = 0
total_possible = 0

for category in gather_grade_categories():
    grade[category] = {}
    while True:
        grade[category]['possible'] = collect_points(category, 'possible')
        grade[category]['earned'] = collect_points(category, 'earned')
        if len(grade[category]['possible']) == len(grade[category]['earned']):
            break
        else:
            print('Entries did not contain the'
                  + ' same number of values. Try again.')
    grade[category]['weight'] = set_weight(category)
    total_earned += calc_grade(category,
                               grade[category]['possible'],
                               grade[category]['earned'],
                               grade[category]['weight'])
    total_possible += grade[category]['weight']

print('Your overall grade is currently '
      + str(total_earned/total_possible*100) +
      '%, or a ' + show_letter(total_earned/total_possible*100))
