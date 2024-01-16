#!/usr/bin/python3

"""prints the ASCII alphabet, in lowercase"""
for alpha in range(97, 123):
    if chr(alpha) != 'q' and chr(alpha) != 'e':
        print("{}".format(chr(alpha)), end="")
