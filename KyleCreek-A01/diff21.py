#---------------------------------------- #
# Title: diff21.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

def diff21(n):
    if n < 21:
        return 21 - n
    elif n > 21:
        return 2*(n - 21)
    elif n == 21:
        return 0

test1 = diff21(19)
test2 = diff21(10)
test3 = diff21(21)
test4 = diff21(40)


print(test1)
print(test2)
print(test3)
print(test4)
