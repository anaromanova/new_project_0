import json
import requests


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


def external_api(amount: float) -> float:
    payload = {}
    headers = {
        "apikey": "34ef6v1Dqt041HD5X5MipsuKsURS61aK"
    }
    to_currency = 'RUB'
    from_currency = 'USD'
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    response = requests.get(url, headers=headers, data = payload)
    status_code = response.status_code
    result = response.json()
    return result['result']


def amount_in_rub(transaction: dict) -> float:




