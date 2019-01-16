#---------------------------------------- #
# Title: not_string.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    if str[0:3] == "not":
        print(str)
    else:
        output = "not " + str
        print(output)


test = "not test"
not_string(test)
test2 = "Lucy"
not_string(test2)
