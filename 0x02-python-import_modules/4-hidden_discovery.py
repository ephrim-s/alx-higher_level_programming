#!/usr/bin/python3

if __name__ == "__main__":
    """print names of hidden module"""

    import hidden_4

    lst = dir(hidden_4)
    for name in lst:
        if name[:2] != "__":
            print(name)
