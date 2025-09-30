#!/usr/bin/python3
"""
Module to convert data from a CSV file into a JSON file.
"""

import csv
import json 

def convert_csv_to_json(csv_filename):
    data = []
    try:
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except Exception:
        return False

    try:
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except Exception:
        return False
