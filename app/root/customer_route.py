from ..domain.customer import Customer

from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.customer_controller import CustomerController

customer_bp = Blueprint('customer', __name__, url_prefix='/customers')
customer_controller = CustomerController()

@customer_bp.route('', methods=['GET'])
def get_all_customers() -> Response:
    customers = customer_controller.find_all_customers_with_relations()
    return make_response(jsonify(customers), HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id: int) -> Response:
    customer = customer_controller.find_customer_with_relations(customer_id)
    return make_response(jsonify(customer), HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>/favorite_couriers/<int:courier_id>', methods=['POST'])
def add_favorite_courier(customer_id: int, courier_id: int) -> Response:
    customer_controller.add_favorite_courier(customer_id, courier_id)
    return make_response("Favorite courier added", HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>/favorite_couriers/<int:courier_id>', methods=['DELETE'])
def remove_favorite_courier(customer_id: int, courier_id: int) -> Response:
    customer_controller.remove_favorite_courier(customer_id, courier_id)
    return make_response("Favorite courier removed", HTTPStatus.OK)

@customer_bp.route('', methods=['POST'])
def create_customer() -> Response:
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customer_controller.create(customer)
    return make_response(jsonify(customer.put_into_dto(include_addresses=False, include_favorite_couriers=False)), HTTPStatus.CREATED)

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

@customer_bp.route('/create_dynamic_tables', methods=['POST'])
def create_dynamic_tables():
    response, status = customer_controller.create_dynamic_tables()
    return jsonify(response), status
