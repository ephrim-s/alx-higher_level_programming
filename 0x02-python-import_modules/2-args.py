#!/usr/bin/python3

if __name__ == "__main__":
    """displays the number of args"""

    import sys

    lst = len(sys.argv) - 1
    if lst == 0:
        print("0 arguments.")
    elif lst == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(lst))
    for x in range(lst):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
