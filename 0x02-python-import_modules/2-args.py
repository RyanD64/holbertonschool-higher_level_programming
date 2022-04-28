#!/usr/bin/python3
import sys
argv = sys.argv[1:]
arguments = len(argv)
index = 1
if arguments == 0:
    print(f"{arguments} arguments.")
elif arguments == 1:
    print(f"{arguments} argument:")
    print(f"{arguments}: {sys.argv[1]}")
else:
    print(f"{arguments} arguments:")
    while index <= arguments:
        print(f"{index}: {sys.argv[index]}")
        index += 1
