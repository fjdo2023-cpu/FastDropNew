
from flask import Blueprint, render_template
from flask_login import login_required
from models.sale import Sale
from utils.db import db

sales_bp = Blueprint("sales", __name__, url_prefix="/sales")

@sales_bp.route("/")
@login_required
def list_sales():
    vendas = db.session.query(Sale).all()
    return render_template("sales/list.html", vendas=vendas)
