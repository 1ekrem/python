import zipfile

archive =zipfile.ZipFile('test.zip', 'r')
with archive.open('squares.txt') as txtFile:
    lines = txtFile.readlines()
    for line in lines:
        print(line.decode('ascii'), end="")


# 1) create a zip file
# 2) read that zip file contents
# 3)compose a email with above contents
# 4) send the email

#With is a block starter

#txtfile = archive.open('squares.txt') -- 
#print("Name of the text file is: ", txtfile.name)