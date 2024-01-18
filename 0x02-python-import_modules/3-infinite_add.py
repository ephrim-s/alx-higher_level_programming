#!/usr/bin/python3

if __name__ == "__main__":
    """display the additions of all arguments"""
    import sys

    total_args = 0
    for x in range(len(sys.argv) - 1):
        total_args += int(sys.argv[x + 1])
    print("{}".format(total_args))
