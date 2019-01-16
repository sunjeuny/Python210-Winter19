#---------------------------------------- #
# Title: missing_char.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
    front = str[:n]
    back = str[n+1:]
    print(front + back)

missing_char("kitten",1)
missing_char("kitten",0)
missing_char("kitten",4)
