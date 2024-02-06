#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    cnt = 0
    a = 0
    n_list = []
    for i in range(list_length):
        try:
            rslt = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            rslt = 0
        except ZeroDivisionError:
            print("division by 0")
            rslt = 0
        except IndexError:
            print("out of range")
            rslt = 0
        finally:
            n_list.append(rslt)
    return n_list
