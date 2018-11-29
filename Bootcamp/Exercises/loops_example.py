# Print i as long as i is less than 6.
# i = 1 
# while i<10:
#     print(i)
#     #i += 1 OR as below
#     i= i+1

# Stop the loop if i is 3
print("------------Loops------------")
i = 0
while i<=6:
    print(i)
    if i==3:
        break
    i = i+1
    

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print("------------Functions------------")
def my_function():
    greeting = "Hello from a function"
    return greeting

ff = my_function()
print(ff)

def my_function2():
    print("Hello2")

my_function2()