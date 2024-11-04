
from typing import List
from .general_controller import GeneralController
from ..domain.customer import Customer
from ..service import customer_service

class CustomerController(GeneralController):
    _service = customer_service

    def find_all_customers_with_relations(self) -> List[object]:
        # Завантажуємо адреси та улюблених кур'єрів для кожного клієнта
        return self.find_all(Customer.addresses, Customer.favorite_couriers)

    def find_customer_with_relations(self, customer_id: int) -> object:
        # Завантажуємо адреси та улюблених кур'єрів для конкретного клієнта
        return self.find_by_id_with_relations(customer_id, Customer.addresses, Customer.favorite_couriers)

    def add_favorite_courier(self, customer_id: int, courier_id: int) -> None:
        self._service.add_favorite_courier(customer_id, courier_id)

    def remove_favorite_courier(self, customer_id: int, courier_id: int) -> None:
        self._service.remove_favorite_courier(customer_id, courier_id)
