import logging
from typing import Any


def get_mask_card(list_of_data: str) -> str:
    """
    Получаем номер карты и выводим в нужном формате
    """
    number_card = list_of_data.split()[-1]
    card_name = " ".join(list_of_data.split()[0:-1])
    log_masks("Номер карты обработан", "INFO")
    return f"{card_name} {number_card[:4]} {number_card[5:7]}** **** {number_card[-4:]}"


def get_mask_score(number_score: str) -> str:
    """
    Получаем номер карты и выводим в нужном формате
    """
    log_masks("Номер счета обработан", "INFO")
    return f"Счет **{number_score[-4:]}"


def log_masks(log_message: str, log_level: str) -> Any:
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("masks.log", "w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    if log_level == "DEBUG":
        logger.setLevel(logging.DEBUG)
        return logger.debug(log_message)
    elif log_level == "INFO":
        logger.setLevel(logging.INFO)
        return logger.info(log_message)
    elif log_level == "WARNING":
        logger.setLevel(logging.WARNING)
        return logger.warning(log_message)
    elif log_level == "ERROR":
        logger.setLevel(logging.ERROR)
        return logger.error(log_message)
    elif log_level == "CRITICAL":
        logger.setLevel(logging.CRITICAL)
        return logger.critical(log_message)
