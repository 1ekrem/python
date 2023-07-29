filename = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//alice.txt'

try:
    with open(filename) as fle:
        contents = fle.read()
        print(contents)
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)