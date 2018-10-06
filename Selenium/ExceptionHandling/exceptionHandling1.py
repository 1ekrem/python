# https://docs.python.org/3/library/exceptions.html


def exceptionHandling(b, c):
    try:
        a = 10
        b = b
        c = c

        d = (a+b)/c
        print(d)

    # except ZeroDivisionError:
    #     print("Zero Division ERROR - Good Catch")
    # except TypeError:
    #     print("Can't add string to an integer")
        
        #FORMAL WAY
    except:
        print("In the except block")

    
exceptionHandling(5, 0)