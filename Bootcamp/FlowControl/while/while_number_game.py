import random
import sys

highest=10

random_nr = random.randint(1,highest)

guess=int(input("Please print a number between 1 and {}\n".format(highest)))

if guess==random_nr:
    print("Great! You guessed it on the first try!")
else:
    print("You have 2 more chances!")
    guess2=int(input("Please print a number between 1 and {}\n".format(highest)))
    if guess2==random_nr:
        print("Good job! You guessed it on the second try!")
    else:
        print("You have 1 more chance!")
        guess3=int(input("Please print a number between 1 and {}\n".format(highest)))
        if guess2==random_nr:
            print("Still okay! You guessed it your third try!")
        else:
            print("Good Bye! The number was: ",random_nr)
            sys.exit
