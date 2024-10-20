def get_mask_card_number(number_of_card: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску."""
    if len(number_of_card) != 16 or not number_of_card.isdigit() or not isinstance(number_of_card, str):
        return ""
    else:
        index_of_first_number = 0
        lst_of_groups = []

        for i in range(4, len(number_of_card) + 1, 4):
            lst_of_groups.append(number_of_card[index_of_first_number:i])
            index_of_first_number += 4

        for i in range(len(lst_of_groups) + 1):
            if i == 1:
                lst_of_groups[i] = "".join(lst_of_groups[i][0:2]) + "**"
            elif i == 2:
                lst_of_groups[i] = "****"
        return " ".join(lst_of_groups)


def get_mask_account(number_of_account: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""
    if len(number_of_account) != 20 or not number_of_account.isdigit() or not isinstance(number_of_account, str):
        return ""
    else:
        return "**" + number_of_account[-4:]
