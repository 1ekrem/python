with open("/Users/ersekrem/Documents/ClassAso/Orif/files/read_file.py") as source:
    lines = source.readline()
    for line in lines:
        print(line.rstrip())#