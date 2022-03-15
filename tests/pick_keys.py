import unittest

from fetcher.helpers import pick_keys


class TestPickKeys(unittest.TestCase):
    def test_pick_keys(self):
        dic = pick_keys(["a", "b"], dict(a=1, b=2, c=3))
        self.assertEqual(dic, dict(a=1, b=2))

    def test_pick_keys_default(self):
        dic = pick_keys(None, dict(a=1, b=2, c=3))
        self.assertEqual(dic, dict(a=1, b=2, c=3))
