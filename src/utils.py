import json
import logging
import os

import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def reading_json_file(path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info('Попытка открыть JSON-файл')
        with open(path, encoding='utf-8') as f:
            lst = json.load(f)
        if not isinstance(lst, list) or not lst:
            logger.warning('Проблема с содержимым JSON-файла')
            return []
        else:
            return lst
    except FileNotFoundError:
        logger.warning('Возможна проблема с путем до JSON-файла')
        return []


def external_api(amount: float, from_currency: str) -> dict:
    """Функция для получения текущего курса валют и конвертации суммы операции в рубли"""
    load_dotenv()
    apikey = os.getenv('API_KEY')
    headers = {
        "apikey": f"{apikey}"
    }
    to_currency = 'RUB'
    try:
        logger.info('Попытка подключения через API')
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
        response = requests.get(url, headers=headers)
        result = response.json()
        logger.info('Успешное подключение через API')
        return result
    except requests.exceptions.RequestException:
        logger.warning('Возможна проблема с подключением через API')


def amount_in_rub(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']
    logger.info('Попытка возвращения суммы транзакции в рублях')
    if currency == 'RUB':
        return amount
    else:
        return external_api(amount, from_currency=currency)['result']
