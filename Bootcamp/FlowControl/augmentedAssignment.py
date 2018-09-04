# Augmented assignment is the combination, in a single statement, of a binary operation and an assignment statement:

# augmented_assignment_stmt: target augop expression_list
# augop:           "+=" | "-=" | "*=" | "/=" | "%=" | "**="
#                | ">>=" | "<<=" | "&=" | "^=" | "|="
# target:          identifier | "(" target_list ")" | "[" target_list "]"
#                | attributeref | subscription | slicing


print("Good Morning")
print("Good Morning\n"*5)

x=23
x+=1
print(x)

x//=2
print(x)

x-=2
print(x)

x**=2
print(x)
