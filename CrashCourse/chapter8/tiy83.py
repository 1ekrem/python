"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""

def make_shirt(size, text):
    if size == 'Large':
        text = 'I love Python'
    
    print("\nThe size of the tshirt will be " + size)
    print("As per your request, the following message will be printed --> " + text)
    
make_shirt("Medium", "2020 IS MY YEAR!")
make_shirt(text='Im using Keyword argument', size='Large')
make_shirt(size='Large',text='Im using Keyword argument')

"""8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country."""

def describe_city(city, country = 'Iceland'):
    print(city + " is in " + country)
    
describe_city("Reykjavik")
describe_city(city="Istanbul", country='Turkey')