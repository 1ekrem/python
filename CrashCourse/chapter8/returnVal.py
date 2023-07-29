def get_formatted(firstname, lastname):
    """Return a full name, neatly formatted."""
    fullName = firstname + ' ' + lastname
    return fullName.title()

#musician = get_formatted("ekrem", "ersayin")
#print(musician)
#
#print("------------ NEW LINE ------------")

def get_formatted_middle(firstname, lastname, middlename=''):
    """Return a full name, neatly formatted."""
    if middlename:
        fullName = firstname + ' ' + middlename + ' ' + lastname
    else:
        fullName = firstname + ' ' + lastname
    return fullName.title()

#middleName = get_formatted_middle("daria", "vizniuk","Mihalylova")
#print(middleName)
#middleName = get_formatted_middle("daria", "vizniuk")
#print(middleName)

while True:
    print("\nPlease tell me your name or type 'stop' to end the program")
    f_name = input("Please enter your first name: ")
    if f_name.lower() == 'stop':
        print("The process has been completed. Please run again!")
        break
    
    l_name = input("Please enter your last name: ")   
    formatted_name = get_formatted(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
