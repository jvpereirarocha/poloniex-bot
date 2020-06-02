from sqlalchemy import (
    create_engine, Table, Column, MetaData, Integer, String, DateTime
)

host = 'db'
user = 'jv'
password = 'sci@2017'
db = 'api_poloniex'

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}",
                       echo=True)
meta = MetaData()

candles = Table(
    'candles', meta,
    Column('id', Integer, primary_key=True),
    Column('currency', String(50), nullable=False),
    Column('period', Integer, nullable=False),
    Column('date_initial', DateTime(timezone=True), nullable=False),
    Column('open_candle', String(30), nullable=False),
    Column('close_candle', String(30), nullable=False),
    Column('high', String(30), nullable=False),
    Column('low', String(30), nullable=False)
)

if __name__ == '__main__':
    meta.create_all(engine)
