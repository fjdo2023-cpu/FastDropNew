
from utils.db import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sku = db.Column(db.String(100), unique=True)
    preco = db.Column(db.Numeric(10, 2), default=0)
    estoque = db.Column(db.Integer, default=0)
    custo_medio = db.Column(db.Numeric(10, 2), default=0)
    image_url = db.Column(db.String(500))
