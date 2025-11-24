
from utils.db import db
from datetime import datetime

class StockMovement(db.Model):
    __tablename__ = "stock_movements"

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    tipo = db.Column(db.String(20))  # entrada/saida
    quantidade = db.Column(db.Integer, default=0)
    data = db.Column(db.DateTime, default=datetime.utcnow)
