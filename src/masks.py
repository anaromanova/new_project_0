import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_of_card: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску."""
    if len(number_of_card) != 16 or not number_of_card.isdigit() or not isinstance(number_of_card, str):
        logger.warning('Возможна проблема с number_of_card')
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
        logger.info('Успешное возвращение маски номера карты')
        return " ".join(lst_of_groups)


def get_mask_account(number_of_account: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску."""
    if len(number_of_account) != 20 or not number_of_account.isdigit() or not isinstance(number_of_account, str):
        logger.warning('Возможна проблема с number_of_account')
        return ""
    else:
        logger.info('Успешное возвращение маски номера счета')
        return "**" + number_of_account[-4:]
