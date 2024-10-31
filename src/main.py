from utils import reading_json_file
from utils_csv_xlsx import reading_csv_file, reading_xlsx_file
from processing import filter_by_state, sort_by_date
from search import rub_operations_from_json, search_operations, rub_operations_from_xlsx_csv
from widget import get_date, mask_account_card


def main():
    """Функция, которая отвечает за основную логику проекта
        и связывает функциональности между собой."""
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

    print('''Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

    status_answer = input('Пользователь: ')

    while status_answer.upper() not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f'Программа: Статус операции "{file_answer.upper()}" недоступен.')
        print('''Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

    if status_answer.upper() == 'EXECUTED':
        lst = filter_by_state(lst, 'EXECUTED')
        print('Программа: Операции отфильтрованы по статусу "EXECUTED".')
    elif status_answer.upper() == 'CANCELED':
        lst = filter_by_state(lst, 'CANCELED')
        print('Программа: Операции отфильтрованы по статусу "CANCELED".')
    elif status_answer.upper() == 'PENDING':
        lst = filter_by_state(lst, 'PENDING')
        print('Программа: Операции отфильтрованы по статусу "PENDING".')

    print('Программа: Отсортировать операции по дате? Да/Нет')
    ascending_answer = input('Пользователь: ')
    if ascending_answer.upper() == 'ДА':
        lst = sort_by_date(lst, False)

    print('Программа: Выводить только рублевые тразакции? Да/Нет')
    rub_or_not_answer = input('Пользователь: ')
    if rub_or_not_answer.upper() == 'ДА':
        if file_answer == '1':
            lst = rub_operations_from_json(lst)
        else:
            lst = rub_operations_from_xlsx_csv(lst)

    print('Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    search_answer = input('Пользователь: ')
    if search_answer.upper() == 'ДА':
        print('Программа: По какому слову отфильтровать?')
        word_answer  = input('Пользователь: ')
        lst = search_operations(lst, word_answer)

    print('Программа: Распечатываю итоговый список транзакций...')
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
