#!/usr/bin/python3
def magic_calculation(a, b):
    rslt = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("Too far")
            rslt += (a ** b) / x
        except Exception:
            rslt = b + a
            break
    return rslt