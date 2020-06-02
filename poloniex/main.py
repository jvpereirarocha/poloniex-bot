from database import Database
import argparse
import time
from utils import Utils
from api import Api
import datetime


def main():
    datetime_format = '%d/%m/%Y %H:%M:%S'
    utils = Utils()
    api = Api()
    db = Database()
    currencies = utils.get_currencies()

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--currency', choices=currencies)
    parser.add_argument('-p', '--period', type=int, choices=[60, 300, 600])

    args = parser.parse_args()

    while(True):
        if args.period is not None:
            api.period = args.period

        if args.currency is not None:
            item = api.get_chart_by_currency(args.currency)
            data = utils.set_chart_data(item, 'last', 'high24hr', 'low24hr')
            datetime_save = datetime.datetime.now()
            db.insert(
                currency=args.currency, period=api.period,
                open_candle=data['last'],
                close_candle=data['last'], high=data['high24hr'],
                low=data['low24hr']
            )
            print('{} salvo com sucesso às {}'
                  .format(args.currency, datetime_save
                          .strftime(datetime_format)))
        else:
            if len(currencies) > 0:
                for currency in currencies:
                    item = api.get_chart_by_currency(currency)
                    data = utils.set_chart_data(item, 'last', 'high24hr',
                                                'low24hr')
                    datetime_save = datetime.datetime.now()
                    db.insert(
                        currency=currency, period=api.period,
                        open_candle=data['last'],
                        close_candle=data['last'], high=data['high24hr'],
                        low=data['low24hr']
                    )
                    print('{} salvo com sucesso às {}'
                          .format(args.currency, datetime_save
                                  .strftime(datetime_format)))
            else:
                print('Nada a salvar')

        time.sleep(api.period)


if __name__ == '__main__':
    main()
