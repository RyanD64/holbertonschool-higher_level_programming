#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    idx = 0
    for index in str_list:
        if index == 'C' or index == 'c':
            str_list[idx] = ""
        idx += 1
    return "".join(str_list)
