import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("x, expected", [("7000792289606361", "7000 79** **** 6361"),
                                         ("70007922", ""),
                                         ("700079228960636123125361", ""),
                                         ("700079228960@*6fwesf", ""),
                                         ("", "")
                                         ])
def test_get_mask_card_number(x: str, expected: str, numbers: str, empty_lsts: str, lsts: str) -> None:
    """Функция тестирует get_mask_account from src.masks"""
    assert get_mask_card_number(x) == expected

    assert get_mask_card_number(empty_lsts) == ""

    assert get_mask_card_number(lsts) == ""

    with pytest.raises(TypeError):
        get_mask_card_number(numbers)


@pytest.mark.parametrize("x, expected", [("73654108430135874305", "**4305"),
                                         ("736541084301358743051234125", ""),
                                         ("736", ""),
                                         ("700079228960@*6fwesf", ""),
                                         ("", "")
                                         ])
def test_get_mask_account(x: str, expected: str, numbers: str, empty_lsts: str, lsts: str) -> None:
    """Функция тестирует get_mask_account from src.masks"""
    assert get_mask_account(x) == expected

    assert get_mask_account(empty_lsts) == ""

    assert get_mask_account(lsts) == ""

    with pytest.raises(TypeError):
        get_mask_card_number(numbers)
