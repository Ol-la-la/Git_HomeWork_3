def get_list_dict(user_dicts: list[dict], state_param: str = "EXECUTED") -> list[dict]:
    """
    Функция, которая принимает на вход список словарей.
    Возвращает новый список, содержащий только те словари,
    у которых ключ state соответствует заданному значению.
    :param user_dicts: Исходный список словарей
    :param state_param: нужное значение ключа state, по умолчанию EXECUTED
    :return: новый список словарей
    """
    new_dict: list[dict] = []
    for user_dict in user_dicts:
        if user_dict["state"] == state_param:
            new_dict.append(user_dict)
    return new_dict


def get_list_data_dict(user_dicts: list[dict], sort_order: bool = False) -> list[dict]:
    """
    Функция, которая принимает на вход список словарей.
    Возвращает новый список, отсортированный по дате
    :param user_dicts: Исходный список словарей
    :param sort_order: способ сортировки даты (по умолчанию - по возрастанию)
    :return: новый список словарей
    """
    if sort_order:
        new_dict = sorted(user_dicts, key=lambda x: x["date"])
    else:
        new_dict = sorted(user_dicts, key=lambda x: x["date"], reverse=True)
    return new_dict
