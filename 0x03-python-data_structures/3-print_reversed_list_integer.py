#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    for a in range(len(my_list)):
        print(my_list[a])
