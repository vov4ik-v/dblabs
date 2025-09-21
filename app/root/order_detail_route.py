# app/route/order_detail_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.order_detail_controller import OrderDetailController
from ..domain.order_detail import OrderDetail

order_detail_bp = Blueprint('order_detail', __name__, url_prefix='/order_details')
order_detail_controller = OrderDetailController()


@order_detail_bp.route('', methods=['GET'])
def get_all_order_details() -> Response:
    """
    List all order details (with relations)
    ---
    tags:
      - OrderDetail
    responses:
      200:
        description: List of order details with relations
        schema:
          type: array
          items:
            type: object
    """
    order_details = order_detail_controller.find_all_order_details_with_relations()
    return make_response(jsonify(order_details), HTTPStatus.OK)


@order_detail_bp.route('/<int:order_detail_id>', methods=['GET'])
def get_order_detail(order_detail_id: int) -> Response:
    """
    Get order detail by ID (with relations)
    ---
    tags:
      - OrderDetail
    parameters:
      - in: path
        name: order_detail_id
        required: true
        type: integer
    responses:
      200:
        description: OK
        schema:
          type: object
      404:
        description: Not found
    """
    order_detail = order_detail_controller.find_order_detail_with_relations(order_detail_id)
    return make_response(jsonify(order_detail), HTTPStatus.OK)


@order_detail_bp.route('', methods=['POST'])
def create_order_detail() -> Response:
    """
    Create a new order detail
    ---
    tags:
      - OrderDetail
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/OrderDetailCreate'
    responses:
      201:
        description: Created
        schema:
          $ref: '#/definitions/OrderDetail'
    """
    content = request.get_json() or {}
    order_detail = OrderDetail.create_from_dto(content)
    order_detail_controller.create(order_detail)
    return make_response(jsonify(order_detail.put_into_dto()), HTTPStatus.CREATED)


@order_detail_bp.route('/<int:order_detail_id>', methods=['PUT'])
def update_order_detail(order_detail_id: int) -> Response:
    """
    Replace order detail by ID
    ---
    tags:
      - OrderDetail
    parameters:
      - in: path
        name: order_detail_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/OrderDetailUpdate'
    responses:
      200:
        description: Updated
        schema:
          $ref: '#/definitions/OrderDetail'
      404:
        description: Not found
    """
    content = request.get_json() or {}
    order_detail = OrderDetail.create_from_dto(content)
    order_detail_controller.update(order_detail_id, order_detail)
    updated = order_detail_controller.find_order_detail_with_relations(order_detail_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@order_detail_bp.route('/<int:order_detail_id>', methods=['PATCH'])
def patch_order_detail(order_detail_id: int) -> Response:
    """
    Partially update order detail by ID
    ---
    tags:
      - OrderDetail
    parameters:
      - in: path
        name: order_detail_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/OrderDetailUpdate'
    responses:
      200:
        description: Updated
        schema:
          type: object
      404:
        description: Not found
    """
    content = request.get_json() or {}
    order_detail_controller.patch(order_detail_id, content)
    updated = order_detail_controller.find_order_detail_with_relations(order_detail_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@order_detail_bp.route('/<int:order_detail_id>', methods=['DELETE'])
def delete_order_detail(order_detail_id: int) -> Response:
    """
    Delete order detail by ID
    ---
    tags:
      - OrderDetail
    parameters:
      - in: path
        name: order_detail_id
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
    order_detail_controller.delete(order_detail_id)
    return make_response(jsonify({"message": "OrderDetail deleted"}), HTTPStatus.OK)
