#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    comp = 0
    miss = 0
    while comp < x:
        try:
            print(f"{my_list[comp]}", end='')
            comp += 1
        except (ValueError, TypeError):
            comp += 1
            miss += 1
    comp -= miss
    print()
    return comp
