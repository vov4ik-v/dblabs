from sqlalchemy.orm import joinedload

from .general_service import GeneralService
from app.extensions import db
from ..dao import customer_dao, CourierDAO, courier_dao
from ..domain import Customer, Courier


class CustomerService(GeneralService):
    def find_all(self, *relations):
        query = Customer.query
        for relation in relations:
            query = query.options(joinedload(relation))
        return query.all()

    def find_by_id_with_relations(self, customer_id: int, *relations):
        query = Customer.query.filter_by(customer_id=customer_id)
        for relation in relations:
            query = query.options(joinedload(relation))
        return query.first()

    def add_favorite_courier(self, customer_id: int, courier_id: int):
        customer = self._dao.find_by_id(customer_id)
        courier = CourierDAO().find_by_id(courier_id)

        if customer and courier:
            customer.favorite_couriers.append(courier)
            db.session.commit()

    def remove_favorite_courier(self, customer_id: int, courier_id: int) -> None:
        customer = self._dao.find_by_id(customer_id)
        courier = Courier.query.get(courier_id)
        if courier in customer.favorite_couriers:
            customer.favorite_couriers.remove(courier)
            db.session.commit()
