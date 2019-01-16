#---------------------------------------- #
# Title: string_splosion.py
# Change Log: KCreek, 1/9/2018, Rev New
# KCreek, 1/9/2019, Created File
#---------------------------------------- #


#  Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    new_string = ""
    counter = 0
    while counter < len(str) + 1:
        new_string = new_string + str[0:counter]
        counter += 1
    
    print(new_string)

string_splosion("code")
string_splosion("abc")
string_splosion("Kyle")
