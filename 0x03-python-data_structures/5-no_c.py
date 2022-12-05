#!/usr/bin/python3

def no_c(my_string):
    new_str = ''
    for i in my_str:
        if i != 'c' && i != 'C':
            new_str += i
        return (new_str)
