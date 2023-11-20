from unittest.mock import patch

import pytest

from scr.utils import get_operations_json, transaction_currency


@patch("builtins.open", create=True)
def test_get_operations_json(filename):
    """
    Проверяем, что файл json корректный
    :return: пустой список
    """
    mock_file = filename.return_value.__enter__.return_value
    mock_file.read.return_value = "test data"
    assert get_operations_json("test data") == []


def test_get_not_file_json():
    """
    Тестируем исключение, если файл json не найден
    :return: ошибка
    """
    assert get_operations_json("1234") == []


def test_transaction_currency():
    """
    Проверяем, что транзакция выполнена в рублях и обрабатываем ошибку
    """
    assert transaction_currency({"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}) == 100
    with pytest.raises(ValueError):
        transaction_currency({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}})
