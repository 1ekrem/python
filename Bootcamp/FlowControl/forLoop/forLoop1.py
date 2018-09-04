# for i in range(1,20):
#     print(i," is now {}".format(i))

number = "9,223,372,036,854,775,807"
cleaned_number = ''
for j in range(0, len(number)):
    if number[j] in '0123456789':
        cleaned_number = cleaned_number + number[j]
new_number = int(cleaned_number) # We keep this indention in the beginning because new_number should be stored only one.
print("The number is {} ".format(new_number))


