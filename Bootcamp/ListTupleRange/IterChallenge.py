name_list=["ekrem", "burhan", "mehmet", "ahmet", "John", "Denise", "Micheal", "Nicky"]
my_iterator = iter(name_list)

x=len(name_list)
for i in range(x):
    next_name = next(my_iterator)
    print(next_name)