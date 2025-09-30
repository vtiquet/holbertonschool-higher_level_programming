#!/usr/bin/python3
"""
Module for serializing and deserializing a Python dictionary to/from
XML format using xml.etree.ElementTree.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        new_dict = {}

        for child in root:
            new_dict[child.tag] = child.text

        return new_dict
    except Exception:
        return None
