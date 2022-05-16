#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print(f"{value}")
        return True
    except (ValueError, TypeError):
        print(f"Exception: {sys.exc_info()[1]}", file=sys.stderr)
        return(False)
