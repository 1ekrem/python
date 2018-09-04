number = "9,223,372,036,854,775,807"
cleaned_number = ''

for char in number:
    if char in '0123456789':
        cleaned_number = cleaned_number + char
new_number = int(cleaned_number)
print("This number is {} ".format(new_number))

#The important point in this script is the location of the print statement.
#If the print statement is under the if statement than it will keep printing the numbers
#If the print statement is under the for loop than it will print only once. TRY! 
new_number2= ''
for char in number:
    if char in '0123456789':
        new_number2 = new_number2+char    
        print(new_number2)