import json
import logging
import os

import requests
from dotenv import load_dotenv

# Основная конфигурация logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='logs/utils.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске

# Создаем логеры для различных компонентов программы
reading_json_file_logger = logging.getLogger('app.reading_json_file')
external_api_logger = logging.getLogger('app.external_api')
amount_in_rub_logger = logging.getLogger('app.amount_in_rub')


def reading_json_file(path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        reading_json_file_logger.info('Попытка открыть JSON-файл')
        with open(path, encoding='utf-8') as f:
            lst = json.load(f)
        if not isinstance(lst, list) or not lst:
            reading_json_file_logger.warning('Проблема с содержимым JSON-файла')
            return []
        else:
            return lst
    except FileNotFoundError:
        reading_json_file_logger.warning('Возможна проблема с путем до JSON-файла')
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
        external_api_logger.info('Попытка подключения через API')
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
        response = requests.get(url, headers=headers)
        result = response.json()
        external_api_logger.info('Успешное подключение через API')
        return result
    except requests.exceptions.RequestException:
        external_api_logger.warning('Возможна проблема с подключением через API')


def amount_in_rub(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']
    external_api_logger.info('Попытка возвращения суммы транзакции в рублях')
    if currency == 'RUB':
        return amount
    else:
        return external_api(amount, from_currency=currency)['result']
