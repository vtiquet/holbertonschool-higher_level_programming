#!/usr/bin/python3
"""Function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout."""
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end="")
