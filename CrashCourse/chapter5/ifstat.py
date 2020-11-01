age = '17'
diff = abs(int(age) - 18)

if age > '18':
    print("You are allowed to vote!")
else:
    print("Sorry you have", diff, "year(s) to be eligible to vote!")
    
    
# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10.

age2 = 66

if age2 == 0:
    price = 0
elif age2 >= 4 and age2 <= 18:
    price = 5
elif age2 > 65:
    price = 1
else:
    price = 10
    
print("Admission costs {}".format(price))