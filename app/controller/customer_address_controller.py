from typing import List

from .general_controller import GeneralController
from ..domain.customer_address import CustomerAddress
from ..service import customer_address_service


class CustomerAddressController(GeneralController):
    _service = customer_address_service

    def find_all_addresses_with_customers(self) -> List[object]:
        return self.find_all(CustomerAddress.customer)

    def find_address_with_customer(self, address_id: int) -> object:
        # Retrieve a single address with related customer eagerly loaded
        return self.find_by_id(address_id, CustomerAddress.customer)
