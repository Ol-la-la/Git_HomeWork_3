from scr.masks import get_mask_card, get_mask_score


def checking_number(name_number_card: str) -> str:
    """
    Получаем исходные данные с номером карты или счета.
    Преобразовываем их в нужный нам формат.
    """
    list_of_data = name_number_card.split()
    number_card = list_of_data[-1]
    if len(number_card) == 20:
        return get_mask_score(number_card)
    elif len(number_card) == 16:
        return get_mask_card(name_number_card)
    else:
        return "Введены неверные данные"


def get_datatime(data_time: str) -> str:
    """
    Преобразовывает дату в нужный формат
    :param : Дата для изменения
    :return: Отформатированная дата
    """
    return f"{data_time[8:10]}.{data_time[5:7]}.{data_time[:4]}"
