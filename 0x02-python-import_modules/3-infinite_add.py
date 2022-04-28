#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arguments = len(argv)
    index = 1
    addres = 0
    while index <= arguments:
        addres += int(sys.argv[index])
        index += 1
    print(f"{addres}")
