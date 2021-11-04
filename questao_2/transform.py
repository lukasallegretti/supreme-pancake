""" Transform a csv into json """
import json
from typing import Dict
from datetime import datetime


import pandas as pd


def output_json(data_frame: pd.DataFrame):
    """ Transform dataframe rows to json output

    Args:
        data_frame (pd.DataFrame): Dataframe to be transform

    Returns:
        Dict: Rows like in json format json
    """
    length = len(data_frame)
    df_values = []

    for row in range(length):
        values = list(data_frame.iloc[row])
        registration = {
            'person_id': str(values[0]),
            'datetime': str(
                datetime.strptime(
                    values[1], "%m/%d/%y %H:%M"
                )
            ),
            'floor_level': int(values[2]),
            'building': values[3]
        }
        df_values.append(registration)

    return json.dumps({'results': df_values})



if __name__ == '__main__':
    df = pd.read_csv('questao_2/questao_02.csv')
    print(output_json(df))
