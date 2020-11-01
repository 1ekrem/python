user_0 = {'username':'papi',
          'f_name':'ekrem',
          'l_name': 'ersay'}

for user_key, user_value in user_0.items():
    print(user_key.title(),user_value.title())
    
fav_lang = {
    'phil':'python',
    'jacob':'C',
    'ramazan':'sql',
    'burhan':'python',
    'yanik':'java',
    'mike':'javascript'
            }

friends = ['phil','ramazan']
for key_v, val_v in fav_lang.items():
    print(key_v)
    
    if key_v in friends:
        print("Hi " + key_v.title() + '!' +
              ", I see that your favorite language is {}".format(val_v))

if 'erin' not in fav_lang.keys():
    print("Erin, please take our poll!")
    
print('\n ------------------------ NEW LINE ------------------------')

for keyx in sorted(fav_lang.keys()):
    print(keyx)
    
print('\n ------------------------ NEW LINE ------------------------')

for valx in sorted(fav_lang.values()):
    print(valx)

print('\n ------------------------ NEW LINE ------------------------')

for valx in sorted(set(fav_lang.values())):
    print(valx)