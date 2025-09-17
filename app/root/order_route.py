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
    tags: [order]
    responses:
      200:
        description: List of orders with related entities
        content:
          application/json:
            schema:
              type: array
              items: {type: object}
    """
    orders = order_controller.find_all_orders_with_relations()
    return make_response(jsonify(orders), HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id: int) -> Response:
    """
    Get order by ID (with relations)
    ---
    tags: [order]
    parameters:
      - in: path
        name: order_id
        required: true
        schema: {type: integer}
    responses:
      200:
        description: Order found
        content:
          application/json:
            schema: {type: object}
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
    tags: [order]
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Order DTO
            properties:
              customer_id: {type: integer, example: 1}
              items:
                type: array
                items:
                  type: object
                  properties:
                    product_id: {type: integer, example: 101}
                    quantity: {type: integer, example: 2}
              delivery_address_id: {type: integer, example: 5}
              comment: {type: string, example: "Ring the doorbell"}
    responses:
      201:
        description: Created order
        content:
          application/json:
            schema: {type: object}
    """
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)

@order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id: int) -> Response:
    """
    Replace order by ID
    ---
    tags: [order]
    parameters:
      - in: path
        name: order_id
        required: true
        schema: {type: integer}
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Full order payload to replace existing one
    responses:
      200: {description: Updated}
      404: {description: Order not found}
    """
    content = request.get_json()
    order = Order.create_from_dto(content)
    order_controller.update(order_id, order)
    return make_response("Order updated", HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=['PATCH'])
def patch_order(order_id: int) -> Response:
    """
    Partially update order by ID
    ---
    tags: [order]
    parameters:
      - in: path
        name: order_id
        required: true
        schema: {type: integer}
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Partial fields to update
    responses:
      200: {description: Updated}
      404: {description: Order not found}
    """
    content = request.get_json()
    order_controller.patch(order_id, content)
    return make_response("Order updated", HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id: int) -> Response:
    """
    Delete order by ID
    ---
    tags: [order]
    parameters:
      - in: path
        name: order_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: Deleted}
      404: {description: Order not found}
    """
    order_controller.delete(order_id)
    return make_response("Order deleted", HTTPStatus.OK)

