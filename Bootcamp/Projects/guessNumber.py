import random

highest = 10
answer = random.randint(1,highest)

print("Please guess a number between 1 and {}: ".format(highest))

guess=0

while guess != answer:
    guess=int(input())
    if guess==0:
        break
    if guess > answer:
        print("Guess lower")
    elif guess < answer:
        print("Guess higher")
    else:
        print("Well done. The anwer is {}".format(answer))



