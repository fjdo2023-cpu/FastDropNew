
from flask import Blueprint, render_template
from utils.db import db
from models.product import Product
from models.sale import Sale

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
def home():
    total_produtos = db.session.query(Product).count()
    total_estoque = db.session.query(db.func.coalesce(db.func.sum(Product.estoque), 0)).scalar()
    vendas_dia = db.session.query(Sale).count()
    lucro_dia = db.session.query(db.func.coalesce(db.func.sum(Sale.lucro), 0)).scalar()

    return render_template(
        "dashboard.html",
        total_produtos=total_produtos,
        total_estoque=total_estoque,
        vendas_dia=vendas_dia,
        lucro_dia=lucro_dia,
    )
