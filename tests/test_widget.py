import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("x, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                         ("Счет 73654108430135874305", "Счет **4305"),
                                         ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                         ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                         ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                         ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                         ("", "")
                                         ])
def test_mask_account_card(x: str, expected: str, numbers: str, empty_lsts: str, lsts: str) -> None:
    assert mask_account_card(x) == expected

    assert mask_account_card(empty_lsts) == ""

    assert mask_account_card(lsts) == ""

    with pytest.raises(TypeError):
        mask_account_card(numbers)


@pytest.mark.parametrize("x, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                         ("", ""),
                                         ])
def test_get_date(x: str, expected: str, numbers: str, empty_lsts: str, lsts: str) -> None:
    assert get_date(x) == expected

    assert get_date(empty_lsts) == ""

    assert get_date(lsts) == ""

    with pytest.raises(TypeError):
        get_date(numbers)
