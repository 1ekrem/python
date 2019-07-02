# read in age

age = int(input("Please enter your age: "))

if age > 18:
    print("Access Allowed!")
elif age < 18 and age >0:
    print("Access NOT Allowed!")
else:
    print("Invalid Age!")