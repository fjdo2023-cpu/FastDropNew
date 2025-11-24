
from flask import Blueprint
products_bp=Blueprint('products',__name__,url_prefix='/products')

@products_bp.route('/')
def list():
    return "products"
