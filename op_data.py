import json, csv


def get_data(filename, type='json'):
    with open(filename, 'r', encoding='utf-8') as file:
        if type == 'json':
            data = json.loads(file.read())
        else:
            data = list(map(list, csv.reader(file)))
    return data


def set_data(data, filename, type='json'):
    with open(filename, 'w', encoding='utf-8') as file:
        if type == 'json':
            file.write(json.dumps(data, indent=4, ensure_ascii=False))
        else:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)

