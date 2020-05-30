from database import candles, engine


class Database:
    def __init__(self):
        pass

    def _connect(self, object):
        try:
            connection = engine.connect()
            connection.execute(object)
        except Exception:
            raise Exception('Could not possible to connect')

    def create(self, **kwargs):
        try:
            new_candle = candles.insert().values(
                currency=kwargs.get('currency'),
                period=kwargs.get('period'),
                date=kwargs.get('date'),
                open=kwargs.get('open'),
                close=kwargs.get('close'),
                high=kwargs.get('high'),
                low=kwargs.get('low'),
            )
            self._connect(new_candle)

        except Exception:
            raise Exception('Could not possible insert in the database')
