print("")

print("Please enter how many rows of pyramid you would like to see. E.g: 5, 7 or 10")
n=int(input())

number=1 #1 Initalize the starting number

for i in range(0,n+1): #2 This loop handles how many rows

    number=1 #3 Reassing number.    

    for k in range (1,i+1): #4 This handles how many columns and changing numbers

        print(number, end=" ") #5 Print number

        number = number+1 #6 Increment the number by 1 at each column

    print("\r") #7 end line after each row    


