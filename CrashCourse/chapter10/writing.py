filename = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming \n")
    file_object.write("I love creating new games.\n")
    

with open(filename, 'a') as file_object2:
    file_object2.write("++ i love adding new lines\n")
    file_object2.write("++ i love 2  new lines")