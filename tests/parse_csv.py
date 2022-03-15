import json
from unittest import TestCase

from fetcher.helpers import parse_csv


class TestParser(TestCase):
    def test_parses_csv(self):
        csv = "a,b,c\n1,2,3"
        json_data = parse_csv(csv)
        data = json.loads(json_data)
        self.assertEqual(data[0]["a"], "1")
        self.assertEqual(data[0]["b"], "2")
        self.assertEqual(data[0]["c"], "3")

    def test_parses_csv_only_certain_fields(self):
        csv = "a,b,c\n1,2,3"
        json_data = parse_csv(csv, ["b", "c"])
        data = json.loads(json_data)
        self.assertEqual(data[0]["b"], "2")
        with self.assertRaises(KeyError):
            data[0]["a"]
            data[0]["c"]
