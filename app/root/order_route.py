from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.order_controller import OrderController
from ..domain.order import Order

order_bp = Blueprint('order', __name__, url_prefix='/orders')
order_controller = OrderController()

@order_bp.route('', methods=['GET'])
def get_all_orders() -> Response:
    orders = order_controller.find_all_orders_with_relations()
    return make_response(jsonify(orders), HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id: int) -> Response:
    order = order_controller.find_order_with_relations(order_id)
    if order:
        return make_response(jsonify(order), HTTPStatus.OK)
    return make_response("Order not found", HTTPStatus.NOT_FOUND)

@order_bp.route('', methods=['POST'])
def create_order() -> Response:
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)

@order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id: int) -> Response:
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.update(order_id, order)
    return make_response("Order updated", HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=['PATCH'])
def patch_order(order_id: int) -> Response:
    content = request.get_json()
    order_controller.patch(order_id, content)
    return make_response("Order updated", HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id: int) -> Response:
    order_controller.delete(order_id)
    return make_response("Order deleted", HTTPStatus.OK)
