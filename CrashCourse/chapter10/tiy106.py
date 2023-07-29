"""
10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
When you try to convert the input to an int, you’ll get a TypeError. 
Write a program that prompts for two numbers. Add them together and print the result. 
Catch the TypeError if either input value is not a number, and print a friendly error message. 
Test your program by entering two numbers and then by entering some text instead of a number.
"""

while True:
    try:
        number1 = input("Please enter number 1\n")
        number2 = input("Please enter number 2\n")
        process = int(number1)//int(number2)
        print(process)
        answer1 = input('Would you like to run the program again? y/n \n')
        if answer1 == 'n':
            break
    except ValueError:
        print("Please enter only numbers")
        answer2 = input('Would you like to run the program again? y/n \n')
        if answer2 == 'n':
            break
        