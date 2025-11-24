
from flask import Blueprint, render_template
from models.sale import Sale
from models.product import Product
from utils.db import db

sales_bp = Blueprint("sales", __name__, url_prefix="/sales")

@sales_bp.route("/")
def list_sales():
    vendas = db.session.query(Sale).all()
    # em templates, usamos v.produto se fizer join depois; por enquanto simples
    return render_template("sales/list.html", vendas=vendas)
