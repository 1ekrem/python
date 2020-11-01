pizza = {'crust': 'thick',
         'toppings': ['mushroom', 'tomato', 'olive']}

#Summerize the order
print("You ordered " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t"+topping)
    
    
portfolio = {'product_class':'equity',
             'tickers': ['MSFT','AMD','BA','DKNG']}


print("\n ---------------------- NEW LINE --------------------")    

for ticker in portfolio['tickers']:
    print("\t" + ticker)

print("\n ---------------------- NEW LINE --------------------")    

users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },

        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            },
        }

for username in users.items():
    print("\n username: " , username)


