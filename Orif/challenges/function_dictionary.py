city_pop={"Tokyo": 11*1900*2000, 
"Paris": 5*20000*6000,
"Istanbul": 9*1000*20000,
"Seoul": 9*2000*2000,
"New York": 8*1500*8000,
"New Jersey": 9*1500*8000
}

def print_dictionary(input_dictionary, key_caption, value_caption):
    print(key_caption, value_caption)
    print("------------------------")

    for key, value in input_dictionary.items():
        print(key, value)

def sorted_values_function(input_dictionary):
    result={}
    for key, value in input_dictionary.items():
        result[value]=key
    return result

def print_city_pop(input_dictionary):
    print_dictionary(input_dictionary, "City", "Population")

print_dictionary(city_pop, "City", "Population")
#reversed_dictionary(city_pop)

reverse_dictionary = sorted_values_function(city_pop)
sorted_dictionary= {}

for population in sorted(reverse_dictionary.keys()):
    sorted_dictionary[reverse_dictionary[population]]=population

print()

print("Sorted bt their population")
print_city_pop(sorted_dictionary)
