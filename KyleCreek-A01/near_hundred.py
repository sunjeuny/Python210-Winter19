#---------------------------------------- #
# Title: near_hundred.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    if n >= 90 or n >= 190:
        return True
    else:
        return False

test1 = near_hundred(89)
print(test1)
