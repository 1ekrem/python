my_list=list(range(10))
print("My List: ",my_list)

even=list(range(0,10,2))
odd=list(range(1,10,2))

print("Even: ",even)
print("Odd: ",odd)


mystring= "abcdefghijklmnoprstuvwxyz"
print("The index of e: ",mystring.index("e"))
print("4th index of mystring: ",mystring[4])

small_decimals = range(0,10)
print(small_decimals)
print(small_decimals.index(8))

odd = range(1, 100, 2)
print(odd)

print(odd[48])

sevens=range(7,100,7)
x= int(input("Please enter a positive number less than 100: "))
if x in sevens:
    print("{} is divisible by seven".format(x))
else:
    print("{} is NOT divisible by seven:".format(x),"{}/7: ".format(x),(x/7))

my_range=small_decimals[::2]
print("my_range: ",my_range)
print(my_range.index(4))
