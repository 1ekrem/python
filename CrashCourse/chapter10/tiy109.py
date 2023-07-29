"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.
"""

filename = ['cat', 'dog']
location = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//'
extension = '.txt'

def reader(location, filename, extension):
    fullpath = location+filename+extension
    try:
        with open(fullpath) as file_object:
            content = file_object.read()
            print(content)
    except FileNotFoundError:
        pass
        #print(filename + "is not located under the specified location")
        
#reader(location, 'cat', extension)

for name in filename:
    reader(location, name, extension)
    
filename1 = 'AliceInWonderland'
location1 = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//'
extension1 = '.txt'
fullpath = location1+filename1+extension1
with open(fullpath, encoding='utf8') as aliceW:
    cont = aliceW.read()
    cont = cont.rsplit()
    print(cont.count('Rabbit'))
    