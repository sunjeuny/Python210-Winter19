#---------------------------------------- #
# Title: front3.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. 
# Return a new string which is 3 copies of the front.

def front3(str):
    if len(str) <= 3:
        print(str*3)
    else:
        sliceword = str[0:3]
        print(sliceword*3)

front3("Java")
front3("Chocolate")
front3("ab")
front3("abc")