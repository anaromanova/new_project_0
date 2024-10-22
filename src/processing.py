def filter_by_state(list_of_dicts: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция, которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    if not isinstance(list_of_dicts, list) or len(list_of_dicts) == 0:
        return [{}]
    else:
        new_list_of_dicts = []
        for i in list_of_dicts:
            if i['state'] == state:
                new_list_of_dicts.append(i)
        return new_list_of_dicts


def sort_by_date(list_of_dicts: list[dict], ascending: bool = True) -> list[dict]:
    """Функция, которая возвращает новый список, отсортированный по дате."""
    if not isinstance(list_of_dicts, list) or len(list_of_dicts) == 0:
        return [{}]
    else:
        return sorted(list_of_dicts, key=lambda x: x['date'], reverse=ascending)
