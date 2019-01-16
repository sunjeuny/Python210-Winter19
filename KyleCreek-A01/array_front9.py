#---------------------------------------- #
# Title: array_front9.py
# Change Log: KCreek, 1/10/2018, Rev New
# KCreek, 1/10/2019, Created File
#---------------------------------------- #

# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.

def array_front9(nums):
    if 9 in nums[0:3]:
        return True
    else:
        return False

test1 = array_front9([1,2,9,3,4])
test2 = array_front9([1,2,3,4,9])
test3 = array_front9([1,2,3,4,5])
test4 = array_front9([1,2,3])
test5 = array_front9([1,2,9])

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)