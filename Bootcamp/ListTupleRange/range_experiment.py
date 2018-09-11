
o = range(0, 100, 2)
print(o)

p=o[1:11:2] #If modifications applied then 'p' range takes the multiplication of the incrementing value of the original range which is 'o' in our case.
print(p)

for i in p:
    print(i)

print(list(p))