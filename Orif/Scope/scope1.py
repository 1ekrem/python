
#Message is in GLOBAL scope
message = "Hello"


def print_message(msg):
    global message
    
    message="new message"
    print(message)

print(message)
print_message(message)