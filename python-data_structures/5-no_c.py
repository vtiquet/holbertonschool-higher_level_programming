#!/usr/bin/python3
def no_c(my_string):
    list = ""
    list = [i for i in my_string if i != "c" and i != "C"]
    return ("".join(list))
