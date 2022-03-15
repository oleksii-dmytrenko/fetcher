import csv
import io
import json

from requests import get


class DataException(Exception):
    pass


FILE_URL = (
    "https://drive.google.com/uc?export=download&id=1zLdEcpzCp357s3Rse112Lch9EMUWzMLE"
)


def fetch_csv(url):
    response = get(url)
    if response.status_code != 200:
        raise DataException("Could not fetch the data")
    return response.text


def parse_csv(csv_data, fields=None):
    reader = csv.DictReader(io.StringIO(csv_data))
    data = [pick_keys(fields, row) for row in reader]
    return json.dumps(data)


def pick_keys(keys, dic):
    return {k: v for k, v in dic.items() if keys is None or k in keys}
