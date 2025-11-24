
from utils.db import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    produto_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantidade = db.Column(db.Integer, default=1)
    valor = db.Column(db.Numeric(10, 2), default=0)
    lucro = db.Column(db.Numeric(10, 2), default=0)
