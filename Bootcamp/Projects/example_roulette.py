rollcount = 0
print("Welcome to Roulette!")
print("You start with a budget of 500")
while rollcount < 100:
    import random
    landon = random.randint(0, 36)
    LOB = []
    budget = 500
    valnum = 0
    valin = 0
    input("Press enter to view the Betting List")
    print("The Betting List:\n--------------------")
    print("Bet on it landing on an even number by typing 'even'")
    print("Bet on an odd number by typing 'odd'")
    print("Bet on it landing on a number between 0 and 12 by typing '1st 3rd'")
    print("Bet on it landing on a number between 13 and 25 by typind '2nd 3rd'")
    print("Bet on it landing on a number between 25 and 36 by typind '2nd 3rd'")
    print("Bet on it landing on a specific number by typing the 'betnum'")
    print("Type 'low' to bet between 0 and 18, and type 'high'")
    betin = input("Place your bet: ")
    if betin == 'even':
        def beteven():
            global valin
            print("You have chosen to bet on the even numbers")
            valin = input("How much would you like to bet?: ")
            print("If it lands on an even number, you win", int(valin)*2)
            LOB.append('beteven')
        beteven()
    if betin == 'odd':
        def betodd():
            global valin
            print("You have chosen to bet on the odd numbers")
            valin = input("How much would you like to bet?: ")
            print("If it lands on an even number, you win", int(valin)*2)
            LOB.append('betodd')
        betodd()
    if betin == '1st 3rd':
        def bet13():
            global valin
            print("You have chosen to bet on the 1st third of numbers")
            valin = input("How much would you like to bet?")
            print("If it lands on the 1st third of numbers, you win", int(valin)*3)
            LOB.append('bet13')
        bet13()
    if betin == '2nd 3rd':
        def bet23():
            global valin
            print("You have chosen to bet on the 2nd third of numbers")
            valin = input("How much would you like to bet?")
            print("If it lands on the 1st third of numbers, you win", int(valin)*3)
            LOB.append('bet23')
        bet23()
    if betin == '3rd 3rd':
        def bet33():
            global valin
            print("You have chosen to bet on the 3rd third of numbers")
            valin = input("How much would you like to bet?")
            print("If it lands on the 1st third of numbers, you win", int(valin)*3)
            LOB.append('bet33')
        bet33()
    if betin == 'betnum':
        def betnum():
            global valin
            global valnum
            print("You have chosen to bet on a specific number")
            valnum = input("What number would you like to bet on?: ")
            if int(valnum) > 36 or int(valnum) < 0:
                print("You can't bet that number...")
                print("The file has reached an error, why did you do that?")
                class NotOnRouletteBoard(Exception):
                    pass
                raise NotOnRouletteBoard
            else:
                print("You chose to bet on", valnum)
                valin = input("How much would you like to bet?: ")
                print("If it lands on", valnum,  "you win", int(valin)*36)
                LOB.append('num')
                LOB.append(valnum)
        betnum()
    if betin == 'low':
        def betlow():
            global valin
            print("You chose to bet low")
            valin = input("How much would you like to bet?: ")
            print("If it lands on the 1st half of numbers, you win", int(valin)*2)
            LOB.append('betlow')
            betlow()
    if betin == 'high':
        def bethigh():
            global valin
            print("You chose to bet high")
            valin = input("How much would you like to bet?: ")
            print("If it lands on the 2nd half of numbers, you win", int(valin)*2)
            LOB.append('bethigh')
        bethigh()
    def roll():
        print("Spinning...")
        print("It has passed", random.randint(0, 36))
        print("Almost lands on", random.randint(0, 36))
        global landon
        print("It landed on", landon)
    roll()
    def lose():
        global budget
        global valin
        print("Oh no! You lost!")
        print("You lost", valin, "dollars")
        budget -= int(valin)
        print("Your budget is now", budget)
    def evenwin():
        global valin
        global budget
        print("Wow! You won! It was an even number!")
        print("You receive", int(valin)*2, "dollars!")
        budget += int(valin)*2
        print("Your budget is now", budget)
    def oddwin():
        global valin
        global budget
        print("Wow! You won! It landed on an odd number!")
        print("You receive", int(valin)*2, "dollars!")
        budget += int(valin)*2
        print("Your budget is now", budget)
    def win13():
        global valin
        global budget
        print("Holy Cow! You won!")
        print("You receive", int(valin)*3, "dollars!")
        budget += int(valin)*3
        print("Your budget is now", budget)
    def win23():
        global valin
        global budget
        print("Oh yeah!!! Hit the jackpot!")
        print("You receive", int(valin)*3, "dollars!")
        budget += int(valin)*3
        print("Your budget is now", budget)
    def win33():
        global valin
        global budget
        print("Nice job...You got a number in the 3rd third! You won!")
        print("You receive", int(valin)*3, "dollars!")
        budget += int(valin)*3
        print("Your budget is now", budget)
    def numwin():
        global valin
        global budget
        print("You won! You won! You won!")
        print("Congratulations!")
        print("You receive", int(valin)*36, "dollars!")
        budget += int(valin)*36
        print("Your budget is now", budget)
    def lowwin():
        global valin
        global budget
        print("Nice, you won!")
        print("You receive", int(valin)*2, "dollars!")
        budget += int(valin)*2
        print("Your budget is now", budget)
    def highwin():
        global valin
        global budget
        print("Nice, you won!")
        print("You receive", int(valin)*2, "dollars!")
        budget += int(valin)*2
        print("Your budget is now", budget)
    if 'beteven' in LOB and landon % 2 == 0:
        evenwin()
    if 'beteven' in LOB and landon % 2 != 0:
        lose()
    if 'betodd' in LOB and landon % 2 == 1:
        oddwin()
    if 'betodd' in LOB and landon % 2 != 1:
        lose()
    if 'bet13' in LOB and landon < 13:
        win13()
    if 'bet13' in LOB and landon >= 13:
        lose()
    if 'bet23' in LOB and landon >= 13 and landon <= 25:
        win23()
    if 'bet23' in LOB and landon < 13 or landon > 25:
        lose()
    if 'bet33' in LOB and landon > 25:
        win33()
    if 'bett33' in LOB and landon <= 25:
        lose()
    if 'num' in LOB and valnum == landon:
        numwin()
    if 'num' in LOB and valnum != landon:
        lose()
    if 'betlow' in LOB and landon < 19:
        lowwin()
    if 'betlow' in LOB and landon >= 19:
        lose()
    if 'bethigh' in LOB and landon >= 19:
        highwin()
    if 'bethigh' in LOB and landon < 19:
        lose()