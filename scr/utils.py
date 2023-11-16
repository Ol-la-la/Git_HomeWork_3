import json
import os


def get_operations_json(path_name: str) -> dict:
    """
    Преобразовывает файл json и возвращает список словарей, содержащий данные об операциях
    :return: list[dict]
    """
    try:
        with open(path_name, encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"File {path_name} not found.")
        return {}


def transaction_currency(transaction: dict) -> float:
    """
    Возвращает сумму транзакции или ошибку, если транзакция выполнена не в рублях
    :param transaction: dict
    :return: float
    """
    for item in transaction:
        if item["operationAmount"]["currency"]["code"] == "RUB":
            return float(item["operationAmount"]["amount"])
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")


if __name__ == '__main__':
    path_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_ = os.path.join(path_dir, 'data', 'operations.json')
    transactions = get_operations_json(path_)
    print(transaction_currency(transactions))
