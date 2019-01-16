#---------------------------------------- #
# Title: front_times.py
# Change Log: KCreek, 1/10/2018, Rev New
# KCreek, 1/10/2019, Created File
#---------------------------------------- #

# Given a string and a non-negative int n, we'll say that the front of the string is the first 3
# chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str,n):
    if len(str) < 3:
        return str*n
    else:
        newStr = str[0:3]
        return newStr*n

test1 = front_times('Chocolate',2)
test2 = front_times('Chocolate',3)
test3 = front_times('Abc',3)
test4 = front_times('ab',5)

print(test1)
print(test2)
print(test3)
print(test4)