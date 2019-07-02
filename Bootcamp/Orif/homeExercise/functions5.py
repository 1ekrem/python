def calc_3rdpower(start, end):
    squares=[]

    for number in range(start, end):
        squares.append(number**3)
    print(squares)

def addition_numbers(end):
    total=0

    for i in range (end+1):
        total= total+i
    
    print (total)
