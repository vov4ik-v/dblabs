import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")

import mysql.connector
from flasgger import Swagger
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from app.api.spec import SWAGGER_TEMPLATE
from app.config import Config
from app.root import register_routes

db = SQLAlchemy()


def register_models():
    from app.domain.addon import Addon
    from app.domain.cancelled_order import CancelledOrder
    from app.domain.courier import Courier
    from app.domain.customer import Customer
    from app.domain.customer_address import CustomerAddress
    from app.domain.delivery import Delivery
    from app.domain.ingredient import Ingredient
    from app.domain.order import Order
    from app.domain.order_detail import OrderDetail
    from app.domain.product import Product


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Swagger(app, template=SWAGGER_TEMPLATE)

    db.init_app(app)

    with app.app_context():
        create_database()
        register_models()
        db.create_all()

    register_routes(app)

    @app.route('/')
    def home():
        return jsonify("Application is running"), 200

    return app


def create_database():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASS", ""),
        database="mysql",
    )
    cur = conn.cursor()
    cur.close()
    conn.close()
