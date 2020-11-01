
# Save each of the following exercises as a separate file with a name like
# name_cases.py. If you get stuck, take a break or see the suggestions in
# Appendix C.
# 2-3. Personal Message: Store a person’s name in a variable, and print a message
    # to that person. Your message should be simple, such as, “Hello Eric,
    # would you like to learn some Python today?”
# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s
    # name in lowercase, uppercase, and titlecase.
# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
    # quote and the name of its author. Your output should look something like the
    # following, including the quotation marks:
    # Albert Einstein once said, “A person who never made a
    # mistake never tried anything new.”
# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s
    # name in a variable called famous_person. Then compose your message
    # and store it in a new variable called message. Print your message.
# 2-7. Stripping Names: Store a person’s name, and include some whitespace
    # characters at the beginning and end of the name. Make sure you use each
    # character combination, "\t" and "\n", at least once.
    # Print the name once, so the whitespace around the name is displayed.
    # Then print the name using each


# 2-3. Personal Message:
firstName = 'Daria'
print("Hello" + " " + firstName + ", would like to learn some Python today?")
print("Hello {}, would like to learn some Python today?".format(firstName))

# 2-4. Name Cases:
print("-"*10)
name1 = 'Ekrem'
nlower = name1.lower()
nupper = name1.upper()
ntitle = name1.title()

print(nlower)
print(nupper)
print(ntitle)

print("-"*10)
# 2-5. Famous Quote:

author = "Albert Einstein"
quote = '"A person who never made a mistake never tried anything new"'

print(author, "once said,",quote)

print("-"*10)

# 2-7. Stripping Names:



