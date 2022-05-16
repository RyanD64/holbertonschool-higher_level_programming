#!/usr/bin/python3
def safe_print_division(a, b):
    final = 0
    try:
        final = a / b
    except ZeroDivisionError:
        final = None
    finally:
        print("Inside result: {}".format(final))
        return final
