import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def sample_transaction():
    return[
        {
            'description': 'canceled', 'operationAmount': {
                'amount': '1432',
                'currency': {
                    'code': 'JPY'
                }
            }
        },
        {
            'description': 'confirmation', 'operationAmount': {
                'amount': '200',
                'currency': {
                    'code': 'USD'
                }
            }
        }
    ]

@pytest.mark.parametrize(
        "start, stop, expected",
        [
            (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"])
        ],
)

def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected

def test_filter_by_currency(sample_transaction):
    result = list(filter_by_currency(sample_transaction, "USD"))
    assert len(result) == 1

def test_filter_by_currency_not_found(sample_transaction):
    result = list(filter_by_currency(sample_transaction, "TWD"))
    assert len(result) == 0

def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([]))
    assert len(result) == 0

def test_transaction_descriptions(sample_transaction):
    result = list(transaction_descriptions(sample_transaction))
    assert result == ['canceled', 'confirmation']

def test_transaction_descriptions_empty_list():
    result = list(transaction_descriptions([]))
    assert result == []
