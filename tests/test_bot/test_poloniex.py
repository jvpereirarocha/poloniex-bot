import unittest
from poloniex import Poloniex


class PoloniexTestCase(unittest.TestCase):
    def setUp(self):
        self.poloniex = Poloniex('BTC_BTS', 60)

    def test_valids_currencies(self):
        self.assertTrue(self.poloniex.valids_currencies())

    def test_invalid_currency(self):
        self.instance = Poloniex('TC_DASH', 800)
        self.assertNotIn(self.instance.currency_pair,
                         self.instance._list_currencies())

    def test_get_response(self):
        self.assertIsNotNone(self.poloniex.get_response())

    def test_list_currencies(self):
        self.assertIsNotNone(self.poloniex._list_currencies())

    def test_get_chart_data(self):
        self.assertIsNotNone(self.poloniex.get_chart_data())
