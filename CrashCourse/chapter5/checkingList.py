requested_toppings = ['olive','anchovies','tomato']

cond = 'olive' in requested_toppings

print(cond)

#Checking Whether a Value Is Not in a List
print("\n Checking Whether a Value Is Not in a List")

requested_toppings2 = ['zeytin','mantar','pastirma']
top1 = 'patlican'

if top1 not in requested_toppings2:
    print(top1.title() + ' is not in requested toppings')