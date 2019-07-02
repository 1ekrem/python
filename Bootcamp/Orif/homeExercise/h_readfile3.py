# import functions5

# functions5.calc_3rdpower(1,5)
# functions5.addition_numbers(8)

# How to read files

def read_file(location):
    with open(location, "r") as source:
        lines = source.readlines()
        for line in lines:
            print(line.rstrip())


#read_file("C:/AsoPython/Orif/homeExercise/executable_file.txt")
