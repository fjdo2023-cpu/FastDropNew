
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from utils.db import db
from models.product import Product
from utils.s3 import upload_file_s3

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route("/")
@login_required
def list_products():
    produtos = Product.query.order_by(Product.id.desc()).all()
    return render_template("products/list.html", produtos=produtos)

@products_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_product():
    if request.method == "POST":
        nome = request.form.get("nome")
        sku = request.form.get("sku")
        preco = request.form.get("preco") or 0
        descricao = request.form.get("descricao")
        image = request.files.get("image")
        extra_files = request.files.getlist("extra_images")

        image_url = None
        if image and image.filename:
            image_url = upload_file_s3(image)

        extra_urls = []
        for f in extra_files:
            if f and f.filename:
                extra_urls.append(upload_file_s3(f))

        produto = Product(
            nome=nome,
            sku=sku,
            preco=preco,
            descricao=descricao,
            image_url=image_url,
            extra_images=",".join(extra_urls) if extra_urls else None,
        )
        db.session.add(produto)
        db.session.commit()

        return redirect(url_for("products.list_products"))

    return render_template("products/new.html")

@products_bp.route("/edit/<int:product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    produto = Product.query.get_or_404(product_id)

    if request.method == "POST":
        produto.nome = request.form.get("nome")
        produto.sku = request.form.get("sku")
        produto.preco = request.form.get("preco") or 0
        produto.descricao = request.form.get("descricao")

        image = request.files.get("image")
        if image and image.filename:
            produto.image_url = upload_file_s3(image)

        extra_files = request.files.getlist("extra_images")
        existing = produto.extra_images_urls
        new_urls = []
        for f in extra_files:
            if f and f.filename:
                new_urls.append(upload_file_s3(f))
        all_urls = existing + new_urls
        produto.extra_images = ",".join(all_urls) if all_urls else None

        db.session.commit()
        return redirect(url_for("products.list_products"))

    return render_template("products/edit.html", produto=produto)
