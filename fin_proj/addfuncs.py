import json


def load_data(filename):
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

    return data
