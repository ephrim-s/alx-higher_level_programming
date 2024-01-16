#!/usr/bin/python3

"""prints numbers in two digits"""

for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
