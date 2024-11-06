from unittest.mock import patch

from main import (file_type_option, filter_rub_option, filter_word_option, printing_results, sort_by_date_option,
                  status_type_option)


@patch("main.reading_csv_file")
@patch("main.input")
def test_file_type_option_csv(mocked_input, mock_reading_csv_file, lst_for_tests_csv_xlsx: list) -> None:
    mocked_input.return_value = '2'
    mock_reading_csv_file.return_value = lst_for_tests_csv_xlsx
    assert file_type_option() == (lst_for_tests_csv_xlsx, '2')


@patch("main.reading_xlsx_file")
@patch("main.input")
def test_file_type_option_xlsx(mocked_input, mock_reading_xlsx_file, lst_for_tests_csv_xlsx: list) -> None:
    mocked_input.return_value = '3'
    mock_reading_xlsx_file.return_value = lst_for_tests_csv_xlsx
    assert file_type_option() == (lst_for_tests_csv_xlsx, '3')


@patch("main.reading_json_file")
@patch("main.input")
def test_file_type_option_json(mocked_input, mock_reading_json_file, lst_for_tests: list) -> None:
    mocked_input.return_value = '1'
    mock_reading_json_file.return_value = lst_for_tests
    assert file_type_option() == (lst_for_tests, '1')


@patch("main.input")
def test_status_type_option_executed(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "EXECUTED"
    assert status_type_option(lst_for_tests_csv_xlsx) == lst_for_tests_csv_xlsx


@patch("main.input")
def test_status_type_option_pending(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "PENDING"
    assert status_type_option(lst_for_tests_csv_xlsx) == []


@patch("main.input")
def test_status_type_option_canceled(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "CANCELED"
    assert status_type_option(lst_for_tests_csv_xlsx) == []


@patch("main.input")
def test_sort_by_date_option_descending(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.side_effect = ["да", "нет"]
    assert sort_by_date_option(lst_for_tests_csv_xlsx) == [
        {"id": 142264268,
         "state": "EXECUTED",
         "date": "2019-04-04T23:20:05.206878",
         "amount": "79114.93",
         "currency_name": "Ruble",
         "currency_code": "RUB",
         "from": "Счет 19708645243227258542",
         "to": "Счет 75651667383060284188",
         "description": "Перевод со счета на счет"
         },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "description": "Перевод организации"
        }
            ]


@patch("main.input")
def test_sort_by_date_option_ascending(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.side_effect = ["да", "да"]
    assert sort_by_date_option(lst_for_tests_csv_xlsx) == lst_for_tests_csv_xlsx


@patch("main.input")
def test_filter_rub_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "да"
    assert filter_rub_option(lst_for_tests_csv_xlsx, '2') == [
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


@patch("main.input")
def test_filter_not_only_rub_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "нет"
    assert filter_rub_option(lst_for_tests_csv_xlsx, '2') == lst_for_tests_csv_xlsx


@patch("main.input")
def test_filter_word_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.side_effect = ["да", "со счета на счет"]
    assert filter_word_option(lst_for_tests_csv_xlsx) == [
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


@patch("main.input")
def test_filter_another_word_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.side_effect = ["да", "Перевод организации"]
    assert filter_word_option(lst_for_tests_csv_xlsx) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "description": "Перевод организации"
        }
            ]


@patch("main.input")
def test_filter_no_word_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "нет"
    assert filter_word_option(lst_for_tests_csv_xlsx) == lst_for_tests_csv_xlsx


def test_printing_results(lst_for_tests_csv_xlsx: list) -> None:
    assert printing_results(lst_for_tests_csv_xlsx) is None
