from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.cancelled_order_controller import CancelledOrderController
from ..domain.cancelled_order import CancelledOrder

cancelled_order_bp = Blueprint('cancelled_order', __name__, url_prefix='/cancelled_orders')
cancelled_order_controller = CancelledOrderController()

@cancelled_order_bp.route('', methods=['GET'])
def get_all_cancelled_orders() -> Response:
    # Використовуємо метод, який отримує всі скасовані замовлення з інформацією про замовлення
    cancelled_orders = cancelled_order_controller.find_all_cancelled_orders_with_order()
    return make_response(jsonify(cancelled_orders), HTTPStatus.OK)

@cancelled_order_bp.route('/<int:cancelled_order_id>', methods=['GET'])
def get_cancelled_order(cancelled_order_id: int) -> Response:
    cancelled_order = cancelled_order_controller.find_cancelled_order_with_order(cancelled_order_id)
    return make_response(jsonify(cancelled_order), HTTPStatus.OK)

@cancelled_order_bp.route('', methods=['POST'])
def create_cancelled_order() -> Response:
    content = request.get_json()
    cancelled_order = CancelledOrder.create_from_dto(content)
    cancelled_order_controller.create(cancelled_order)
    return make_response(jsonify(cancelled_order.put_into_dto()), HTTPStatus.CREATED)

@cancelled_order_bp.route('/<int:cancelled_order_id>', methods=['PUT'])
def update_cancelled_order(cancelled_order_id: int) -> Response:
    content = request.get_json()
    cancelled_order = CancelledOrder.create_from_dto(content)
    cancelled_order_controller.update(cancelled_order_id, cancelled_order)
    return make_response("CancelledOrder updated", HTTPStatus.OK)

@cancelled_order_bp.route('/<int:cancelled_order_id>', methods=['PATCH'])
def patch_cancelled_order(cancelled_order_id: int) -> Response:
    content = request.get_json()
    cancelled_order_controller.patch(cancelled_order_id, content)
    return make_response("CancelledOrder updated", HTTPStatus.OK)

@cancelled_order_bp.route('/<int:cancelled_order_id>', methods=['DELETE'])
def delete_cancelled_order(cancelled_order_id: int) -> Response:
    cancelled_order_controller.delete(cancelled_order_id)
    return make_response("CancelledOrder deleted", HTTPStatus.OK)
