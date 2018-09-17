with open("/Users/ersekrem/Documents/ClassAso/Orif/files/read_file2.py", "a") as source:
    for num in range(1,3):
        source.writelines(str(num*num))
    14