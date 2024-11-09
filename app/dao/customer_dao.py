from .general_dao import GeneralDAO
from ..domain import Customer


class CustomerDAO(GeneralDAO):
    _domain_type = Customer

    def find_by_id(self, customer_id: int) -> Customer:
        return Customer.query.get(customer_id)
