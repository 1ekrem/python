from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("Enter your name: ")
    if first.lower() == 'q':
        break
    last = input("Enter your last name: ")
    if last.lower() == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\t Neatly formatted name: " + formatted_name + ".")