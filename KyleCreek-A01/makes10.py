#---------------------------------------- #
# Title: makes10.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a,b):
    if a + b == 10 or a == 10 or b == 10:
        return True
    else:
        return False

test1 = makes10(10,9)
test2 = makes10(5,5)
test3 = makes10(2,2)
test4 = makes10(7,10)


print(test1)
print(test2)
print(test3)
print(test4)