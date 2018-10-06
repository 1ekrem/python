def exceptionHandling(enter_key):

    try:
        car = {"make":"BMW", 
        "model":"325i", 
        "year":"2015"}

        print(car[enter_key])
    except KeyError:
        print("The value entered is not found")
    finally:
        print("Please enter a different value. Thanks!")

exceptionHandling('color')