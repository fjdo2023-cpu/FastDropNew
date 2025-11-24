
from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # TODO: implementar autenticação real
        return redirect(url_for("dashboard.home"))
    return render_template("login.html")
