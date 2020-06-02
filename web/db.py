from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Candles(db.Model):
    __tablename__ = 'candles'
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(50), nullable=False)
    period = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False)
    open = db.Column(db.String(30), nullable=False)
    close = db.Column(db.String(30), nullable=False)
    high = db.Column(db.String(30), nullable=False)
    low = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<Candles: {}>".format(self.currency)
