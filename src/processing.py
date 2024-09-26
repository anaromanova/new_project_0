def filter_by_state(list_of_dicts: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция, которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    new_list_of_dicts = []
    for i in list_of_dicts:
        if i['state'] == state:
            new_list_of_dicts.append(i)
    return new_list_of_dicts


def sort_by_date(list_of_dicts: list[dict], ascending: bool = True) -> list[dict]:
    """Функция, которая возвращает новый список, отсортированный по дате."""
    return sorted(list_of_dicts, key=lambda x: x['date'], reverse=ascending)
