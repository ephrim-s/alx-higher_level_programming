#!/usr/bin/python3

"""prints all possible combination"""

for dig1 in range(0, 10):
    for dig2 in range(dig1 + 1, 10):
        if dig1 == 8 and dig2 == 0:
            print("{}{}".format(dig1, dig2))
        else:
            print("{}{}".format(dig1, dig2), end=", ")
