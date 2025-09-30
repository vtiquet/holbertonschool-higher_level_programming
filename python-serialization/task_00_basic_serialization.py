#!/usr/bin/python3
"""
Module for basic serialization and deserialization of Python dictionaries
to/from JSON files.
"""

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
