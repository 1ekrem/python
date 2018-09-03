parrot="Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[1])
print(parrot[-1]) # Count backwards. It will begin printing from the last button.
print(parrot[0:6]) # It'll take up to 6 indexes -- Norweg
print(parrot[:6]) # It'll take up to 6 indexes beginning from the 0th index -- Norwe
print(parrot[6:]) # Will print from 6th index to the end --ian Blue
print(parrot[-4:-2])
print(parrot[0:6:2])# take up to 6th index but skip 2 characters at a time
print(parrot[0:6:3])# take up to 6th index but skip 3 characters at a time

number = "9,233-372+036/854&775^807"
print(number[1::4]) # Start from the 1th index and print every other 4th character.


numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3]) #Start from the 0th index and print every other 3rd character. 
# This should print 1 and skip 3 characters than print the 3th one. 
#The slice starts at the first character, and includes every 3th character.

string1="he's "
string2="probably"
print(string1+string2)
print("he's probably pining")
print("hello "*5)
print("hello "*(5+4))
print("hello "*5+"4")

print()
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print("we want to slice the string to extract just the digits.")
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9" 
print(numbers[0::3])