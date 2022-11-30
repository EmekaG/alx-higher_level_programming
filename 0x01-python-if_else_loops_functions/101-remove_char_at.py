#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    alph = 0
    for c in str:
        if alph != n:
            new += c
        alph += 1
    return new
