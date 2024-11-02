from typing import List

from .general_controller import GeneralController
from ..domain.customer import Customer
from ..service import customer_service


class CustomerController(GeneralController):
    _service = customer_service

    def find_all_customers_with_addresses(self) -> List[object]:
        return self.find_all(Customer.addresses)

    def find_customer_with_addresses(self, customer_id: int) -> object:
        return self.find_by_id_with_relations(customer_id, Customer.addresses)
