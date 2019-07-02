inputa = 'A11a4'
outputb = '411aA'
outputc = ''

lowerc = []
upperc = []
numeric = []
sorted_list = []

for i in inputa:
    if i.isnumeric():
        numeric.append(i)
        numeric.sort(reverse=True)
    if i.islower():
        lowerc.append(i)
    if i.isupper():
        upperc.append(i)

for item in (numeric, lowerc, upperc):
    sorted_list.extend(item)
print(sorted_list)

for i in sorted_list:
    outputc.join(str(i))

print(outputc)
