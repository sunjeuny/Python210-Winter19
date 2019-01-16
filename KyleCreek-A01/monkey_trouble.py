#---------------------------------------- #
# Title: monkey_trouble.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. 
# Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    else:
        return False

test = monkey_trouble(True, True)
test2 = monkey_trouble(False,False)
test3 = monkey_trouble(True, False)

print(test)
print(test2)
print(test3)
