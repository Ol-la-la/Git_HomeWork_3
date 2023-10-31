from scr.processing import get_list_data_dict, get_list_dict
from scr.widget import checking_number, get_datatime


def main():
    """
    Запрашиваем от пользователя исходные данные в формате:
    тип и номер карты: Master Card 7000792289606361
    номер счета: Счет 73654108430135817305
    выводим дату
    """
    name_number_card = input("Введите номер карты или счета\n")
    return print(
        f"{checking_number(name_number_card)}\nДата: {get_datatime('2018-07-11T02:26:18.671407')}"
    )


if __name__ == "__main__":
    user_dicts = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(get_list_dict(user_dicts))
    print(get_list_data_dict(user_dicts))
    main()
