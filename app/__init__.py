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
        populate_data()

    # Реєструємо маршрути
    register_routes(app)

    # Додаємо простий тестовий маршрут для перевірки роботи додатку
    @app.route('/')
    def home():
        return jsonify({"status": "Application is running"}), 200

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


def populate_data():
    # Перевірка наявності SQL-файлу та виконання запитів у контексті SQLAlchemy
    if os.path.exists('data.sql'):
        with db.engine.connect() as connection:
            with open('data.sql', 'r') as sql_file:
                sql_text = sql_file.read()
                sql_statements = sql_text.split(';')
                for statement in sql_statements:
                    statement = statement.strip()
                    if statement:
                        try:
                            connection.execute(statement)
                        except Exception as error:
                            print(f"Error executing SQL statement: {error}")
