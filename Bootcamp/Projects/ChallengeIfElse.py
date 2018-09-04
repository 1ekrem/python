#Section 6 Lecture 32

# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person is
# the right age to go o an 18-30 holiday (They must be over 18 and under 31.)
# If they are, welcome them to the holiday, otherwise print
# a polite message refusing them enter.

name = input("Please type your name:\n")
age = int(input("Please type your age:\n"))

if 18<=age<31:
    print("Welcome to the Holiday Inn, {0}. Enjoy your vacation!!".format(name))
else:
    print("Due to exceeded number of reservations, we will not be able to accept you. Sorry!")
    print("Thank your for your interest in our resort!")