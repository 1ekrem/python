def reverse_dictionary(input_dictionary):
    result= {}
    for key, value in input_dictionary.items():
        result[value] = key    
    return result


def print_dictionary(input_dictionary, key_caption, value_caption):
    print(key_caption, value_caption)
    print("------------------")
    
    for key, value in input_dictionary.items():
        print(key, value)


def print_city_pops(input_dictionary):
    print_dictionary(input_dictionary, "City", "Population")

city_pop_list={"Tokyo": 11*1900*2000, 
"Paris": 5*20000*6000,
"Istanbul": 9*1000*20000,
"Seoul": 9*2000*2000,
"New York": 8*1500*8000,
"New Jersey": 8*1500*8000
}

print_city_pops(city_pop_list)

#Pretty print cities and their population numbers ordered by population
print()

#Reverse Logic
reversed_dictionary = reverse_dictionary(city_pop_list)
sorted_dictionary ={}
#Let's adopt the code to the function
for population in sorted(reversed_dictionary.keys()):
    sorted_dictionary[reversed_dictionary[population]]=population

print("Sorted by their populations")
print_city_pops(sorted_dictionary)

