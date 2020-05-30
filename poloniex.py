from api import Api


class Poloniex:
    def __init__(self, currency_pair, period):
        self.currency_pair = currency_pair
        self.period = period
        self._api = Api(self.currency_pair, self.period)

    def _list_currencies(self):
        return self._api.currencies()

    def valids_currencies(self):
        if self.currency_pair in self._list_currencies():
            return True
        return False

    def get_response(self):
        if self._api.get_status_code() == 200:
            return self._api.response()
        raise ConnectionError('Could not possible return the response')

    def get_chart_data(self):
        try:
            for currency in self.get_response().items():
                if currency[0] == self.currency_pair:
                    currency[1].pop('lowestAsk', None)
                    currency[1].pop('highestBid', None)
                    currency[1].pop('percentChange', None)
                    currency[1].pop('baseVolume', None)
                    currency[1].pop('quoteVolume', None)
                    currency[1].pop('isFrozen', None)
                    return currency[1]
            return None
        except IndexError:
            raise IndexError('List out of range')

    def get_field(self, name):
        items = self.get_chart_data().items()
        if items is not None:
            for key, value in items:
                if key == name:
                    return value
        return None
