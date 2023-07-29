listx = ['Ekrem', 'Daria', 'Jacob']

name = str(input("Enter Name\n"))

if name in listx:
    print(name + " is in the list")
else:
    print(name + " is not in the list and will be added.")
    listx.append(name)
    print(listx)