meal = ["Eggs","Bagel","Milk","Spam","Cheese","Pasta"]

nasty_food = '' #If you don't initialize this object than the script will fail when the keyworrd "SPAM" is missing.

for item in meal:
    if item=="Spam":
        nasty_food=item
        print("Ignore {}".format(nasty_food))
        break
else:
    print("I'll have a plate of that, then, please!")

if nasty_food:
    print("Can't eat something having spam in it!")

for i in range(0, 100, 7):
    if (i%11)==0:
        break
    print(i)