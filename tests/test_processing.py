import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [{'state': 'EXECUTED', 'id': 1, 'date': '2019-07-03T18:35:29.512364'}, 
            {'state': 'EXECUTED', 'id': 2, 'date': '2018-06-30T02:08:58.425572'}, 
            {'state': 'CANCELED', 'id': 3, 'date': '2020-09-12T21:27:25.241681'}
            ]

def tests_sort_by_date(sample_data):
    result = sort_by_date(sample_data)
    assert result[0]['date'] == '2020-09-12T21:27:25.241681'
    assert result[-1]['date'] == '2018-06-30T02:08:58.425572'
    
@pytest.mark.parametrize(
        "state_name, expected_count",
        [
            ("EXECUTED", 2),
            ("CANCELED", 1 ),
            ("PENDING", 0),
        ]
)

def test_filter_by_state(sample_data, state_name, expected_count):
    result = filter_by_state(sample_data, state_name)
    assert len(result) == expected_count
