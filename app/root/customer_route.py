from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import customer_controller
from ..domain.customer import Customer

customer_bp = Blueprint('customer', __name__, url_prefix='/customers')

@customer_bp.route('', methods=['GET'])
def get_all_customers() -> Response:
    return make_response(jsonify(customer_controller.find_all()), HTTPStatus.OK)

@customer_bp.route('', methods=['POST'])
def create_customer() -> Response:
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customer_controller.create(customer)
    return make_response(jsonify(customer.put_into_dto()), HTTPStatus.CREATED)

@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id: int) -> Response:
    return make_response(jsonify(customer_controller.find_by_id(customer_id)), HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id: int) -> Response:
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customer_controller.update(customer_id, customer)
    return make_response("Customer updated", HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=['PATCH'])
def patch_customer(customer_id: int) -> Response:
    content = request.get_json()
    customer_controller.patch(customer_id, content)
    return make_response("Customer updated", HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id: int) -> Response:
    customer_controller.delete(customer_id)
    return make_response("Customer deleted", HTTPStatus.OK)