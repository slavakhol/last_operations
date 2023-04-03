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

"""Function gets date and change date format and returns default error if it is not valid data"""
def get_date(sorted_data, n):
        try:
                return sorted_data[n]['date'].strftime("%d.%m.%Y")
        except KeyError:
                return "<Нет данных о дате и времени операции>"

"""Function gets description and returns default error if it is not valid data"""
def get_description(sorted_data, n):
    try:
        return sorted_data[n]['description']
    except KeyError:
        return "<Нет описания операции>"

"""Function gets from data, check if it is account or card, add asterix and returns default error if it is not valid data"""
def get_from(sorted_data, n):
    try:
        if "Счет" in sorted_data[n]['from']:
            return f"Счет **{sorted_data[n]['from'][-4:]}"
        else:
            return f"{sorted_data[n]['from'][:-12]} {sorted_data[n]['from'][-12:-10]}** **** {sorted_data[n]['from'][-4:]}"
    except KeyError:
        return "<Нет данных об отправителе>"

"""Function gets to data, check if it is account or card, add asterix and returns default error if it is not valid data"""
def get_to(sorted_data, n):
    try:
        if "Счет" in sorted_data[n]['to']:
            return f"Счет **{sorted_data[n]['to'][-4:]}"
        else:
            return f"{sorted_data[n]['to'][:-12]} {sorted_data[n]['to'][-12:-10]}** **** {sorted_data[n]['to'][-4:]}"
    except KeyError:
        return "<Нет данных о получателе>"

"""Function gets amount and currency and returns default error if it is not valid data"""
def get_amount(sorted_data, n):
    try:
        return f"{sorted_data[n]['operationAmount']['amount']} {sorted_data[n]['operationAmount']['currency']['name']}"
    except KeyError:
        return "<Нет данных о сумме операции>"

"""Publish set number of last operations and checking for errors"""
def publish_operations(sorted_data, NUMBER_OF_LAST_OPERATIONS):
    published_operations = 0
    n = 0
    while published_operations < NUMBER_OF_LAST_OPERATIONS:
        if sorted_data[n]['state'] == "EXECUTED":
            published_operations += 1
            print(get_date(sorted_data, n), end=" ")
            print(get_description(sorted_data, n))
            print(get_from(sorted_data, n), end=" -> ")
            print(get_to(sorted_data, n))
            print(get_amount(sorted_data,n), end="\n\n")
        n += 1