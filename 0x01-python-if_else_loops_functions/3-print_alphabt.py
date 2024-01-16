#!/usr/bin/python3

"""prints the ASCII alphabet, in lowercase"""
for alpha in range(97, 123):
    if chr(alpha) is not 'q' and chr(alpha) is not 'e':
        print("{}".format(chr(alpha)), end="")
