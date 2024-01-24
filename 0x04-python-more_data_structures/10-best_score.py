#!/usr/bin/python3

def best_score(a_dictionary):
    """return bigger key integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    retn = list(a_dictionary.keys())[0]
    bigger = a_dictionary[retn]
    for x, y in a_dictionary.items():
        if y > bigger:
            bigger = y
            retn = x
    return (retn)
