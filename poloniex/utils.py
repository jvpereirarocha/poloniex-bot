from api import Api


class Utils:
    def __init__(self):
        self.repr = '<Utils>'
        self.__api = Api()

    def _check_type(self, arg, expected_type):
        return type(arg) == expected_type

    def get_currencies(self):
        if self.__api.get_currencies() is not None:
            currencies = []
            for currency in self.__api.get_currencies():
                currencies.append(currency)
            return currencies
        return None

    def get_field_by_chart_data(self, data, field):
        if data is not None:
            for key, value in data.items():
                if key == field:
                    return value
        return None

    def set_chart_data(self, item, *args):
        data = {}
        for arg in args:
            data[arg] = self.get_field_by_chart_data(item, arg)
        return data

    def __repr__(self):
        return self.repr
