'''
Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.         '''

person_1 = {'firstName':'daria',
            'lastName':'vizniuk',
            'catName':'pupsik',
            'age':'27',
            'catAge':'2',
            'city':'New York'
            }

print(person_1['firstName'].title())
print(person_1['lastName'].title())
print(person_1['catName'].title())
print(person_1['age'])
print(person_1['catAge'])
print(person_1['city'].title())

print("\n ------------ NEW LINE ------------ \n")
'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.'''

fav_num = {'daria':'5',
           'Ekrem':'7',
           'Pupsik':'1',
           'Papi':'2',
           'Jacob':'4',
           'Riyad':'6'
            }

for name, value in fav_num.items():
    print(name.title() + "'s favorite number is: " + fav_num[name])

print("\n ------------ NEW LINE ------------ \n")

for name1 in fav_num.keys():
    print(name1.title())

print("\n ------------ NEW LINE ------------ \n")

fav_lang = {
    'phil':'python',
    'jacob':'C',
    'Ekrem':'sql',
    'burhan':'python',
    'daria':'java',
    'mike':'javascript'
}

fav_num2 = {'daria':'5',
           'Ekrem':'7',
           'Pupsik':'1',
           'Papi':'2',
           'Jacob':'4',
           'Riyad':'6'
            }

for value1 in fav_num2.values():
    print(value1)

print("\n ------------ NEW LINE ------------ \n")

friends_list = ['daria', 'Ekrem']

for name2 in fav_lang.keys():
    print(name.title())
    
    if name2 in friends_list:
        print(" Hi " + name2.title() + 
            ", I see your favorite language is " +
            fav_lang[name2].title() + "!")