import json


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data


def set_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

