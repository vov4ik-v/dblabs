import os
import mysql.connector
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes

# Ініціалізація SQLAlchemy тільки один раз у цьому файлі
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ініціалізація SQLAlchemy з додатком
    db.init_app(app)

    # Виконуємо всі операції з базою даних у контексті додатку
    with app.app_context():
        create_database()
        db.create_all()

    # Реєструємо маршрути
    register_routes(app)

    @app.route('/')
    def home():
        return jsonify("Application is running"), 200

    return app


def create_database():
    # Використовуємо mysql.connector для створення бази даних
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='VASILIWIN2020',
        database='mysql'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS restaurant_delivery")
    cursor.close()
    connection.close()
