def diplay_message():
    message = "In this chapter we are learning about how the functions are used in programming"
    print(message)
    
diplay_message()

def favorite_book(title):
    print("My favorite book is {}".format(title))

favorite_book(input())

bookList = ['Kral', 'Dostum', 'Yanlizlik']

for name in bookList:
    favorite_book(name)