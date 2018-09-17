#TUPLE
# city_pop=("New York", 1000*1000*25)

# print("City: ",city_pop[0], " Population: ",city_pop[1])

# str="Hello"
# length =len(str)
# string = str[0:length:2]
# print(string)

str = "Code"

result=""
for i in range(len(str)):
    result=result+str[:i+1]
print(result)
