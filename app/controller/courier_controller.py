from typing import List

from .general_controller import GeneralController
from ..domain import Courier
from ..service import courier_service


class CourierController(GeneralController):
    _service = courier_service

    def find_all_couriers_with_relations(self) -> List[object]:
        return self.find_all(Courier.regular_customers)

    def find_courier_with_relations(self, courier_id: int) -> object:
        return self.find_by_id_with_relations(courier_id, Courier.regular_customers)

    def add_regular_customer(self, courier_id: int, customer_id: int) -> None:
        self._service.add_regular_customer(courier_id, customer_id)

    def remove_regular_customer(self, courier_id: int, customer_id: int) -> None:
        self._service.remove_regular_customer(courier_id, customer_id)
