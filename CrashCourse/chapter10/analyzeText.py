filename1 = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//AliceInWonderland.txt'
# encoding='utf8'
# To read this file, either indicate the encoding type or read it with 'read and binary' as 'rb' mode.
with open(filename1, encoding='utf8') as alice:
    contents = alice.read()
    words = contents.split()
    numberofwords = len(words)
    print(numberofwords)


def count_words(filename):
    location = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//'
    filetype = '.txt'
    filenamecon = location+filename+filetype
    try:
        with open(filenamecon, 'rb') as file_object:
            contents = file_object.read()
            word = contents.split()
            numberofwords = len(word)
        print(filename, "has the following number of words:", numberofwords)
    except FileNotFoundError:
        pass
        #print(filename+filetype + " file is not found")

filenames = ['alice', 'cat', 'filename105', 'AliceInWonderland', 'Hello']

for f in filenames:
    count_words(f)