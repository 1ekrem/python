def greet_user(xname):
    """Display a simple greeting."""
    print("Hello {}!".format(xname))


name = input("Enter your name: ")

if name.title() == 'Ekrem':
    greet_user(name.title())
else:
    print("Bye Bye {}".format(name.title()))