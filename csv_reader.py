import csv
from typing import List, Dict


def read_csv_to_list_if_dict(file_name: str) -> List[Dict]:
    list_of_rows: list = []
    with open(file_name) as file:
        list_of_rows = [
            {
                key.replace("\ufeff", "").lower(): value for key, value in row.items()
            }
            for row in csv.DictReader(file, skipinitialspace=True)
        ]
    return list_of_rows
