import json

def favorite_number():
    location = 'C://PythonClass//CrashCourse//chapter10//jsonFiles//'
    filename = 'favoriteNumber'
    extention = '.json'
    fullpath = location+filename+extention

    answer = int(input("Enter your favorite number: \n"))

    with open(fullpath, 'w') as file_object:
        json.dump(answer, file_object)

    with open(fullpath, 'r') as file_object2:
        number = json.load(file_object2)
        print("I know your favorite number! It is " + str(number) + "!")
        
favorite_number()