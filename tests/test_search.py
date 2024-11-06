from src.search import count_of_descriptions, rub_operations_from_json, rub_operations_from_xlsx_csv, search_operations


def test_search_operations_with_word(lst_for_tests: list) -> None:
    transaction_search = search_operations(lst_for_tests, 'организации')
    assert transaction_search == [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
        ]


def test_search_operations_impossible(lst_for_tests: list) -> None:
    transaction_search = search_operations(lst_for_tests, 'другу')
    assert transaction_search == []


def test_search_operations_empty(lst_for_tests: list) -> None:
    transaction_search = search_operations(lst_for_tests, '')
    assert transaction_search == lst_for_tests


def test_search_operations_empty_lst(empty_lsts: list) -> None:
    transaction_search = search_operations(empty_lsts, 'организации')
    assert transaction_search == []


def test_count_of_descriptions(lst_for_tests: list) -> None:
    transaction_count = count_of_descriptions(lst_for_tests, ['Перевод с карты на карту'])
    assert transaction_count == {'Перевод с карты на карту': 1}


def test_count_of_descriptions_empty(lst_for_tests: list) -> None:
    transaction_count = count_of_descriptions(lst_for_tests, [])
    assert transaction_count == {}


def test_count_of_descriptions_empty_lst(empty_lsts: list) -> None:
    transaction_count = count_of_descriptions(empty_lsts, ['Перевод с карты на карту'])
    assert transaction_count == {}


def test_rub_operations_from_json(lst_for_tests: list) -> None:
    transaction_count = rub_operations_from_json(lst_for_tests)
    assert transaction_count == [{
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }]


def test_rub_operations_from_json_empty_lst(empty_lsts: list) -> None:
    transaction_count = rub_operations_from_json(empty_lsts)
    assert transaction_count == []


def test_rub_operations_from_xlsx_csv(lst_for_tests_csv_xlsx: list) -> None:
    transaction_count = rub_operations_from_xlsx_csv(lst_for_tests_csv_xlsx)
    assert transaction_count == [
                                   {"id": 142264268,
                                    "state": "EXECUTED",
                                    "date": "2019-04-04T23:20:05.206878",
                                    "amount": "79114.93",
                                    "currency_name": "Ruble",
                                    "currency_code": "RUB",
                                    "from": "Счет 19708645243227258542",
                                    "to": "Счет 75651667383060284188",
                                    "description": "Перевод со счета на счет"}
                                ]


def test_rub_operations_from_xlsx_csv_empty_lst(empty_lsts: list) -> None:
    transaction_count = rub_operations_from_xlsx_csv(empty_lsts)
    assert transaction_count == []
