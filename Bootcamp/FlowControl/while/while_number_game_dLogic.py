import random

highest = 10
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess=int(input())

if guess != answer:
    if guess > answer:
        print("Guess lower")
    else:
        print("Guess higher")
    guess=int(input())
    if guess == answer:
        print("Well done. The anwer is {}".format(answer))
    else:
        print("Sorry, you have not guessed correctly. The random number was {}".format(answer))
else:
    print("Great! You guessed it on the first try!")