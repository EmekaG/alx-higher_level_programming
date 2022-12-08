#!/usr/bin/python3

def roman_to_int(roman_string):
    # convert a roman numeral to an integer.
    if (not isinstance(roman_string, s) or
            roman_string is None):
        return (0)

    glossary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    n = 0

    for i in range(len(roman_string)):
        if glossary.get(roman_string[i], 0) == 0:
            return (0)
        if (i != (len(roman_string) - 1) and
                glossary[roman_string[i]] < glossary[roman_string[i + 1]]):
            n += glossary[roman_string[i]] * -1
    else:
        n += glossary[roman_string[i]]
    return (n)
