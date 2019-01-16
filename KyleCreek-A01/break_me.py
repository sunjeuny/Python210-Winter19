#---------------------------------------- #
# Title: break_me.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


def ErrorName():
    print(hello)

try:
    ErrorName()
except NameError:
    print("Name Error Has been produced")


def ErrorType():
    print(2 + "l")

try:
    ErrorType()
except TypeError:
    print("Type Error has been producted")

#def ErrorSyntax():
#    while True


def ErrorAttribute():
    lststuff = []
    print(lststuff.test())


ErrorAttribute()
