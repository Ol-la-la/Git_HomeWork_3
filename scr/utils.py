import json
import logging
from typing import Any


def get_operations_json(path_name: str) -> Any:
    """
    Преобразовывает файл json и возвращает список словарей, содержащий данные об операциях
    :return: list[dict]
    """
    try:
        with open(path_name, encoding="utf-8") as f:
            data = json.load(f)
            log_utils("Файл считывается корректно", "INFO")
    except FileNotFoundError:
        print(f"File {path_name} not found.")
        data = []
        log_utils("Вы пытаетесь обратиться к несуществующему файлу", "ERROR")
    except json.decoder.JSONDecodeError:
        log_utils("Ошибка формата файла", "ERROR")
        print(f"File {path_name} is not json")
        data = []
    return data


def transaction_currency(transaction: dict) -> float | Any:
    """
    Возвращает сумму транзакции или ошибку, если транзакция выполнена не в рублях
    :param transaction: dict
    :return: float
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        log_utils("Функция работает корректно", "INFO")
        s = transaction["operationAmount"]["amount"]
        return s
    else:
        log_utils("Произошла ошибка транзакции. Транзакция выполнена не в рублях", "ERROR")
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")


def log_utils(log_message: str, log_level: str) -> Any:
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("utils.log", "w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.propagate = True
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
