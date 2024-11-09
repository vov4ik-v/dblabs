from sqlalchemy.exc import DatabaseError

from .general_service import GeneralService
from ..dao import courier_dao, CustomerDAO, customer_dao
from ..domain import Customer, Courier
from app.extensions import db


class CourierService(GeneralService):
    _dao = courier_dao

    def add_regular_customer(self, courier_id: int, customer_id: int):
        courier = self._dao.find_by_id(courier_id)
        customer = CustomerDAO().find_by_id(customer_id)

        if courier and customer:
            courier.regular_customers.append(customer)
            db.session.commit()

    def remove_regular_customer(self, courier_id: int, customer_id: int) -> None:
        courier = self._dao.find_by_id(courier_id)
        customer = Customer.query.get(customer_id)
        if customer in courier.regular_customers:
            courier.regular_customers.remove(customer)
            db.session.commit()

    def create_courier(self, courier_data: dict) -> dict:
        try:
            courier = Courier.create_from_dto(courier_data)
            db.session.add(courier)
            db.session.commit()
            return courier.put_into_dto(include_regular_customers=True)
        except DatabaseError as e:
            db.session.rollback()
            error_message = str(e.orig)
            return {"error": error_message}

    def update_courier(self, courier_id: int, courier_data: dict) -> dict:
        try:
            courier = self._dao.find_by_id(courier_id)
            if not courier:
                return {"error": "Courier not found"}

            for key, value in courier_data.items():
                setattr(courier, key, value)

            db.session.commit()
            return courier.put_into_dto(include_regular_customers=True)
        except DatabaseError as e:
            db.session.rollback()
            error_message = str(e.orig)
            return {"error": error_message}

    def patch_courier(self, courier_id: int, updates: dict) -> dict:
        try:
            courier = self._dao.find_by_id(courier_id)
            if not courier:
                return {"error": "Courier not found"}

            for key, value in updates.items():
                setattr(courier, key, value)

            db.session.commit()
            return courier.put_into_dto(include_regular_customers=True)
        except DatabaseError as e:
            db.session.rollback()
            error_message = str(e.orig)
            return {"error": error_message}

    def delete_courier(self, courier_id: int) -> dict:
        try:
            self._dao.delete(courier_id)
            db.session.commit()  # Завершуємо транзакцію після успішного видалення
            return {"message": "Courier deleted successfully"}
        except DatabaseError as e:
            db.session.rollback()  # Очищаємо сесію після помилки
            error_message = str(e.orig)  # Отримуємо текст помилки
            return {"error": error_message}