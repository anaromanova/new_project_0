from unittest.mock import mock_open, patch

from src.utils import amount_in_rub, external_api, reading_json_file


@patch("builtins.open", new_callable=mock_open,
       read_data='''[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                   "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                   "description": "Перевод организации",
                   "from": "Maestro 1596837868705199",
                   "to": "Счет 64686473678894779589"}]''')
def test_valid_reading_json_file(mock_file: str) -> None:
    """Функция тестирует reading_json_file from src.utils на корректный файл с транзакциями"""
    transactions = reading_json_file("data/operations.json")
    assert transactions == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             'description': 'Перевод организации',
                             'from': 'Maestro 1596837868705199',
                             'to': 'Счет 64686473678894779589'}]


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_not_a_list_reading_json_file(mock_file: str) -> None:
    """Функция тестирует reading_json_file from src.utils на некорректные данные (например, не список)"""
    not_a_list_transactions = reading_json_file("data/operations.json")
    assert not_a_list_transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found_reading_json_file(mock_file: str) -> None:
    """Функция тестирует reading_json_file from src.utils на случай, если файл не найден"""
    file_not_found_transactions = reading_json_file("data/operations.json")
    assert file_not_found_transactions == []


@patch('requests.get')
def test_external_api(mock_get: any) -> None:
    """Функция тестирует external_api from src.utils"""
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 456},
                                               'info': {'timestamp': 1729440965, 'rate': 95.802878},
                                               'date': '2024-10-20', 'result': 43686.112368}
    assert (external_api(456, 'USD') == {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 456}, 'info': {'timestamp': 1729440965, 'rate': 95.802878}, 'date': '2024-10-20', 'result': 43686.112368})


def test_amount_in_rub() -> None:
    """Функция тестирует amount_in_rub from src.utils"""
    assert amount_in_rub({"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                          "operationAmount": {"amount": "123", "currency": {"name": "руб.", "code": "RUB"}},
                          "description": "Перевод организации",
                          "from": "Maestro 1596837868705199",
                          "to": "Счет 64686473678894779589"}) == '123'
