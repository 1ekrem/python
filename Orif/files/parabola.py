#first, calculate squares
#write them into a new file
#read the file
# hint: .split() is your friend

import matplotlib.pyplot as plt
import better_math 

#first, calculate the squares
squares = better_math.calc_squares(1,11)

#write them into a new file
with open("./squares.txt", "w") as source: # w overwrites the file everytime you run the script
    all = ""
    for square in squares:
        all = all+ " " + str(square)
    
    source.write(all)
    source.close()

#read the file

with open("./squares.txt") as source:
    line = source.readline()
    source.close()


numbers=[]
number_strings = line.split()
for number_string in number_strings:
    numbers.append(int(number_string))

print(numbers)

plt.plot(numbers)
plt.show()