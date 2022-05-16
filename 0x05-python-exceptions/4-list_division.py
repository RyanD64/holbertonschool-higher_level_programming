#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    comp = 0
    length = []
    while comp < list_length:
        try:
            result = my_list_1[comp] / my_list_2[comp]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            comp += 1
            length.append(result)
    return length
