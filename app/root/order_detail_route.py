from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import order_detail_controller
from ..domain.order_detail import OrderDetail

order_detail_bp = Blueprint('order_detail', __name__, url_prefix='/order_details')

@order_detail_bp.route('', methods=['GET'])
def get_all_order_details() -> Response:
    return make_response(jsonify(order_detail_controller.find_all()), HTTPStatus.OK)

@order_detail_bp.route('', methods=['POST'])
def create_order_detail() -> Response:
    content = request.get_json()
    order_detail = OrderDetail.create_from_dto(content)
    order_detail_controller.create(order_detail)
    return make_response(jsonify(order_detail.put_into_dto()), HTTPStatus.CREATED)

@order_detail_bp.route('/<int:order_detail_id>', methods=['GET'])
def get_order_detail(order_detail_id: int) -> Response:
    return make_response(jsonify(order_detail_controller.find_by_id(order_detail_id)), HTTPStatus.OK)

@order_detail_bp.route('/<int:order_detail_id>', methods=['PUT'])
def update_order_detail(order_detail_id: int) -> Response:
    content = request.get_json()
    order_detail = OrderDetail.create_from_dto(content)
    order_detail_controller.update(order_detail_id, order_detail)
    return make_response("OrderDetail updated", HTTPStatus.OK)

@order_detail_bp.route('/<int:order_detail_id>', methods=['PATCH'])
def patch_order_detail(order_detail_id: int) -> Response:
    content = request.get_json()
    order_detail_controller.patch(order_detail_id, content)
    return make_response("OrderDetail updated", HTTPStatus.OK)

@order_detail_bp.route('/<int:order_detail_id>', methods=['DELETE'])
def delete_order_detail(order_detail_id: int) -> Response:
    order_detail_controller.delete(order_detail_id)
    return make_response("OrderDetail deleted", HTTPStatus.OK)
