#---------------------------------------- #
# Title: array_count9.py
# Change Log: KCreek, 1/10/2018, Rev New
# KCreek, 1/10/2019, Created File
#---------------------------------------- #

# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
    count = 0
    for number in nums:
        if number == 9:
            count += 1
    return count

test1 = array_count9([1,2,9])
test2 = array_count9([1,9,9])
test3 = array_count9([1,9,9,3,9])
test4 = array_count9([1,2,3,4,5])

print(test1)
print(test2)
print(test3)
print(test4)