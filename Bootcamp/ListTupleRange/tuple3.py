imelda="More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3,"Mayhem"), (4,"Kentish Town Waltz")
)

print(imelda)

title, artist, year, tracks = imelda

print(imelda)

print(title)
print(artist)
print(year)

for song in tracks:
    track, title = song
    #print(song)
    print("Track number {}, Title: {}".format(track, title))


tracks.