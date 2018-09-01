
#Create a list
lists = [1,2,3,4,5,6, "hello"]

#Add a new value/variable
lists.append(9)

print(lists)

# I want to know how many '2's in the list?

print (lists.count(2))
#There is only one 2. 

# What if I add another '2' in the list and count again?

print("What if I add another '2' in the list and count again?")

lists.append(2)
print(lists)

print(lists.count(2))
#   There should be two 2s now!

# What if I want to remove a value like 6 from the list?
print ("What if I want to remove a value like 6 from the list?")
lists.remove(6)

print(lists)

# Copy list1 to list2
print("Copy list1 to list2")
list2=lists.copy()

print(lists)
print(list2)

# Reverse the list2
print("Reverse the list2")
list2.reverse()

print("This is list1",lists)
print("This is list2",list2)


