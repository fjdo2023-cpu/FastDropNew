import os
from flask import Flask
from config import Config

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.products import products_bp
from routes.sales import sales_bp
from routes.stock import stock_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(products_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(stock_bp)

if __name__ == "__main__":
    # Render define a variável PORT (ex.: 10000)
    port = int(os.environ.get("PORT", 5000))
    # PRECISA rodar em 0.0.0.0, nunca em 127.0.0.1
    app.run(host="0.0.0.0", port=port)
