

def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin=(width-len(text))//2
    print(" "*left_margin, text)

def centre_text(text):
    left_margin=(80-len(text))//2
    print(" "*left_margin, text)

#Call the function
centre_text("spam ")
centre_text("spam and ")
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text("spam, spam, spam and eggs")



