import json

import pandas as pd

from questao_2.transform import output_json


def test_output(mock_data):
    df = pd.DataFrame(mock_data)
    result = output_json(df)
    print(result)
    assert result == json.dumps({
        "results": [
            {"person_id": "1",
            "datetime": "2015-10-01 08:02:00",
            "floor_level": 6,
            "building": "B"},
            {"person_id": "2",
            "datetime": "2015-11-03 12:34:00",
            "floor_level": 5,
            "building": "C"},
            {"person_id": "3",
            "datetime": "2015-12-02 10:27:00",
            "floor_level": 1,
            "building": "C"}
            ]
        })
