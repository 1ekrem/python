city_pop_list={"Tokyo": 11*1900*2000, 
"Paris": 5*20000*6000,
"Istanbul": 9*1000*20000,
"Seoul": 9*2000*2000,
"New York": 8*1500*8000,
"New Jersey": 8*1500*8000
}

print("City", "Population")
print("------------------")

for city_name in city_pop_list:
    print(city_name, city_pop_list[city_name])


print("Sorted by their populations")
print("City", "Population")
print("------------------")

print()
#Orif's Logic
sorted_by_pop = {}
for city_name in city_pop_list:
    population = city_pop_list[city_name]
    sorted_by_pop[population]=city_name

for population in sorted(sorted_by_pop.keys()):
    print(sorted_by_pop[population], population)