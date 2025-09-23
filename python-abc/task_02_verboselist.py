#!/usr/bin/python3
"""
This module defines the VerboseList class that extends the list type.
"""


class VerboseList(list):
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, nb_of_item):
        count = len(nb_of_item)
        print(f"Extended the list with [{count}] items.")
        super().extend(nb_of_item)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
