#FizzBuzz Challenge
#Print from 1 to 100
#Print 'fizz' if the number if divisible by 3
#Print 'buzz' if the number if divisible by 5
#Print 'fizzbuzz' if the number if divisible by 3 and 5

fizz="fizz"
buzz="buzz"


for i in range(0,101): 
    if  (i%3==0 and i%5==0):
        print("{1}-{0} is divisible by 3 and 5".format(str(fizz+buzz),int(i)))
    elif i%3==0 :
        print("{1}-{0} is divisible by 3".format(str(fizz),int(i)))
    elif i%5==0:
        print("{1}-{0} is divisible by 5".format(str(buzz),int(i)))
    else:
        print(i) #Print all the indivisible numbers