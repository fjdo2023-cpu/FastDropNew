
from flask import Flask, redirect, url_for
from config import Config
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.products import products_bp
from routes.sales import sales_bp
from routes.stock import stock_bp
from utils.db import db
from flask_login import LoginManager
from models.user import User
from werkzeug.security import generate_password_hash
import os

login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init DB
    db.init_app(app)

    # Login manager
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(sales_bp)
    app.register_blueprint(stock_bp)

    # Home -> login
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    # Cria tabelas e admin inicial (se variáveis de ambiente estiverem definidas)
    with app.app_context():
        db.create_all()
        admin_email = app.config.get("ADMIN_EMAIL")
        admin_password = app.config.get("ADMIN_PASSWORD")
        if admin_email and admin_password:
            if not User.query.filter_by(email=admin_email).first():
                admin = User(
                    email=admin_email,
                    password_hash=generate_password_hash(admin_password),
                    is_admin=True,
                )
                db.session.add(admin)
                db.session.commit()

    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
