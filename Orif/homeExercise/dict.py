post2 = dict(message= "SS Cotopaxi", language="English")
#print(post2)

post2["user"]="Ekrem"
post2["datetime"] = "19771116t0"

#print(post2)

#print(post2["language"], post2["user"])

search= input("Please type the keyword: ")
if search in post2:
    print(post2[search])
else:
    print("The post2 dictionary doens't contain the keyword {}".format(search))


# Handling exceptions
try:
    print(post2[search])
except KeyError:
    print("The dict does not have a {} value".format(search))

#iterate all the keys and values

for key in post2.keys():
    value=post2[key]
    print(key, "=", value)

print("="*40)

for i in post2.keys():
    print("i = ", i)
    print("post2[i] = ", post2[i])
