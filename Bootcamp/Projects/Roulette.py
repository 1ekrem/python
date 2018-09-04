import random
import time
import sys

deposit = float(input("How much would you like to deposit?\n"))

bet=float(input("How much would you like to bet?\n"))
time.sleep(1)
remaning_balance = deposit-bet
print("Your remaning balance is: $"+str(remaning_balance))
time.sleep(1)
print()

input("Press enter to view the Betting List")
print("The Betting List:\n--------------------")
time.sleep(1)
print("Bet on it landing on an even number by typing 'even'")
time.sleep(1)
print("Bet on an odd number by typing 'odd'")
time.sleep(1)
bet_name= input("What's your bet? Even or Odd?\n")
time.sleep(1)

random_number=random.randint(1,32)
winning_logic=int(random_number % 2)
zero=0
print()

print("The ball is spinning...")
time.sleep(2)
print("The number is :"+str(random_number))

even_odd_rate=2
time.sleep(1)


if (winning_logic==0) and bet_name == "even":
    print("You won!")
    bet_total = bet*even_odd_rate
    deposit=deposit-bet
    deposit= deposit+bet_total
    print("You bet: $"+str(bet)+".\nYou won: $"+str(bet_total)+".")
    print("Your total is: "+str(deposit))
elif (winning_logic==1) and bet_name == "odd" :
    print("You won!")
    bet_total = bet*even_odd_rate
    deposit=deposit-bet
    deposit= deposit+bet_total
    print("You bet: $"+str(bet)+".\nYou won: $"+str(bet_total)+".")
    print("Your total is: $"+str(deposit))
else:
    deposit=deposit-bet
    print("You lost: $"+str(bet)+"!")
    print("Your total is: $"+str(deposit)+".")
