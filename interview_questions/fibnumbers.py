
# n = int(input("Enter Number for fib: ")) 

# if n==0:
#     print("0")
# elif n==1:
#     print("1")
# else:
#     print((n-1) + (n-2))

def FinNum(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return FinNum(n-1)+FinNum(n-2)

x = int(input("Enter Fib End number: "))
for i in range(1,x):
    print(FinNum(i))

