from typing import List

from .general_controller import GeneralController
from ..domain.customer import Customer
from ..service import customer_service


class CustomerController(GeneralController):
    _service = customer_service

    def find_all_customers_with_addresses(self) -> List[object]:
        # Retrieve all customers with addresses eagerly loaded
        return self.find_all(Customer.addresses)

    def find_customer_with_addresses(self, customer_id: int) -> object:
        # Retrieve a single customer with addresses eagerly loaded
        return self.find_by_id(customer_id, Customer.addresses)
