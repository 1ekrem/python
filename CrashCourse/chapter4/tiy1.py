# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

for i in range(1,20+1):
    print(i)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
print("New Q")
for i in range(1,1000000+1):
    if i == 1000000:
        print(i)
        
# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

print('\n', "New Q")
mlist = []
for x in range(1,1000000+1):
    mlist.append(x)

print('Min of mlist:',min(mlist))
print('Max of mlist:',max(mlist))
print('Sum of mlist:',sum(mlist))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
print('\n', "New Q")
odd_list = list(range(1,20+1,2))
print(odd_list)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
print('\n', "New Q")
odd3_list = list(range(3,30+1,3))
print(odd3_list)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

print('\n', "New Q4.8")
cubes =[val**3 for val in range(1,10+1)]
print(cubes)

for cube in cubes:
    print(cube)

