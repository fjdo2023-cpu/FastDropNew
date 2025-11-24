
from flask import Blueprint, render_template
from flask_login import login_required
from models.product import Product

stock_bp = Blueprint("stock", __name__, url_prefix="/stock")

@stock_bp.route("/")
@login_required
def list_stock():
    produtos = Product.query.all()
    return render_template("stock/list.html", produtos=produtos)
