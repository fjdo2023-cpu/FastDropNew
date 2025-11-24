
from flask import Blueprint, render_template
from models.product import Product

stock_bp = Blueprint("stock", __name__, url_prefix="/stock")

@stock_bp.route("/")
def list_stock():
    produtos = Product.query.all()
    return render_template("stock/list.html", produtos=produtos)
