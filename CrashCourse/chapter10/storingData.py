import json

number = [2, 3, 5, 7, 11, 13]

filename = 'C://PythonClass//CrashCourse//chapter10//jsonFiles//number.json'

print("--- Now Writing to the File ---")
with open(filename, 'w') as file_object:
    json.dump(number, file_object)
    
print("--- Now Reading the File ---")
with open(filename, 'r') as file2:
    numbers = json.load(file2)

print(numbers)

