# How to remove a value from a dictionary

alien_0 = {'color':'red','point':'5'}

print(alien_0)

del alien_0['point']
print(alien_0)

# How to save a dictionary of Similar Objects

fav_lang = {
    'phil':'python',
    'jacob':'C',
    'ramazan':'sql',
    'burhan':'python',
    'yanik':'java',
    'mike':'javascript'
}

print("Burhan's favorite language is "+
      fav_lang['burhan'].title() + "."
      )

new_dict = {key:val for key, val in fav_lang.items() if key != 'phil'}
print(new_dict)