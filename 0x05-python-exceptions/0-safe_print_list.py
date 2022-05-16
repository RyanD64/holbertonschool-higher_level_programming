#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        comp = 0
        while comp < x:
            print(f"{my_list[comp]}", end='')
            comp += 1
        print()
        return comp
    except IndexError:
        print()
        return comp
        pass
