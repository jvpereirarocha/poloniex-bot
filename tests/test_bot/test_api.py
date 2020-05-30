from api import Api
import unittest


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = Api('BTC_BTS', 60)

    def test_instance(self):
        self.assertIsInstance(self.api, Api)

    def test_get_status_code(self):
        self.assertEqual(self.api.get_status_code(), 200)

    def test_response(self):
        self.assertIsNotNone(self.api.response())

    def test_currencies(self):
        data = self.api._connection.json().keys()
        self.assertEqual(self.api.currencies(), data)

    def test_raise_currencies(self):
        data = self.api._connection.json()
        self.assertRaises(TypeError, self.api.currencies(),
                          type(data) != dict(), data.keys())
