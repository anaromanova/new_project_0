import json
import os

import requests
from dotenv import load_dotenv


def reading_json_file(path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as f:
            lst = json.load(f)
        if not isinstance(lst, list) or not lst:
            return []
        else:
            return lst
    except FileNotFoundError:
        return []


def external_api(amount: float, from_currency: str) -> dict:
    """Функция для получения текущего курса валют и конвертации суммы операции в рубли"""
    load_dotenv()
    apikey = os.getenv('API_KEY')
    headers = {
        "apikey": f"{apikey}"
    }
    to_currency = 'RUB'
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    response = requests.get(url, headers=headers)
    result = response.json()
    return result


def amount_in_rub(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']
    if currency == 'RUB':
        return amount
    else:
        return external_api(amount, from_currency=currency)['result']
