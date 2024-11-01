from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.delivery_controller import DeliveryController
from ..domain.delivery import Delivery

delivery_bp = Blueprint('delivery', __name__, url_prefix='/deliveries')
delivery_controller = DeliveryController()

@delivery_bp.route('', methods=['GET'])
def get_all_deliveries() -> Response:
    # Використовуємо метод для отримання доставок з обмеженою інформацією про замовлення
    deliveries = delivery_controller.find_all_deliveries_with_relations()
    return make_response(jsonify(deliveries), HTTPStatus.OK)

@delivery_bp.route('/<int:delivery_id>', methods=['GET'])
def get_delivery(delivery_id: int) -> Response:
    # Використовуємо метод для отримання доставки з обмеженою інформацією про замовлення
    delivery = delivery_controller.find_delivery_with_relations(delivery_id)
    return make_response(jsonify(delivery), HTTPStatus.OK)

@delivery_bp.route('', methods=['POST'])
def create_delivery() -> Response:
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.create(delivery)
    return make_response(jsonify(delivery.put_into_dto()), HTTPStatus.CREATED)

@delivery_bp.route('/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id: int) -> Response:
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.update(delivery_id, delivery)
    return make_response("Delivery updated", HTTPStatus.OK)

@delivery_bp.route('/<int:delivery_id>', methods=['PATCH'])
def patch_delivery(delivery_id: int) -> Response:
    content = request.get_json()
    delivery_controller.patch(delivery_id, content)
    return make_response("Delivery updated", HTTPStatus.OK)

@delivery_bp.route('/<int:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id: int) -> Response:
    delivery_controller.delete(delivery_id)
    return make_response("Delivery deleted", HTTPStatus.OK)
