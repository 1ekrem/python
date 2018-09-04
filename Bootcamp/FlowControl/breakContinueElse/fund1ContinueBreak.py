#Continue
print()
print("CONTINUE - should continue the for loop after 'Spam'")
shopping_list = ["Eggs","Bagel","Milk","Spam","Cheese","Pasta"]

print(shopping_list)
for item in shopping_list:
    if item=="Spam":
        print("***Ignore {}".format(item))
        continue
    print("Buy "+item)

#Break
print()
print("BREAK  - should stop the for loop after 'Spam'")
new_shopping_list = ["Coke","Apricots","Almonds","Spam","Meat","Votka"]

print(new_shopping_list)
for item2 in new_shopping_list:
    if item2=="Spam":
        print("***Ignore {}".format(item2))
        break
    print("Buy "+item2)