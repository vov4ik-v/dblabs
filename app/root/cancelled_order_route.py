# app/route/cancelled_order_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.cancelled_order_controller import CancelledOrderController
from ..domain.cancelled_order import CancelledOrder

cancelled_order_bp = Blueprint('cancelled_order', __name__, url_prefix='/cancelled_orders')
cancelled_order_controller = CancelledOrderController()


@cancelled_order_bp.route('', methods=['GET'])
def get_all_cancelled_orders() -> Response:
    """
    List all cancelled orders (with order relations)
    ---
    tags:
      - CancelledOrder
    responses:
      200:
        description: List of cancelled orders with related order info
        schema:
          type: array
          items:
            type: object
    """
    cancelled_orders = cancelled_order_controller.find_all_cancelled_orders_with_order()
    return make_response(jsonify(cancelled_orders), HTTPStatus.OK)


@cancelled_order_bp.route('/<int:cancelled_order_id>', methods=['GET'])
def get_cancelled_order(cancelled_order_id: int) -> Response:
    """
    Get cancelled order by ID (with order relation)
    ---
    tags:
      - CancelledOrder
    parameters:
      - in: path
        name: cancelled_order_id
        required: true
        type: integer
    responses:
      200:
        description: Cancelled order found
        schema:
          type: object
      404:
        description: Not found
    """
    cancelled_order = cancelled_order_controller.find_cancelled_order_with_order(cancelled_order_id)
    return make_response(jsonify(cancelled_order), HTTPStatus.OK)


@cancelled_order_bp.route('', methods=['POST'])
def create_cancelled_order() -> Response:
    """
    Create a new cancelled order record
    ---
    tags:
      - CancelledOrder
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/CancelledOrderCreate'
    responses:
      201:
        description: Created cancelled order record
        schema:
          $ref: '#/definitions/CancelledOrder'
    """
    content = request.get_json() or {}
    cancelled_order = CancelledOrder.create_from_dto(content)
    cancelled_order_controller.create(cancelled_order)
    return make_response(jsonify(cancelled_order.put_into_dto()), HTTPStatus.CREATED)


@cancelled_order_bp.route('/<int:cancelled_order_id>', methods=['PUT'])
def update_cancelled_order(cancelled_order_id: int) -> Response:
    """
    Replace cancelled order record by ID
    ---
    tags:
      - CancelledOrder
    parameters:
      - in: path
        name: cancelled_order_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/CancelledOrderUpdate'
    responses:
      200:
        description: Updated
        schema:
          $ref: '#/definitions/CancelledOrder'
      404:
        description: Not found
    """
    content = request.get_json() or {}
    cancelled_order = CancelledOrder.create_from_dto(content)
    cancelled_order_controller.update(cancelled_order_id, cancelled_order)
    updated = cancelled_order_controller.find_cancelled_order_with_order(cancelled_order_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@cancelled_order_bp.route('/<int:cancelled_order_id>', methods=['PATCH'])
def patch_cancelled_order(cancelled_order_id: int) -> Response:
    """
    Partially update cancelled order record by ID
    ---
    tags:
      - CancelledOrder
    parameters:
      - in: path
        name: cancelled_order_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/CancelledOrderUpdate'
    responses:
      200:
        description: Updated
        schema:
          $ref: '#/definitions/CancelledOrder'
      404:
        description: Not found
    """
    content = request.get_json() or {}
    cancelled_order_controller.patch(cancelled_order_id, content)
    updated = cancelled_order_controller.find_cancelled_order_with_order(cancelled_order_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@cancelled_order_bp.route('/<int:cancelled_order_id>', methods=['DELETE'])
def delete_cancelled_order(cancelled_order_id: int) -> Response:
    """
    Delete cancelled order record by ID
    ---
    tags:
      - CancelledOrder
    parameters:
      - in: path
        name: cancelled_order_id
        required: true
        type: integer
    responses:
      200:
        description: Deleted
        schema:
          $ref: '#/definitions/Message'
      404:
        description: Not found
    """
    cancelled_order_controller.delete(cancelled_order_id)
    return make_response(jsonify({"message": "CancelledOrder deleted"}), HTTPStatus.OK)
