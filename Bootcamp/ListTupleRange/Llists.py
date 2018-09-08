# number=input("Please enter 10 digits number")
# print(number.count("5"))

parrot_list = ["non pinin'","no more", "a stiff", "bereft of live"]
for state in parrot_list:
    if state.__contains__('o'):
        print("This parrot is "+state)
