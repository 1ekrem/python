def reverse_string(w):
    rev = ''
    for i in range(len(w)):
        j = -(i+1)
        rev = rev + w[j]
    print(rev)


reverse_string('Ekrem')

x = 'Berken'
print(x[-2])