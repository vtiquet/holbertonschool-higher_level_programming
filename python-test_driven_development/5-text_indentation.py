#!/usr/bin/python3
"""
This module contains the function text_indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 newlines after each '.', '?', and ':'.

    Args:
        text (str): The text to be processed.

    Returns:
        None.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = ""
    for i in text:
        x += i
        if i in ".?:":
            print(x.strip())
            print()
            x = ""
    if x.strip():
        print(x.strip(), end="")
