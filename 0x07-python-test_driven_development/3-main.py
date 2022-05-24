#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Wal#", "White")
say_my_name("1")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
