import random
import os

random_nr = random.randint(0,100)

def write_squares(nrange, power):
    global file_name
    file_name="write_file"+str(random_nr)+".txt"
    with open(file_name, "w+") as writing:
        
        for i in range(nrange):
            lines = writing.write(str(i**power)+ " ")
        
        writing.close()

def read_written_file():
    with open(file_name, 'r') as reading:
        lines=reading.readlines()
        
        for line in lines:
            print(line.rstrip())

write_squares(10,2)
read_written_file()

