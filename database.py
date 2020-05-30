from sqlalchemy import (
    create_engine, Table, Column, MetaData, Integer, String, DateTime
)

engine = create_engine("mysql+pymysql://jv:sci@2017@localhost/api_poloniex",
                       echo=False)
meta = MetaData()

candles = Table(
    'candles', meta,
    Column('id', Integer, primary_key=True),
    Column('currency', String(50), nullable=False),
    Column('period', Integer, nullable=False),
    Column('date', DateTime(timezone=True), nullable=False),
    Column('open', String(30), nullable=False),
    Column('close', String(30), nullable=False),
    Column('high', String(30), nullable=False),
    Column('low', String(30), nullable=False)
)

if __name__ == '__main__':
    meta.create_all(engine)
