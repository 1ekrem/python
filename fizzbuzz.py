
f='fizz'
b='buzz'

for i in range(1,100+1):
    if (i%3==0 and i%5==0):
        print(i,"-",f,b)
    elif i%3==0:
        print(i,"-",f)
    elif i%5==0:
        print(i,"-",b)
    else:
        print(i,'--------')