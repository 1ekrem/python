# We will see the else block here

def exceptionHandling(b, c):
    try:
        a = 10
        b = b
        c = c

        d = (a+b)/c
        print(d)

    except:
        print("In the except block")
        raise Exception("This is an exception")
    else:
        print("Because there was no exception, else is being executed! - Everything works PERFECTLY!")
    finally: # Finally is the block that gets executed always!
        print("Finally, always executed")


    
exceptionHandling(5, 0)