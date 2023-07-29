'''
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.

10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.

10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
'''

filename = "C://PythonClass//CrashCourse//chapter10//sampleFiles//guests.txt"
name = str(input("Can you please enter your name?: \n"))
name2 = ('{}\n').format(name)

try:
    with open(filename) as read_object:
            cont = read_object.readlines()
            cont2 = []
            for i in cont:
                cont2.append(i.rstrip())
            if name not in cont2:
                 with open(filename, 'a') as file_object:
                    file_object.write(name2)
                    print(name + " is added to the guests list. Thank you!")   
            else:
                print(name + " is in the guest list")
                print("Current Names in the file: ", cont2)
except FileNotFoundError:
    print("File not found.")
        

print("--- NEW LINE ---")
"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename105 = 'C://PythonClass//CrashCourse//chapter10//sampleFiles//filename105.txt'

responses = []
while True:
    response = input("Why do you like programming?:\n")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename105, 'w') as f:
    for i in responses:
        f.write(i + "\n")