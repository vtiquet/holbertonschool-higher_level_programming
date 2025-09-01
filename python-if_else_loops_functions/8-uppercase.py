#!/usr/bin/python3
def uppercase(str):

    new_string = ""
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
            new_string += uppercase_char
        else:
            new_string += char
    print(new_string)
