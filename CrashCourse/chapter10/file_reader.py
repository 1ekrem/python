
filepath = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//pi_digits.txt'

#with open(filepath) as file_object:
#    for line in file_object:
#        print(line.rstrip())
    #contents = file_object.read()
    #print(contents.rstrip())


with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))