import os
from pprint import pprint

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


if __name__ == "__main__":
    # pprint(open_csv_file(path_csv))
    pprint(open_csv_file(path_xlsx))
