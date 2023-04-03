import json
from datetime import datetime

"""Function open json file and returns its content"""
def open_json(file):
    with open(file) as json_file:
        return json.load(json_file)

"""Function convert string format into datetime format for futher manipulation. In case of wrong original format function set default_value"""
def convert_to_datetime(data):
    for item in data:
        try:
            item['date'] = datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S.%f")
        except KeyError:
            item['date'] = datetime(1900, 1, 1, 0, 0, 0)
    return data

"""Function sort operations by date by descending"""
def sort_data(data):
    return sorted(data, reverse=True, key=lambda x: x['date'])


"""Publish set number of last operations and checking for errors"""
def publish_operations(sorted_data, NUMBER_OF_LAST_OPERATIONS):
    published_operations = 0
    n = 0
    while published_operations < NUMBER_OF_LAST_OPERATIONS:
        if sorted_data[n]['state'] == "EXECUTED":
            published_operations += 1
            try:
                print(sorted_data[n]['date'].strftime("%d.%m.%Y"), end=" ")
            except KeyError:
                print("<Нет данных о дате и времени операции>", end=" ")

            try:
                print(sorted_data[n]['description'])
            except KeyError:
                print("<Нет описания операции>")

            try:
                if "Счет" in sorted_data[n]['from']:
                    print(f"Счет **{sorted_data[n]['from'][-4:]}", end=" -> ")
                else:
                    print(
                        f"{sorted_data[n]['from'][:-12]} {sorted_data[n]['from'][-12:-10]}** **** {sorted_data[n]['from'][-4:]}",
                        end=" -> ")
            except KeyError:
                print("<Нет данных об отправителе>", end=" -> ")

            try:
                if "Счет" in sorted_data[n]['to']:
                    print(f"Счет **{sorted_data[n]['to'][-4:]}")
                else:
                    print(
                        f"{sorted_data[n]['to'][:-12]} {sorted_data[n]['to'][-12:-10]}** **** {sorted_data[n]['to'][-4:]}")
            except KeyError:
                print("<Нет данных о получателе>")

            try:
                print(sorted_data[n]['operationAmount']['amount'],
                      sorted_data[n]['operationAmount']['currency']['name'], end="\n\n")
            except KeyError:
                print("<Нет данных о сумме операции>", end="\n\n")
        n += 1