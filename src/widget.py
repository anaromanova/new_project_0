from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number_or_account: str) -> str:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах."""
    if len(type_and_number_or_account) == 0 or not isinstance(type_and_number_or_account, str):
        return ""
    else:
        if type_and_number_or_account[0:4] == "Счет":
            return "Счет " + get_mask_account(type_and_number_or_account[5:])
        else:
            return type_and_number_or_account[0:-17] + " " + get_mask_card_number(type_and_number_or_account[-16:])


def get_date(str_date: str) -> str:
    """Функция, которая  принимает на вход строку с датой в формате
        "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
        "ДД.ММ.ГГГГ"("11.03.2024")."""
    if len(str_date) == 0 or not isinstance(str_date, str):
        return ""
    else:
        return datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")