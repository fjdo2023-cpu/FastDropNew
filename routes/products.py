
from flask import Blueprint, render_template, request, redirect, url_for
from utils.db import db
from models.product import Product
from utils.s3 import upload_file_s3

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route("/")
def list_products():
    produtos = Product.query.order_by(Product.id.desc()).all()
    return render_template("products/list.html", produtos=produtos)

@products_bp.route("/new", methods=["GET", "POST"])
def new_product():
    if request.method == "POST":
        nome = request.form.get("nome")
        sku = request.form.get("sku")
        preco = request.form.get("preco") or 0
        image = request.files.get("image")

        image_url = None
        if image and image.filename:
            image_url = upload_file_s3(image)

        produto = Product(nome=nome, sku=sku, preco=preco, image_url=image_url)
        db.session.add(produto)
        db.session.commit()

        return redirect(url_for("products.list_products"))

    return render_template("products/new.html")
