'''
Creating the __init__.py file means that the my_sum folder can be imported 
as a module from the parent directory.
'''

def sum(arg):
    total = 0
    for val in arg:
        total = total + 1
    
    return total