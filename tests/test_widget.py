import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card(numbers, empty_lsts, lsts):
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"

    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"

    assert mask_account_card("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"

    assert mask_account_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"

    assert mask_account_card("") == ""

    assert mask_account_card(empty_lsts) == ""

    assert mask_account_card(lsts) == ""

    with pytest.raises(TypeError) as exc_info:
        mask_account_card(numbers)


def test_get_date(numbers, empty_lsts, lsts):
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    assert get_date(empty_lsts) == ""

    assert get_date("") == ""

    assert get_date(lsts) == ""

    with pytest.raises(TypeError) as exc_info:
        get_date(numbers)



