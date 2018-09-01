age=24
print("My name is "+ str(age) + " years")

#NOTE: REPLACEMENT Fuel --> {x}.format
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", 
"March", "May", "July", "August", "October", "December"))

print()
print("My age is %d years" %age)
print()

print("My age is %d %s, %d %s." %(age,"years",6,"months"))
# %d = VALUE Replacement  %s = STRING Replacement.

print()

# FORMATTING
for i in range(1,12):
    print("No. %2d squared is %4d and cubed is %4d" %(i,i*i,i**3))

#note: %2d -- Allocate 2 spaces before the d=number
#note: %4d -- Allocate 4 spaces before the d=number
print()

print("Pi is approximately %12.50f" %(22/7) )

print()
# SAME AS USING %-Replacement syntax, here will be using the .FORMAT
for i in range(1,12):
    print("No. {0:2} squared is {1:<} and cubed is {2:4}".format(i,i*i,i**3))


# SAME AS USING %-Replacement syntax, here will be using the .FORMAT
# < these are formatted to the left
for i in range(1,12):
    print("No. {0:<2} squared is {1:<4} and cubed is {2:<4}".format(i,i*i,i**3))

print("spam\neggs\nbeans")