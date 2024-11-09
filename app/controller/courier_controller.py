from http import HTTPStatus
from typing import List, Tuple, Any

from flask import jsonify

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

    def delete_courier(self, courier_id: int) -> tuple[Any, HTTPStatus]:
        result = self._service.delete_courier(courier_id)
        if "error" in result:
            return result, HTTPStatus.BAD_REQUEST  # Повертаємо статус-код 400 для помилки
        return result, HTTPStatus.OK

    def create_courier(self, courier_data: dict):
        response = self._service.create_courier(courier_data)
        if "error" in response:
            return jsonify(response), HTTPStatus.BAD_REQUEST
        return jsonify(response), HTTPStatus.CREATED

    def update_courier(self, courier_id: int, courier_data: dict):
        response = self._service.update_courier(courier_id, courier_data)
        if "error" in response:
            return jsonify(response), HTTPStatus.BAD_REQUEST
        return jsonify(response), HTTPStatus.OK

    def patch_courier(self, courier_id: int, updates: dict):
        response = self._service.patch_courier(courier_id, updates)
        if "error" in response:
            return jsonify(response), HTTPStatus.BAD_REQUEST
        return jsonify(response), HTTPStatus.OK
