from flask import Flask, redirect, url_for
from config import Config
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.products import products_bp
from routes.sales import sales_bp
from routes.stock import stock_bp
import os

app = Flask(__name__)
app.config.from_object(Config)

# Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(products_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(stock_bp)

# 🔹 ROTA INICIAL -> REDIRECIONA PARA /login
@app.route("/")
def index():
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
