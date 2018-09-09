# You have a dictionary of cities with their population numbers. Print cities and their numbers in a pretty format:

# Sample: {"London": 9 * 1000 * 1000, "New York": 10 * 1000 * 1000}
# Pretty print:

# City  Population
# ----------------------
# London  9000000
# New York 10000000

# Now sort cities by their popultion numbers and print them:

# City  Population
# ----------------------
# New York 10000000
# London  9000000


city_pop_list={ "City": "Population",
"Tokyo": 11*1900*2000, 
"Paris": 5*20000*6000,
"Istanbul": 9*1000*20000,
"Seoul": 9*2000*2000,
"New York": 8*1500*8000,
"New Jersey": 8*1500*8000
}

print()
print("Formatted Print")
for keys,values in city_pop_list.items():
    if keys == "City":
        print(keys, ": ", values)
        print("----------------------")
        #continue
    else:
        print(keys, ": ", values)

print()
print("Formatted and Sorted Print")
for keys1,values2 in sorted(city_pop_list.items()):
    if keys1 == "City":
        print(keys1, ": ", values2)
        print("----------------------")
        continue
    else:
        print(keys1, ": ", values2)      

