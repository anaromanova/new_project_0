import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(numbers, empty_lsts, lsts):
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

    assert get_mask_card_number("70007922") == ""

    assert get_mask_card_number("700079228960636123125361") == ""

    assert get_mask_card_number("700079228960@*6fwesf") == ""

    assert get_mask_card_number("") == ""

    assert get_mask_card_number(empty_lsts) == ""

    assert get_mask_card_number(lsts) == ""

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(numbers)


def test_get_mask_account(numbers, empty_lsts, lsts):
    assert get_mask_account("73654108430135874305") == "**4305"

    assert get_mask_account("736541084301358743051234125") == ""

    assert get_mask_account("736") == ""

    assert get_mask_account("700079228960@*6fwesf") == ""

    assert get_mask_account("") == ""

    assert get_mask_account(empty_lsts) == ""

    assert get_mask_account(lsts) == ""

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(numbers)
