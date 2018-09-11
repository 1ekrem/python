welcome = "Big Short", "Documentary", 2014
bad = "Bad Company", "Bad Company", 1974
metallica = "Ride the Lightining", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

print("="*40)

# You can only restore the values in a tuple since tuples are immutable
#metallica[1]="Master of puppets" #This wont work!
bad = bad[0], "Burhan Altintop", bad[2]
print(bad)

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0]="Master of Puppets"
print(metallica2)


print("Tuple is created with ''x'")
print("list is created with ['' ''] ")
print("Range is created with ('')")

#Tuples are expected to hold heterogeneous items like, string, string, int


