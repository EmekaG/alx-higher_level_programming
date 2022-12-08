#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    gloss = a_dictionary.copy()
    list_keys = list(gloss.keys())

    for i in list_keys:
        gloss[i] *= 2

    return (gloss)
