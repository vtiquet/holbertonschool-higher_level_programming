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

    new_text = ""
    for char in text:
        new_text += char
        if char in ['.', '?', ':']:
            new_text += "\n\n"

    lines = new_text.split('\n')
    for line in lines:
        print(line.strip(' '), end="")
        if line != lines[-1]:
            print("")
