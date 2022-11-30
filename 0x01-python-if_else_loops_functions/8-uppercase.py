#!/usr/bin/python3
def alphupper(alph):
    if ord(alph) >= 97 and ord(alph) <= 122:
        return (ord(alph) - 32)
    else:
        return ord(alph)

def uppercase(string):
    string_new = ""
    for alph in string:
        string_new += "%c" % alphupper(alph)
        print("{:s}".format(string_new))
