# app/route/order_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.order_controller import OrderController
from ..domain.order import Order

order_bp = Blueprint('order', __name__, url_prefix='/orders')
order_controller = OrderController()


@order_bp.route('', methods=['GET'])
def get_all_orders() -> Response:
    """
    List all orders (with relations)
    ---
    tags:
      - Order
    responses:
      200:
        description: List of orders with related entities
        schema:
          type: array
          items:
            type: object
    """
    orders = order_controller.find_all_orders_with_relations()
    return make_response(jsonify(orders), HTTPStatus.OK)


@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id: int) -> Response:
    """
    Get order by ID (with relations)
    ---
    tags:
      - Order
    parameters:
      - in: path
        name: order_id
        required: true
        type: integer
    responses:
      200:
        description: Order found
        schema:
          type: object
      404:
        description: Order not found
    """
    order = order_controller.find_order_with_relations(order_id)
    if order:
        return make_response(jsonify(order), HTTPStatus.OK)
    return make_response("Order not found", HTTPStatus.NOT_FOUND)


@order_bp.route('', methods=['POST'])
def create_order() -> Response:
    """
    Create a new order
    ---
    tags:
      - Order
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/OrderCreate'
    responses:
      201:
        description: Created order
        schema:
          $ref: '#/definitions/Order'
    """
    content = request.get_json() or {}
    order = Order.create_from_dto(content)
    order_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)


@order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id: int) -> Response:
    """
    Replace order by ID
    ---
    tags:
      - Order
    parameters:
      - in: path
        name: order_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/OrderUpdate'
    responses:
      200:
        description: Updated
        schema:
          $ref: '#/definitions/Order'
      404:
        description: Order not found
    """
    content = request.get_json() or {}
    order = Order.create_from_dto(content)
    order_controller.update(order_id, order)
    updated = order_controller.find_order_with_relations(order_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@order_bp.route('/<int:order_id>', methods=['PATCH'])
def patch_order(order_id: int) -> Response:
    """
    Partially update order by ID
    ---
    tags:
      - Order
    parameters:
      - in: path
        name: order_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/OrderUpdate'
    responses:
      200:
        description: Updated
        schema:
          type: object
      404:
        description: Order not found
    """
    content = request.get_json() or {}
    order_controller.patch(order_id, content)
    updated = order_controller.find_order_with_relations(order_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id: int) -> Response:
    """
    Delete order by ID
    ---
    tags:
      - Order
    parameters:
      - in: path
        name: order_id
        required: true
        type: integer
    responses:
      200:
        description: Deleted
        schema:
          $ref: '#/definitions/Message'
      404:
        description: Order not found
    """
    order_controller.delete(order_id)
    return make_response(jsonify({"message": "Order deleted"}), HTTPStatus.OK)
