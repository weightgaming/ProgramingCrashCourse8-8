import random

# Lesson 3 - Control structures
#
# In general there are two general categories of control structures
# in programing.
#
# 1.    If statements - Makes a decision on if a block of code could be executed
#       based on a set condition
#
# 2.    Loops - Loops repeat a set of instructions till a set condition is hit

if __name__ == '__main__':
    # If statements control the execution of code based on if a statement is true or false
    if False:
        print('This will never be called')

    if True:
        print('This will always be called')

    if 3 > 0:
        print('This statement will also be true')

    # The key words "or" and "and" can be used to chain conditions
    if True and 1 == 2 and 1 > -3:
        print('This will never be called')

    if 1 == 1 and 1 != 2:
        print('This will be called')

    if False or 1 == 2 or 1 == 1:
        print('This will now be called')

    if False or 1 != 1:
        print('This will not be called')

    # Not (most languages use the '!' symbol) can be used to invert logic
    if not 1 == 2:
        print('This would now be called')

    # Else statement can be used to provide a default statement that would be called
    # if the statement is not true
    if 1 == 2:
        print('This will not be called')
    else:
        print('This will be called')

    # Multiple if statements can be chained together using "else if" statement. Else If statements
    # are evaluated in order of declaration with the first true statement having its code executed and
    # then terminating the remaining evaluations.
    if 1 == 2:
        priint('This will not be called')
    elif 2 == 3:
        priint('This will not be called')
    elif 3 == 3:
        print('This will be called')
    elif 4 == 4:
        priint('This will not be called')
    else:
        priint('This will not be called')

    # NOTE: While not present in python, many languages have a variant of else if statements called
    # switch case statements. Switch case statements mainly work with very simple types and can usually
    # only check if a value is a specific value. It should be noted though in most languages switch case
    # statements are actually more efficient then else if statements but only slightly and in reality most
    # compilers will convert else if statements into switch cases if they can. Switch cases do tend to be more
    # readable though, especially if a large number of values need to be compared.
    #
    # An example of a switch case statement is:
    # switch(15)
    # {
    #   case 1:
    #       print
    #       break
    #   case 15:        <-- Would be called
    #       print
    #       break
    #   default:
    #       print
    #       break
    # }

    # Loops are a control structures that repeat a list of commands till a condition is met
    # there are usually two types of loops in most languages, while and for loops.

    # While loops are met to loop until a condition is no longer true. The following
    # will loop until num == 10
    num: int = 0
    while num != 10:
        print('Loop' + str(num))
        num = random.randrange(0, 11)

    # For loops can iterate over a set list of elements or iterate a set number of times.
    # most for loops follow the format of (counter, condition, incrementer) with "foreach" loops
    # being used to loop over collections. In Python all for loops are technically foreach loops.
    # The following will loop 10 times
    for count in range(0, 10):
        print('For Loop' + str(count))