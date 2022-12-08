#!/usr/bin/python3

def roman_to_int(roman_string):
    # convert a roman numeral to an integer.
    if not roman_string or type(roman_string) != s:
        return (0)
    n = 0
    glossary = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        figures = glossary[roman]
        n += figures if n < figures * 5 else -figures
    return (n)
