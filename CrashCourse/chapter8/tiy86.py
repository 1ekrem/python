"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
"""

def city_country(cityName, countryName):
    return  (cityName + ", "+ countryName)

city_1 = city_country("Santiago", "Chile")
print(city_1)

city_2 = city_country("New York City", "NY")
print(city_2)

city_3 = city_country("Barcelona", "Spain")
print(city_3)

print("------- NEW LINE --------")

"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album."""

def make_album(artistName, albumTitle, numberofTracks=''):
    album = {
        'Artist Name': artistName, 
        'Album Title': albumTitle
        }
    
    if numberofTracks:
        album['Number of Tracks'] = numberofTracks
    
    return album

artist1 = make_album("Ekrem", "Hello1")
artist2 = make_album("Daria", "Sensitive2")
artist3 = make_album("Pupsik", "Always Hungry", 3)

print(artist1)
print(artist2)
print(artist3)
     

"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""

user_question = input("\nWould you like me to ask you some questions?: ")
if user_question.title() == 'Yes':
    while True:
        print("If you would like me to stop, please type 'stop' below")
        artist_name = input("Enter Artist's name: ")
        if  artist_name == 'stop':
            break
        album_title = input("Enter Artist's album title: ")
        artist_generation = make_album(artist_name,album_title)
        print(artist_generation)
        
        