#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dict to JSON and save to filename (overwrite if exists)."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON from filename and return as a Python dict."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
