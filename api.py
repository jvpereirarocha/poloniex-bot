import requests


class Api:
    def __init__(self, currency_pair, period):
        self.currency_pair = currency_pair
        self.period = period
        self._url = 'https://poloniex.com/public?command='
        self._command = 'returnTicker'
        self._connection = requests.get(self._url + self._command)

    def get_status_code(self):
        return self._connection.status_code

    def response(self):
        if self.get_status_code() == 200:
            return self._connection.json()
        return None

    def currencies(self):
        try:
            data = self._connection.json()
            return data.keys()
        except TypeError:
            raise TypeError('Invalid type to return data')

    def __repr__(self):
        if self.get_status_code() == 200:
            return "<API: returnTicker>"
        else:
            return "<API: unknow command>"
