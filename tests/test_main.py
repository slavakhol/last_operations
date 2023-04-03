from utils.functions import convert_to_datetime, sort_data, get_date, get_from, get_to, get_amount, get_description, publish_operations
import datetime

def test_convert_to_datetime():
    assert convert_to_datetime([{"date": "2019-06-30T15:11:53.136004"}]) == [{'date': datetime.datetime(2019, 6, 30, 15, 11, 53, 136004)}]
    assert convert_to_datetime([{}]) == [{'date': datetime.datetime(1900, 1, 1, 0, 0, 0)}]

def test_sort_data():
    assert sort_data([{'date': datetime.datetime(2019, 6, 30, 15, 11, 53, 136004)},{'date': datetime.datetime(2020, 6, 30, 15, 11, 53, 136004)}]) == [{'date': datetime.datetime(2020, 6, 30, 15, 11, 53, 136004)}, {'date': datetime.datetime(2019, 6, 30, 15, 11, 53, 136004)}]
    assert sort_data([{'date': datetime.datetime(2021, 6, 30, 15, 11, 53, 136004)},{'date': datetime.datetime(2020, 6, 30, 15, 11, 53, 136004)}]) == [{'date': datetime.datetime(2021, 6, 30, 15, 11, 53, 136004)}, {'date': datetime.datetime(2020, 6, 30, 15, 11, 53, 136004)}]

def test_get_date():
    assert get_date([{'date': datetime.datetime(2019, 6, 30, 15, 11, 53, 136004)}], 0) == '30.06.2019'
    assert get_date([{}], 0) == '<Нет данных о дате и времени операции>'

def test_get_description():
    assert get_description([{'description':'Test'}],0) == 'Test'
    assert get_description([{}], 0) == '<Нет описания операции>'

def test_get_from():
    assert get_from([{'from':'Счет 11111111114444'}],0) == 'Счет **4444'
    assert get_from([{'from': 'Visa 11111111114444'}], 0) == 'Visa 11 11** **** 4444'
    assert get_from([{}], 0) == '<Нет данных об отправителе>'

def test_get_to():
    assert get_to([{'to':'Счет 11111111114444'}],0) == 'Счет **4444'
    assert get_to([{'to': 'Visa 11111111114444'}], 0) == 'Visa 11 11** **** 4444'
    assert get_to([{}], 0) == '<Нет данных о получателе>'

def test_get_amount():
    assert get_amount([{"operationAmount": {"amount": "31957.58","currency": {"name": "руб."}}}],0) == '31957.58 руб.'
