from utils import reading_json_file
from utils_csv_xlsx import reading_csv_file, reading_xlsx_file
from processing import filter_by_state, sort_by_date
from search import rub_operations, search_operations

def main():
    global lst
    print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')

    file_answer = input()

    if file_answer == '1':
        print('Для обработки выбран JSON-файл.')
        lst: list = reading_json_file('data/operations.json')
    elif file_answer == '2':
        print('Для обработки выбран CSV-файл.')
        lst: list = reading_csv_file('data/transactions.csv')
    elif file_answer == '3':
        print('Для обработки выбран XLSX-файл.')
        lst: list = reading_xlsx_file('data/transactions_excel.xlsx')

    print('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

    status_answer = input()

    while status_answer.upper() not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f'Статус операции "{file_answer.upper()}" недоступен.')
        print('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

    if status_answer.upper() == 'EXECUTED':
        lst: list = filter_by_state(lst, 'EXECUTED')
        print('Операции отфильтрованы по статусу "EXECUTED".')
    elif status_answer.upper() == 'CANCELED':
        lst: list = filter_by_state(lst, 'CANCELED')
        print('Операции отфильтрованы по статусу "CANCELED".')
    elif status_answer.upper() == 'PENDING':
        lst: list = filter_by_state(lst, 'PENDING')
        print('Операции отфильтрованы по статусу "PENDING".')

    print('Отсортировать операции по дате? Да/Нет')
    ascending_answer = input()
    if ascending_answer.upper() == 'ДА':
        lst: list = sort_by_date(lst, False)

    print('Выводить только рублевые тразакции? Да/Нет')
    rub_or_not_answer = input()
    if rub_or_not_answer.upper() == 'ДА':
        lst: list = rub_operations(lst)

    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    search_answer = input()
    if search_answer.upper() == 'ДА':
        print('По какому слову отфильтровать?')
        word_answer  = input()
        lst: list = search_operations(lst, word_answer)

    print('Распечатываю итоговый список транзакций...')
    print(lst)


main()