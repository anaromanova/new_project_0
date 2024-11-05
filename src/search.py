import re
from collections import Counter


def search_operations(lst_of_dicts: list[dict], search_line: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях
     и строку поиска, а возвращает список словарей, у которых в описании есть данная строка."""
    return [i for i in lst_of_dicts if re.findall(pattern=search_line.lower(), string=i['description'].lower())]


def count_of_descriptions(lst_of_dicts: list[dict], lst_of_descriptions: list) -> dict:
    """Функция, которая принимает список словарей с данными о банковских операциях и
     список категорий операций, а возвращает словарь, в котором ключи — это названия категорий,
      а значения — это количество операций в каждой категории."""
    return Counter([i['description'] for i in lst_of_dicts if i['description'] in lst_of_descriptions])


def rub_operations_from_xlsx_csv(lst_of_dicts: list[dict]):
    """Функция, которая принимает список словарей с данными о банковских операциях
    из xlsx или csv, а возвращает список словарей, у которых только рублевые тразакции."""
    return [i for i in lst_of_dicts if i.get('currency_code') == 'RUB']


def rub_operations_from_json(lst_of_dicts: list[dict]):
    """Функция, которая принимает список словарей с данными о банковских операциях
    из json, а возвращает список словарей, у которых только рублевые тразакции."""
    lst = []
    for i in lst_of_dicts:
        try:
            if i.get('operationAmount').get('currency').get('code') == 'RUB':
                lst.append(i)
        except AttributeError:
            continue
    return lst
