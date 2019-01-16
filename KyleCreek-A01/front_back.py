#---------------------------------------- #
# Title: front_back.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


# Given a string, return a new string where the first and last chars have been exchanged

def front_back(str):
    new_word = str[-1] + str[1:-1] + str[0]
    print(new_word)

front_back('code')
front_back('a')
front_back('ab')
front_back('Kyle')
front_back("lucy")
front_back("expelliarmus")



