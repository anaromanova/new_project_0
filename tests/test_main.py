from unittest.mock import patch

from main import  file_type_option, sort_by_date_option, status_type_option, filter_rub_option, filter_word_option


@patch("main.reading_csv_file")
@patch("main.input")
def test_file_type_option(mocked_input, mock_reading_csv_file, lst_for_tests_csv_xlsx: list) -> None:
    mocked_input.return_value = '2'
    mock_reading_csv_file.return_value = lst_for_tests_csv_xlsx
    assert file_type_option() == (lst_for_tests_csv_xlsx, '2')


@patch("main.input")
def test_status_type_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "EXECUTED"
    assert status_type_option(lst_for_tests_csv_xlsx) == lst_for_tests_csv_xlsx


@patch("main.input")
def test_sort_by_date_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "да"
    assert sort_by_date_option(lst_for_tests_csv_xlsx) == lst_for_tests_csv_xlsx


@patch("main.input")
def test_filter_rub_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "да"
    assert filter_rub_option(lst_for_tests_csv_xlsx, '2') == [
        { "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "amount": "79114.93",
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
            "description": "Перевод со счета на счет"
        }
            ]


@patch("main.input")
def test_filter_word_option(mock_input, lst_for_tests_csv_xlsx: list) -> None:
    mock_input.return_value = "со счета на счет"
    assert filter_word_option(lst_for_tests_csv_xlsx) == lst_for_tests_csv_xlsx
