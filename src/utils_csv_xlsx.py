import csv

import pandas as pd


def reading_csv_file(path: str) -> list:
    """Функция, которая принимает на вход путь до CSV-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        lst = []
        fieldnames = ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description']
        with open(path, encoding="utf-8-sig") as file:
            reader = csv.DictReader(file, delimiter=';', fieldnames=fieldnames)
            next(reader)
            for row in reader:
                lst.append(row)
        if not isinstance(lst, list) or not lst:
            return []
        else:
            return lst
    except FileNotFoundError:
        return []


def reading_xlsx_file(path: str) -> list:
    """Функция, которая принимает на вход путь до XLSX-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        lst = []
        fieldnames = ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description']
        df = pd.read_excel(path, decimal=';', names=fieldnames)
        lst = df.to_dict('records')
        if not isinstance(lst, list) or not lst:
            return []
        else:
            return lst
    except FileNotFoundError:
        return []
