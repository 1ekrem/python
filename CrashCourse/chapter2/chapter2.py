

var1= "Given Name"

print(var1)

var1 = "Give Name has changed to 'Papichulo'"

print(var1)

var2 = 'ekrem' 
var3 = 'Ersayin'

#title function 
print(var2.title())

print("-"*50)

#upper and lower function
print(var2.upper())
print(var3.lower())

var2 = var2.upper()
print("Var2 has changed to", var2)

#Concat
fname = 'ekrem'
lname = 'ERSAYIN'
fullName = fname + " " + lname

print("Printing Full Name: ",fullName)
print("Printing Titles :", fname.title(), lname.title())

print("-"*50)
# Adding Whitespaces to Strings \t, \n
codingLan = "Languages: PythonJavaC++C"
print(codingLan)

codingLan = "Languages:\nPython\nJava\nC++\nC"
print(codingLan)

codingLan = "Languages:\tPython\tJava\tC++\tC"
print(codingLan)