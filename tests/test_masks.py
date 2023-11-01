from scr.masks import get_mask_card, get_mask_score


def test_get_mask_score():
    assert get_mask_score("Счет 73654108430135817305") == "Счет **7305"


def test_get_mask_card():
    assert (get_mask_card("Master Card 7000792289606361")
            == "Master Card 7000 92** **** 6361"
            )
