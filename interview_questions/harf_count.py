list = ['a','b','c', 'a', 'b','d']
# for i in list:
#     my_dict = {i:list.count(i)}
#     print(my_dict)

my_dict = {i:list.count(i) for i in list}
print(my_dict)


#Pythonic version of counting duplicates
list = ['a','b','c', 'a', 'b','d']

my_dict = {i:list.count(i) for i in list}
print(my_dict)