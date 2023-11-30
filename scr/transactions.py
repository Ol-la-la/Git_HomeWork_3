import os
import re
from pprint import pprint
from typing import Any

import numpy as np
import pandas as pd

path_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_csv = os.path.join(path_dir, "data", "transactions.csv")
path_xlsx = os.path.join(path_dir, "data", "transactions_excel.xlsx")


def open_csv_file(path_csv_xlsx: str) -> list[dict] | str:
    """
    Считываем файл csv или xlsx и возвращаем список словарей
    :param path_csv_xlsx: путь до файла csv или xlsx
    :return: список словарей или сообщение об ошибке пути.
    """
    path_user = str(path_csv_xlsx)
    if path_user.endswith(".csv"):
        reader = pd.read_csv(path_user, sep=";")

    elif path_user.endswith(".xlsx"):
        reader = pd.read_excel(path_user)
    else:
        return "Указан неверный путь файла"

    reader = pd.DataFrame(reader).replace({np.nan: None})
    result = reader.to_dict(orient="records")
    for i in result:
        i["operationAmount"] = {
            "amount": i["amount"],
            "currency": {"name": i["currency_name"], "code": i["currency_code"]},
        }
        del i["amount"], i["currency_name"], i["currency_code"]
    return result


def get_search_operation(transaction: list[dict], meaning: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях
    и строку поиска. Возвращает список словарей, у которых в описании есть данная строка.

    """
    transaction_list = []
    pattern = re.compile(f"{meaning}", flags=re.IGNORECASE)
    for operation in transaction:
        try:
            if pattern.search(operation["description"]):
                transaction_list.append(operation)
        except KeyError:
            continue
        except TypeError:
            continue
    return transaction_list


def get_filter_dict(transactions: list[dict[Any, Any]], category: dict) -> dict:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и
    словарь категорий операций, и возвращать словарь с названиями категорий и
    количеством операций в каждой категории.
    """
    for operation in transactions:
        try:
            for keys in category:
                if keys.upper() in operation["description"].upper():
                    category[keys] += 1
        except AttributeError:
            continue
    return category


if __name__ == "__main__":
    transaction_open = open_csv_file(path_csv)
    # pprint(get_search_operation(transaction_open, 'Открытие'))
    pprint(get_filter_dict(transaction_open, {"Перевод": 0, "Карты": 0}))
