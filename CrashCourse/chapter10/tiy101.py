"""
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... 

Save the file as learning_python.txt in the same directory as your exercises from this chapter. -- Done 

Write a program that reads the file and prints what you wrote three times.  -- Done

Print the contents once by reading in the entire file, 
once by looping over the file object, 
and once by storing the lines in a list 
and then working with them outside the with block.
"""

fileName = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//learning_python.txt'

with open(fileName) as file :
    file_content = file.readlines()
   
outside_block = []

for file_con in file_content:
    outside_block.append(file_con.rstrip())
    #print(file_con)
        #print(file_con.rstrip())

print(outside_block)

"""
try:
    with open(fileName) as file :
        file_content = file.read()
        print(file_content)
except FileNotFoundError:
    print("Sorry no file found.")

print("---- NEW LINE ----")
    
try:
    for i in range (0,3):
       with open(fileName) as file :
            file_content = file.read()
            print(file_content)
except FileNotFoundError:
    print("Sorry no file found.")

print("---- NEW LINE ----")
"""

"""
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:

message = "I really like dogs."
message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""

print("---- NEW LINE ----")
file2 = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//cat.txt'

with open(file2) as file2_v:
    reading = file2_v.read()
    print(reading)
    
    reading_changed = reading.replace("cats", "cars")
    print(reading_changed)

print("---- NEW LINE ----")
file2 = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//learning_python.txt'

with open(file2) as file2_v:
    reading = file2_v.read()
    print(reading)
    
    reading_changed = reading.replace("python", "C")
    print(reading_changed)
    