import random
rand_nr = random.randint(0,100)
print("Random number is: ", rand_nr)

def fib(n):
    if n<2:
        f=1
    else:
        f=(n-1)+(n-2)
    return f

print(fib(rand_nr))

# Dynamic Programming
memo = {}
def fib_dy(m):
    if m in memo:
        return memo[m]
    elif m<2:
        f=1
    else:
        f=(m-1)+(m-2)
    memo[m] = f
    return f

print(fib_dy(4))