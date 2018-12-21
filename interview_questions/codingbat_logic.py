# str = 'hiABChi  hi'
# a=0

# for i in range(len(str)-1):
#     if str[i] == 'h' and str[i+1] =='i':
#         a = a + 1
# print(a)


# str = 'catdogcat'
# ncat = 0 
# ndog = 0
# for i in range(len(str)-1):
#     if str[i]=='c' and str[i+1]=='a' and str[i+2]=='t':
#         ncat += 1
#     if str[i]=='d' and str[i+1]=='o' and str[i+2]=='g':
#         ndog += 1
# print(True if ncat == ndog else False)
# print(True if str.count('cat')==str.count('dog') else False)

i= 1
while i <= 100:
    i += 1
    if i==5:
        continue
    print(i, "NAME")
