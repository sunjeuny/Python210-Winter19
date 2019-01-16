#---------------------------------------- #
# Title: pos_neg.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


#  Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a,b, negative):
    # b is negative case option
    if a > 0 and b < 0 and negative == False:
        return True
    # a is negative case option
    elif a < 0 and b > 0 and negative == False:
        return True
    # Both Negative Option
    elif a < 0 and b < 0 and negative == False:
        return False
    # Negative flag is set to "True"
    elif a < 0 and b < 0 and negative == True:
        return True
    else:
        return False

test1 = pos_neg(1,-1,False)
test2 = pos_neg(-1,1,False)
test3 = pos_neg(-4,-5,True)
test4 = pos_neg(-4,-5,False)

print(test1)
print(test2)
print(test3)
print(test4)
