from .general_service import GeneralService
from .. import db
from ..dao import courier_dao, CustomerDAO, customer_dao
from ..domain import Customer


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
