def greet_users(names):
    """Print a simple greeting message to each user"""
    
    for name in names:
        message = "Hello " + name
        print(message)

usernames = ['Ekrem', 'Kerem', 'Merke']
greet_users(usernames)