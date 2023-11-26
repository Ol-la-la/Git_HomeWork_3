from unittest.mock import patch

from scr.transactions import open_csv_file, path_csv, path_xlsx


@patch("builtins.open", create=True)
def test_open_csv_file_not_file(filename):
    """
    Проверяем путь, если некорректный.
    :return: Сообщение об ошибке пути.
    """
    mock_file = filename.return_value.__enter__.return_value
    mock_file.read.return_value = "test"
    assert open_csv_file("test") == "Указан неверный путь файла"


def test_open_csv_file():
    with patch('scr.transactions.open_csv_file') as mock_get:
        mock_get.path_csv.return_value = 650703.0
        assert open_csv_file(path_csv)[0]['id'] == 650703.0


def test_open_xlsx_file():
    with patch('scr.transactions.open_csv_file') as mock_get:
        mock_get.path_xlsx.return_value = 650703.0
        assert open_csv_file(path_xlsx)[0]['id'] == 650703.0
