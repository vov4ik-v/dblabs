import mysql.connector
from .general_dao import GeneralDAO
from ..domain import Order
from app.extensions import db

class OrderDAO(GeneralDAO):
    _domain_type = Order

    def calculate_order_total_price(self, operation: str) -> float:
        conn = db.engine.raw_connection()  # Отримуємо низькорівневе з’єднання
        try:
            cursor = conn.cursor()
            cursor.callproc('calculate_order_total_price', [operation])

            result = None
            for res in cursor.stored_results():
                result = res.fetchone()[0]

            cursor.close()
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()


