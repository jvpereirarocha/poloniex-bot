from config import get_db_config
import datetime


class Database:
    def __init__(self):
        self._connection = get_db_config()
        self._cursor = self._connection.cursor()

    def insert(self, **kwargs):
        sql = "INSERT INTO `candles` (currency, period, date_initial,"
        sql += " open_candle, close_candle, high, low)"
        sql += " VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self._cursor.execute(sql, [
            kwargs.get('currency'), kwargs.get('period'),
            datetime.datetime.now(), kwargs.get('open_candle'),
            kwargs.get('close_candle'),
            kwargs.get('high'), kwargs.get('low')
        ])
        self._connection.commit()

    def get(self):
        sql = 'SELECT * FROM `candles`'
        self._cursor.execute(sql)
        result = self._cursor.fetchall()
        return result
