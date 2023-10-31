from scr.masks import get_mask_card, get_mask_score
from scr.widget import checking_number, get_datatime


def test_get_mask_card():
    assert (
        get_mask_card("Master Card 7000792289606361")
        == "M a s t e r   C a r d   7 0 0 0 7 9 2 2 8 9 6 0 6 3 6 1 ** **** 1"
    )


def test_get_mask_score():
    assert get_mask_score("Счет 73654108430135817305") == "Счет **7305"


def test_checking_number():
    assert checking_number("Visa 7000792289606361") == "Visa 7000 92** **** 6361"
    assert checking_number("Счет 73654108430135817305") == "Счет **7305"


def test_get_datatime():
    assert get_datatime("2018-07-11T02:26:18.671407") == "11.07.2018"
