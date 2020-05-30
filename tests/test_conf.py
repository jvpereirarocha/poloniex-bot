from tests.test_bot.test_api import ApiTestCase
from tests.test_bot.test_poloniex import PoloniexTestCase
from tests.test_bot.test_utils import UtilsTestCase
import unittest

if __name__ == '__main__':
    ApiTestCase()
    PoloniexTestCase()
    UtilsTestCase()
    unittest.main()
