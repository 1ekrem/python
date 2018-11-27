# def add_this(a: int, b: int) -> int:
#     return 'hello'

# print(add_this(2,3))


# x = '           Ekrem Ersayin     '

        #List
# list = ['25%','50%', '90%']

# print(min(list))

##
# d={"name": "Ekrem", "lastname": "Ersayin"}
# print(d.keys())
# print(d.values())
# print(d["name"])

# print("*"*50)
# d2 = {}
# d3 = {}
# for k, v in d.items():
#     d2[k]=v
#     print(d2.keys())
#     print(d2.values())
#     print(d2["name"])

#     d3[v]=k
#     print(d3.keys())
#     print(d3.values())
#     print(d3["Ekrem"])

# list1 = ['50%', '70%']
# list2 = ['Rolex','Hublot']

# print(list1)
# print(list2)
# list3 = dict(zip(list2,list1))

# print(list3)

# import datetime

# date = datetime.datetime.today()
# print(date)


# Store square of numbers in x list.
x = []
for y in range(10+1):
    x.append(y)

squares = []
third_power = []
fourth_power = []
fifth_power = []
sixth_power = []
seventh_power = []
eighth_power = []
nineth_power = []
tenth_power = []
for i in x:
    squares.append(i**2)
    third_power.append(i**3)
    fourth_power.append(i**4)
    fifth_power.append(i**5)
    sixth_power.append(i**6)
    seventh_power.append(i**7)
    eighth_power.append(i**8)
    nineth_power.append(i**9)
    tenth_power.append(i**10)
print(squares)
print(third_power)
print(fourth_power)
print(fifth_power)
print(sixth_power)
print(seventh_power)
print(eighth_power)
print(nineth_power)
print(tenth_power)