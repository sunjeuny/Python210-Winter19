#---------------------------------------- #
# Title: install_test.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


import sys
print("This is my first Python program")

version = sys.version_info
version_string = "{}.{}".format(version.major,version.minor)

if version.major == 3:
    if version.minor not in (6, 7):
        print("You should be running 3.6 or 3,7")
    else:
        print("You are running python {} -- all good!".format(version_string))
else:
    print("You need to run Python 3!")
    print("This is version: {}".format(version_string))
