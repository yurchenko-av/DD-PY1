import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filepath, delimiter=',', new_line='\n') -> list[dict]:

    dicts_list = []

    with open(filepath) as f:
        headers_str = f.readline().replace(new_line, '')
        headers_list = headers_str.split(delimiter)

        for row in f:
            row = row.replace(new_line, '')
            values_list = row.split(delimiter)
            dicts_list.append(dict(zip(headers_list, values_list)))

    return dicts_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
