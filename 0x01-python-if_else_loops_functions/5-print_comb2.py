#!/usr/bin/python3
for i in range(0, 100):
    print(F"{i:02d}", end=", ")
    if i == 99:
        print(F"{i:02d}", end="\n")
