# x = "false"
# if x:
#     print("x is true")

# How to check if values are True or False
print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
""".format(False, bool(None), bool(0), bool(0.0), bool([])))