import json
from datetime import datetime

NUMBER_OF_LAST_OPERATIONS = 5  #set the number of last operations to display

def main():
    with open("operations.json") as file:
        data = json.load(file)

    for item in data:
        try:
            item['date'] = datetime.strptime(item['date'], "%Y-%m-%dT%H:%M:%S.%f")
        except KeyError:
            item['date'] = datetime(1900, 1, 1, 0, 0, 0)

    sorted_data = sorted(data, reverse=True, key=lambda x: x['date'])

    n = 0

    while n < NUMBER_OF_LAST_OPERATIONS:
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
                print(f"{sorted_data[n]['from'][:-12]} {sorted_data[n]['from'][-12:-10]}** **** {sorted_data[n]['from'][-4:]}", end=" -> ")
        except KeyError:
            print("<Нет данных об отправителе>", end=" -> ")

        try:
            if "Счет" in sorted_data[n]['to']:
                print(f"Счет **{sorted_data[n]['to'][-4:]}")
            else:
                print(f"{sorted_data[n]['to'][:-12]} {sorted_data[n]['to'][-12:-10]}** **** {sorted_data[n]['to'][-4:]}")
        except KeyError:
            print("<Нет данных о получателе>")

        try:
            print(sorted_data[n]['operationAmount']['amount'], sorted_data[n]['operationAmount']['currency']['name'], end="\n\n")
        except KeyError:
            print("<Нет данных о сумме операции>", end="\n\n")
        n += 1

if __name__ == '__main__':
    main()