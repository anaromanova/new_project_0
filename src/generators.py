def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """Функция, которая возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
            try:
                yield i
            except StopIteration:
                break


def transaction_descriptions(transactions: list[dict]) -> str:
    """Функция, которая возвращает описание каждой операции по очереди."""
    for i in transactions:
        try:
            yield i["description"]
        except 'StopIteration':
            break


def card_number_generator(start: int, end: int) -> str:
    """Функция, которая возвращает номера банковских карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for i in range(start, end):
        text = ((16 - len(str(i))) * "0" + str(i))
        yield ' '.join(text[b*4:(b+1)*4] for b in range(4))
