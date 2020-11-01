
list1 = ['Ekrem Ersayin', 'Papichulo', 'Daria Viznuik', 'Pupsick Vizniuk']

print(list1)

# for i in list1:
#     if i == "Jack":
#         list1.append("Papi chulo")
#     print(i)


print(list1[-4].title())

list1.append("NewVar")
print(list1)

list1.insert(1,"InsertedVar")
print(list1)

del list1[1]
print(list1)

list1.pop()
print(list1)

list1.remove("Papichulo")
print(list1)