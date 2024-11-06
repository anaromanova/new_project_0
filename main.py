from src.utils import reading_json_file
from src.utils_csv_xlsx import reading_csv_file, reading_xlsx_file
from src.processing import filter_by_state, sort_by_date
from src.search import rub_operations_from_json, search_operations, rub_operations_from_xlsx_csv
from src.widget import get_date, mask_account_card


def file_type_option() -> (list, str):
    """Функция, которая выдает список транзакций по выбранному файлу."""
    lst = []
    print('''Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
    file_answer = input('Пользователь: ')
    if file_answer == '1':
        print('Программа: Для обработки выбран JSON-файл.')
        lst= reading_json_file('data/operations.json')
    elif file_answer == '2':
        print('Программа: Для обработки выбран CSV-файл.')
        lst= reading_csv_file('data/transactions.csv')
    elif file_answer == '3':
        print('Программа: Для обработки выбран XLSX-файл.')
        lst = reading_xlsx_file('data/transactions_excel.xlsx')
    return lst, file_answer


def status_type_option(lst: list) -> list:
    """Функция, которая выдает список транзакций по выбранному статусу."""
    status_list = ["EXECUTED", "CANCELED", "PENDING"]
    print('''Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    status_answer = input('Пользователь: ')
    while status_answer.upper() not in status_list:
        print(f'Программа: Статус операции "{status_answer.upper()}" недоступен.')
        print('''Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    lst = filter_by_state(lst, status_answer)
    print(f'Программа: Операции отфильтрованы по статусу "{status_answer}".')
    return lst


def sort_by_date_option(lst: list) -> list:
    """Функция, которая выдает отсортированный или не отсортированный список транзакций."""
    print('Программа: Отсортировать операции по дате? Да/Нет')
    sorting_answer = input('Пользователь: ')
    if sorting_answer.upper() == 'ДА':
        print('Отсортировать по возрастанию? Да/Нет')
        ascending_answer = input('Пользователь: ')
        if ascending_answer.upper() == 'ДА':
            ascending = False
        else:
            ascending = True
        lst = sort_by_date(lst, ascending)
        return lst


def filter_rub_option(lst: list, file_answer: str) -> list:
    """Функция, которая выдает список транзакций только в рублях или нет."""
    print('Программа: Выводить только рублевые тразакции? Да/Нет')
    rub_or_not_answer = input('Пользователь: ')
    if rub_or_not_answer.upper() == 'ДА':
        if file_answer == '1':
            lst = rub_operations_from_json(lst)
        else:
            lst = rub_operations_from_xlsx_csv(lst)
    return lst


def filter_word_option(lst: list) -> list:
    """Функция, которая выдает список транзакций с фильтрацией по слову или словам."""
    print('Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    search_answer = input('Пользователь: ')
    if search_answer.upper() == 'ДА':
        print('Программа: По какому слову отфильтровать?')
        word_answer  = input('Пользователь: ')
        lst = search_operations(lst, word_answer)
    return lst


def printing_results(lst: list) -> None:
    """Функция, которая выдает список транзакций со всеми условиями."""
    print('Программа: Распечатываю итоговый список транзакций...')
    if len(lst) == 0:
        print('Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        print(f'Программа: Всего банковских операций в выборке: {len(lst)}')
        for i in lst:
            print(f'{get_date(i['date'])} {i['description']}')
            if i['description'] == 'Открытие вклада':
                print(mask_account_card(i['to']))
            else:
                print(f'{mask_account_card(i['from'])} -> {mask_account_card(i['to'])}')
            try:
                print(f'Сумма: {i['amount']} {i['currency_code']}')
            except KeyError:
                print(f'Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['code']}')
            print('')


def main() -> None:
    """Функция, которая отвечает за основную логику проекта
        и связывает функциональности между собой."""
    lst, file_answer = file_type_option()
    lst = status_type_option(lst)
    lst = sort_by_date_option(lst)
    lst = filter_rub_option(lst, file_answer)
    lst = filter_word_option(lst)
    printing_results(lst)
