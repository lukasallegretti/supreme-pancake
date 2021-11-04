import pytest


@pytest.fixture()
def mock_data():
    return {
            'person_id': [1,2,3],
            'datetime': ['10/1/15 8:02', '11/3/15 12:34', '12/2/15 10:27'],
            'floor_level': [6, 5, 1],
            'building': ['B', 'C', 'C']
        }
