import pytest
from scr.widget import checking_number, get_datatime


def test_get_datatime():
    assert get_datatime("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.mark.parametrize(
    "n, expected_result",
    [
        ("Master Card 7000792289606361", "Master Card 7000 92** **** 6361"),
        ("Счет 73654108430135817305", "Счет **7305"),
        ("Счет 73654108430135817", "Введены неверные данные"),
    ],
)
def test_checking_number(n, expected_result):
    assert checking_number(n) == expected_result
