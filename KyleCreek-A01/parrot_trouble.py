#---------------------------------------- #
# Title: parrot_trouble.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
    if talking == True and  (hour < 7 or hour > 20):
        return True
    else:
        return False
    

test = parrot_trouble(True,6)
test2 = parrot_trouble(True, 7)
test3 = parrot_trouble(False,6)

print(test)
print(test2)
print(test3)

    