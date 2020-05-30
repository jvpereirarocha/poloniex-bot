import argparse
import time
from datetime import datetime
from poloniex import Poloniex
from sql import Database
from web import create_app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--currency', required=True)
    parser.add_argument('-p', '--period', type=int, required=True,
                        choices=[60, 300, 600])

    args = parser.parse_args()
    poloniex = Poloniex(args.currency, args.period)

    count = 0

    while(True):
        date = datetime.now()
        open = poloniex.get_field('last')
        close = poloniex.get_field('last')
        high = poloniex.get_field('high24hr')
        low = poloniex.get_field('low24hr')

        db = Database()
        db.create(currency=args.currency, period=args.period,
                  date=date, open=open, close=close, high=high,
                  low=low)
        count = count + 1
        print('Salvo com sucesso! Data/Hora: {}'
              .format(date.strftime('%d/%m/%Y %H:%M:%S')))
        print('Nº de candles salvos: ', count)

        time.sleep(args.period)


if __name__ == '__main__':
    main()
