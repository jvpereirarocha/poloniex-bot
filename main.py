import argparse
import time
from datetime import datetime
from currencies import currencies
from poloniex import Poloniex


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--currency', required=True, choices=currencies)
    parser.add_argument('-p', '--period', type=int, required=True,
                        choices=[20, 300, 600])

    args = parser.parse_args()
    poloniex = Poloniex(args.currency, args.period)

    count = 0
    initial_date_time = ''
    final_date_time = ''
    while(count <= args.period):
        if count == 0:
            initial_date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        elif count == args.period:
            break
        count += 1
        print('Remaining time: ', args.period-count)
        time.sleep(1)
    print("initial: ", initial_date_time)
    print("final: ", final_date_time)


if __name__ == '__main__':
    main()
