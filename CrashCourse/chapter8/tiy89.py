"""8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list."""


def show_magicians(magicians):
    for name in magicians:
        print(name)
        
names = ['Ekrem', 'Daria', 'Pupsik']
show_magicians(names)



"""8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified."""
print("--- New line ---")

def show_magicians2(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    
    #Building a new list to hold great magicians
    great_magicians = []

    #Make each magician great, and add it to great_magician
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append (great_magician)
        
    for great_magician in great_magicians:
        magicians.append(great_magician)    
        
m_names = ['Tapar', 'Sencer', 'Hasan Sabbah']
show_magicians2(m_names)
print("--- New line ---")
make_great(m_names)


"""8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name. """

print("8-11")

