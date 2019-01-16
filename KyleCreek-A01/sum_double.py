#---------------------------------------- #
# Title: sum_double.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a,b):
    if a == b:
        return 2*(a+b)
    else:
        return a + b

test1 = sum_double(5,5)
test2 = sum_double(2,7)

print(test1)
print(test2)
