#Write a loop that stops when i is exactly divisible by 11
#Make sure you print the numbers until it reaches the i is exactly divisible by 11

for i in range(0, 100, 7):
    if i>0 and (i%11)==0:
        print(i)
        break
    print(i)    
    