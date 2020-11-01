cars = ['audi', 'bmw', 'lexus', 'mercedes']

for car in cars:
    if car == 'lexus':
        print(car.upper())
    else:
        print(car.title())
        
        
print("\n New Exercise")

x = "Lexus"
print(x == "lexus".title())

banned = ['aslan', 'yilan', 'kus']
user = 'yanik'

if user not in banned:
    print(user.title() + " is not banned")

requested_topic = 'mushroom'

if requested_topic != 'tomato':
    print("Hold the tomato!")