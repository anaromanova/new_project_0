from unittest.mock import Mock

from main import main


def test_main_file_answer(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    i = input('''Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
                Выберите необходимый пункт меню:
                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла?''')
    assert i == "1"


def test_main_status_answer(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "EXECUTED")
    i = input('''Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    assert i == "EXECUTED"


def test_main_ascending_answer(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Да")
    i = input('''Программа: Отсортировать операции по дате? Да/Нет''')
    assert i == "Да"


def test_main_rub_or_not_answer(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Да")
    i = input('''Программа: Выводить только рублевые тразакции? Да/Нет''')
    assert i == "Да"


def test_main_search_answer(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Да")
    i = input('''Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет''')
    assert i == "Да"


def test_main():

    output = main()
    assert output == []
