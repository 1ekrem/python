import json

def greet_user():
    """Greet the user by name"""
    location = 'C://PythonClass//CrashCourse//chapter10//jsonFiles//'
    filename3 = 'username'
    extention = '.json'
    fullpath = location+filename3+extention
    try:
        with open(fullpath, 'w') as file_object:
            json.dump(filename3,file_object)
    except FileNotFoundError:
        username = input('Please enter your name\n')
        with open(location+username+extention, 'w') as file_obj2:
            json.dump(username, file_obj2)
            
            
            