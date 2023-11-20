import json
from typing import Any


def get_operations_json(path_name: str) -> Any:
    """
    Преобразовывает файл json и возвращает список словарей, содержащий данные об операциях
    :return: list[dict]
    """
    try:
        with open(path_name, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File {path_name} not found.")
        data = []
    except json.decoder.JSONDecodeError:
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
        s = transaction["operationAmount"]["amount"]
        return s
    else:
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
