import os
import mysql.connector
from flasgger import Swagger
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
from flask_restx import Api

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        create_database()
        db.create_all()

    app.config["SWAGGER"] = {"title": "Restaurant Delivery API", "uiversion": 3}
    Swagger(app)

    register_routes(app)

    @app.route('/')
    def home():
        return jsonify("Application is running"), 200

    return app


def create_database():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "dbuser"),
        password=os.getenv("DB_PASS", ""),
        database="mysql",
    )
    cur = conn.cursor()
    cur.execute(
        f"CREATE DATABASE IF NOT EXISTS `{os.getenv('DB_NAME', 'restaurant_delivery')}` "
        "DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
    )
    cur.close()
    conn.close()
