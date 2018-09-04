import random
import time


x=input("Please enter your name: ")
y=input("Please enter your lastname: ")
age=int(input("Please enter your age: "))

years_to_drink= 25-age
age_logic = age >= 25 
name_logic = (x=="ekrem") and (y=="ersayin")
randomnumber = str(random.randint(100,1000))
sleep=time.sleep(1.5)

if x:
    print("Your name is {1}\nYour last name is {2}\nYour age is {3}. ".format(str, x,y, int(age)))
    sleep
    if name_logic :
        print("Correct name entered: ", x)
        sleep
        if age_logic :
            print("You can enjoy your drink!")
        else:
            print("Please come back in "+str(years_to_drink)+" year to drink something in the bar.")
    else:
        print("Wrong name entered. Can't find you on the invitation list!")
        check_again=input("Would you like to check again? yes/no: \n")
        if check_again == "yes":
            name_reenter= input("Please enter your name:\n")
            if name_reenter=="ekrem":
                print("Name is confirmed! Now I need to confirm your age again!")
                age_reenter=int(input("Please provide your age\n"))
                if age_reenter >=25:
                    print("Validated! Generating your userID")
                    sleep
                    print("Invitation found! This is your userID for enterance: "+name_reenter+randomnumber)
        else:
            print("Thank you! Good Bye!")
            # else:
            #     print("Something wrong with the name you entered.")
            #     time.sleep(4)
            #     print("Please call helpdesk at 888-853-7752")
else:
    print("You did not enter anything.")
