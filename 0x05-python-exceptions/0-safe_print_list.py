#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            cnt = cnt + 1
        except IndexError:
            continue
    print("")
    return cnt
