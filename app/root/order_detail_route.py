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
    tags: [order_detail]
    responses:
      200:
        description: List of order details with relations
        content:
          application/json:
            schema: {type: array, items: {type: object}}
    """
    order_details = order_detail_controller.find_all_order_details_with_relations()
    return make_response(jsonify(order_details), HTTPStatus.OK)


@order_detail_bp.route('/<int:order_detail_id>', methods=['GET'])
def get_order_detail(order_detail_id: int) -> Response:
    """
    Get order detail by ID (with relations)
    ---
    tags: [order_detail]
    parameters:
      - in: path
        name: order_detail_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: OK}
      404: {description: Not found}
    """
    order_detail = order_detail_controller.find_order_detail_with_relations(order_detail_id)
    return make_response(jsonify(order_detail), HTTPStatus.OK)


@order_detail_bp.route('', methods=['POST'])
def create_order_detail() -> Response:
    """
    Create a new order detail
    ---
    tags: [order_detail]
    requestBody:
      required: true
      content:
        application/json:
          schema: {type: object}
    responses:
      201: {description: Created}
    """
    content = request.get_json()
    order_detail = OrderDetail.create_from_dto(content)
    order_detail_controller.create(order_detail)
    return make_response(jsonify(order_detail.put_into_dto()), HTTPStatus.CREATED)


@order_detail_bp.route('/<int:order_detail_id>', methods=['PUT'])
def update_order_detail(order_detail_id: int) -> Response:
    """
    Replace order detail by ID
    ---
    tags: [order_detail]
    parameters:
      - in: path
        name: order_detail_id
        required: true
        schema: {type: integer}
    requestBody:
      required: true
      content:
        application/json:
          schema: {type: object}
    responses:
      200: {description: Updated}
      404: {description: Not found}
    """
    content = request.get_json()
    order_detail = OrderDetail.create_from_dto(content)
    order_detail_controller.update(order_detail_id, order_detail)
    return make_response("OrderDetail updated", HTTPStatus.OK)


@order_detail_bp.route('/<int:order_detail_id>', methods=['PATCH'])
def patch_order_detail(order_detail_id: int) -> Response:
    """
    Partially update order detail by ID
    ---
    tags: [order_detail]
    parameters:
      - in: path
        name: order_detail_id
        required: true
        schema: {type: integer}
    requestBody:
      required: true
      content:
        application/json:
          schema: {type: object}
    responses:
      200: {description: Updated}
      404: {description: Not found}
    """
    content = request.get_json()
    order_detail_controller.patch(order_detail_id, content)
    return make_response("OrderDetail updated", HTTPStatus.OK)


@order_detail_bp.route('/<int:order_detail_id>', methods=['DELETE'])
def delete_order_detail(order_detail_id: int) -> Response:
    """
    Delete order detail by ID
    ---
    tags: [order_detail]
    parameters:
      - in: path
        name: order_detail_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    order_detail_controller.delete(order_detail_id)
    return make_response("OrderDetail deleted", HTTPStatus.OK)

