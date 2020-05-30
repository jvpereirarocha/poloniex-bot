from utils import (
    datetime_to_string, string_to_datetime, datetime_to_timestamp,
    timestamp_to_datetime
)
import datetime
import unittest


class UtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.format = '%d/%m/%Y %H:%M:%S.%f'
        self.now = datetime.datetime.now()
        self.string_now = self.now.strftime(self.format)
        self.timestamp = self.now.timestamp()

    def test_datetime_to_string(self):
        self.assertEqual(self.string_now, datetime_to_string(self.now))

    def test_raise_datetime_to_string(self):
        self.assertRaises(TypeError, datetime_to_string(self.now),
                          type(self.now) != datetime.datetime,
                          self.string_now)

    def test_string_to_datetime(self):
        self.assertEqual(self.now, string_to_datetime(self.string_now))

    def test_raise_string_to_datetime(self):
        self.assertRaises(TypeError, string_to_datetime(self.string_now),
                          type(self.string_now) != str(),
                          datetime.datetime.strptime(self.string_now,
                                                     self.format))

    def test_datetime_to_timestamp(self):
        self.assertEqual(self.timestamp, datetime_to_timestamp(self.now))

    def test_raise_datetime_to_timestamp(self):
        self.assertRaises(TypeError, datetime_to_timestamp(self.now),
                          type(self.now) != datetime.datetime, self.timestamp)

    def test_timestamp_to_datetime(self):
        self.assertEqual(self.now, timestamp_to_datetime(self.timestamp))

    def test_raise_timestamp_to_datetime(self):
        self.assertRaises(TypeError, timestamp_to_datetime(self.timestamp),
                          type(self.timestamp) != float(), self.now)
