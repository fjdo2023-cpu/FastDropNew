
from flask import Blueprint
sales_bp=Blueprint('sales',__name__,url_prefix='/sales')

@sales_bp.route('/')
def sales():
    return "sales"
