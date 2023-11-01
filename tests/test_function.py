import pytest

from scr.masks import get_mask_card, get_mask_score
from scr.processing import get_list_data_dict, get_list_dict
from scr.widget import checking_number, get_datatime


def test_get_mask_score():
    assert get_mask_score("Счет 73654108430135817305") == "Счет **7305"


def test_checking_number():
    assert checking_number("Visa 7000792289606361") == "Visa 7000 92** **** 6361"
    assert checking_number("Счет 73654108430135817305") == "Счет **7305"
    assert checking_number("Счет 73654108430135817") == "Введены неверные данные"


def test_get_mask_card():
    assert (
        get_mask_card("Master Card 7000792289606361")
        == "M a s t e r   C a r d   7 0 0 0 7 9 2 2 8 9 6 0 6 3 6 1 ** **** 1"
    )


def test_get_datatime():
    assert get_datatime("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.fixture
def new_list_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_get_list_dict(new_list_dict):
    assert get_list_dict(new_list_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert get_list_dict(new_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_get_list_data_dict(new_list_dict):
    assert get_list_data_dict(new_list_dict, True) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert get_list_data_dict(new_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
