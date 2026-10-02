import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305") 
    ]
)

def test_mask_account_card(info: str, expected: str):
    assert mask_account_card(info) == expected

@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2026-10-02T08:32:35", "02.10.2026")
    ]
)

def test_get_date(date_str: str, expected: str):
    assert get_date(date_str) == expected