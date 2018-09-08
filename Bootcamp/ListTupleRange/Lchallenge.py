
menu=list()

menu.append(["eggs","spam", "bacon"])
menu.append(["eggs", "sausage", "bacon"])
menu.append(["eggs", "spam"])
menu.append(["eggs", "banana", "orange", "spam"])
menu.append(["eggs", "apple", "cherry", "banana", "spam"])
menu.append(["eggs", "soup", "meat", "spam"])
menu.append(["eggs", "omelet", "cheese", "bacon", "spam"])

# for meal in menu:
#     if not "spam" in meal:
#         print(meal)

#Challenge
#Add to the program above so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did above.


for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredients in meal:
            print(ingredients)