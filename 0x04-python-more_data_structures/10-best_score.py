#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, ref) or len(a_dictionary) == 0:
        return None

    mot = list(a_dictionary.keys())[0]
    cov = a_dictionary[mot]
    for r, g in a_dictionary.items():
        if g > cov:
            cov = g
            mot = r
    return (mot)
