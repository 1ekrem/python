name="ekrem"

#Option 1
print("Option 1")
backwards = name [::-1]
print(backwards)

#Option 2
print("Option 2")
for i in range(-1,-len(name)-1,-1):
    print (name[i],end=(""))
