import requests
from config import get_url_api


class Api:
    def __init__(self, period=60):
        self._url = get_url_api()
        self.period = int(period)
        self._connection = requests.get(self._url)

    def _get_status_code(self):
        return self._connection.status_code

    def _get_request_text(self):
        return self._connection.text

    def response(self):
        if self._get_status_code() == 200\
                and self._get_request_text is not None:
            return self._connection.json()
        return None

    def get_currencies(self):
        if self.response() is not None:
            return self.response().keys()
        return None

    def get_chart_data(self):
        if self.response() is not None:
            currencies = []
            for currency in self.response().items():
                currency[1]['name'] = currency[0]
                currency[1].pop('lowestAsk', None)
                currency[1].pop('highestBid', None)
                currency[1].pop('percentChange', None)
                currency[1].pop('baseVolume', None)
                currency[1].pop('quoteVolume', None)
                currency[1].pop('isFrozen', None)
                currencies.append(currency[1])
            return currencies
        return None

    def get_chart_by_currency(self, currency_name):
        if self.get_chart_data() is not None:
            for currency in self.get_chart_data():
                if currency['name'] == currency_name:
                    return currency
        return None

    def __repr__(self):
        return "<API: command=returnTicker>"
