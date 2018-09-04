number = "9,223,372,036,854,775,807"
cleaned_number = ''

for char in number:
    if char in '0123456789':
        cleaned_number = cleaned_number + char
new_number = int(cleaned_number)
print("This number is {} ".format(new_number))


for char in number:
    if char in '0123456789':
        print(char)