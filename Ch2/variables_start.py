
# Example file for variables


# Declare a variable and initialize it
f = 0
# print(f)

# re-declaring the variable works
# f = "abc"
# print(f)

# ERROR: variables of different types cannot be combined
# print("This is a string"+str(123))

# Global vs. local variables in functions


def someFunc():
    global f
    f = "def"
    print(f)


someFunc()
print(f)
print(type(f))

del f
print(f)
