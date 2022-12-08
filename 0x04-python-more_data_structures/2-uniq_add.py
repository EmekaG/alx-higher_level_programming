#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = 0
    for e in set(my_list):
        res += e
    return (res)
