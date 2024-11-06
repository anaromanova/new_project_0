from unittest.mock import mock_open, patch

from src.utils_csv_xlsx import reading_csv_file, reading_xlsx_file

# @patch("builtins.open", new_callable=mock_open,
#        read_data='''id;state;date;amount;currency_name;currency_code;from;to;description''')
# def test_valid_reading_csv_file(mock_file: str) -> None:
#     """Функция тестирует reading_csv_file from src.utils_csv_xlsx на корректный файл с транзакциями"""
#     transactions = reading_csv_file("data/operations.csv")
#     assert transactions == ['650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации']


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_not_a_list_reading_csv_file(mock_file: str) -> None:
    """Функция тестирует reading_csv_file from src.utils_csv_xlsx на некорректные данные (например, не список)"""
    not_a_list_transactions = reading_csv_file("data/operations.csv")
    assert not_a_list_transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found_reading_csv_file(mock_file: str) -> None:
    """Функция тестирует reading_csv_file from src.utils_csv_xlsx на случай, если файл не найден"""
    file_not_found_transactions = reading_csv_file("data/operations.csv")
    assert file_not_found_transactions == []


# @patch("builtins.open", new_callable=mock_open,
#        read_data='''[{'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z',
#                       'amount': 23423.0, 'currency_name': 'Peso', 'currency_code': 'PHP',
#                       'from': 'Discover 7269000803370165',
#                       'to': 'American Express 1963030970727681',
#                       'description': 'Перевод с карты на карту'}]''')
# def test_valid_reading_xlsx_file(mock_file: str) -> None:
#     """Функция тестирует reading_xlsx_file from src.utils_csv_xlsx на корректный файл с транзакциями"""
#     transactions = reading_xlsx_file("data/operations_excel.xlsx")
#     assert transactions == [{'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z',
#                               'amount': 23423.0, 'currency_name': 'Peso', 'currency_code': 'PHP',
#                               'from': 'Discover 7269000803370165',
#                               'to': 'American Express 1963030970727681',
#                               'description': 'Перевод с карты на карту'}]


# @patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
# def test_not_a_list_reading_xlsx_file(mock_file: str) -> None:
#     """Функция тестирует reading_xlsx_file from src.utils_csv_xlsx на некорректные данные (например, не список)"""
#     not_a_list_transactions = reading_xlsx_file("data/operations_excel.xlsx")
#     assert not_a_list_transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found_reading_xlsx_file(mock_file: str) -> None:
    """Функция тестирует reading_xlsx_file from src.utils_csv_xlsx на случай, если файл не найден"""
    file_not_found_transactions = reading_xlsx_file("data/operations_excel.xlsx")
    assert file_not_found_transactions == []
