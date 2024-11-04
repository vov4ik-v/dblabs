from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import courier_controller
from ..domain.courier import Courier

courier_bp = Blueprint('courier', __name__, url_prefix='/couriers')

@courier_bp.route('', methods=['GET'])
def get_all_couriers() -> Response:
    couriers = courier_controller.find_all_couriers_with_relations()
    return make_response(jsonify(couriers), HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>', methods=['GET'])
def get_courier(courier_id: int) -> Response:
    courier = courier_controller.find_courier_with_relations(courier_id)
    return make_response(jsonify(courier), HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>/regular_customers/<int:customer_id>', methods=['POST'])
def add_regular_customer(courier_id: int, customer_id: int) -> Response:
    courier_controller.add_regular_customer(courier_id, customer_id)
    return make_response("Regular customer added", HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>/regular_customers/<int:customer_id>', methods=['DELETE'])
def remove_regular_customer(courier_id: int, customer_id: int) -> Response:
    courier_controller.remove_regular_customer(courier_id, customer_id)
    return make_response("Regular customer removed", HTTPStatus.OK)

@courier_bp.route('', methods=['POST'])
def create_courier() -> Response:
    content = request.get_json()
    courier = Courier.create_from_dto(content)
    courier_controller.create(courier)
    return make_response(jsonify(courier.put_into_dto(include_regular_customers=True)), HTTPStatus.CREATED)

@courier_bp.route('/<int:courier_id>', methods=['PUT'])
def update_courier(courier_id: int) -> Response:
    content = request.get_json()
    courier = Courier.create_from_dto(content)
    courier_controller.update(courier_id, courier)
    return make_response("Courier updated", HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>', methods=['PATCH'])
def patch_courier(courier_id: int) -> Response:
    content = request.get_json()
    courier_controller.patch(courier_id, content)
    return make_response("Courier updated", HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>', methods=['DELETE'])
def delete_courier(courier_id: int) -> Response:
    courier_controller.delete(courier_id)
    return make_response("Courier deleted", HTTPStatus.OK)
