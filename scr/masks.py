def get_mask_card(list_of_data: str) -> str:
    """
    Получаем номер карты и выводим в нужном формате
    """
    number_card = list_of_data.split()[-1]
    card_name = " ".join(list_of_data.split()[0:-1])
    return f"{card_name} {number_card[:4]} {number_card[5:7]}** **** {number_card[-4:]}"


def get_mask_score(number_score: str) -> str:
    """
    Получаем номер карты и выводим в нужном формате
    """
    return f"Счет **{number_score[-4:]}"
