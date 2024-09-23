from masks import get_mask_account, get_mask_card_number
from datetime import datetime

def mask_account_card(type_and_number_or_account: str) -> str:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах."""
    if type_and_number_or_account[0:4] == "Счет":
        return "Счет " + get_mask_account(type_and_number_or_account[5:])
    else:
        return type_and_number_or_account[0:-17] + " " + get_mask_card_number(type_and_number_or_account[-16:])


def get_date(str_date: str) -> str:
    return datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
