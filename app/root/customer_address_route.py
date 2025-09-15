from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.customer_address_controller import CustomerAddressController
from ..domain.customer_address import CustomerAddress

customer_address_bp = Blueprint('customer_address', __name__, url_prefix='/customer_addresses')
customer_address_controller = CustomerAddressController()

@customer_address_bp.route('', methods=['GET'])
def get_all_customer_addresses() -> Response:
    # Load customer relationships for each customer address
    customer_addresses = customer_address_controller.find_all(CustomerAddress.customer)
    return make_response(jsonify(customer_addresses), HTTPStatus.OK)

@customer_address_bp.route('', methods=['POST'])
def create_customer_address() -> Response:
    content = request.get_json()
    customer_address = CustomerAddress.create_from_dto(content)
    customer_address_controller.create(customer_address)
    return make_response(jsonify(customer_address.put_into_dto()), HTTPStatus.CREATED)

@customer_address_bp.route('/<int:address_id>', methods=['GET'])
def get_customer_address(address_id: int) -> Response:
    # Load customer relationship for a single customer address
    customer_address = customer_address_controller.find_by_id_with_relations(address_id, CustomerAddress.customer)
    return make_response(jsonify(customer_address), HTTPStatus.OK)

@customer_address_bp.route('/<int:address_id>', methods=['PUT'])
def update_customer_address(address_id: int) -> Response:
    content = request.get_json()
    customer_address = CustomerAddress.create_from_dto(content)
    customer_address_controller.update(address_id, customer_address)
    return make_response("CustomerAddress updated", HTTPStatus.OK)

@customer_address_bp.route('/<int:address_id>', methods=['PATCH'])
def patch_customer_address(address_id: int) -> Response:
    content = request.get_json()
    customer_address_controller.patch(address_id, content)
    return make_response("CustomerAddress updated", HTTPStatus.OK)

@customer_address_bp.route('/<int:address_id>', methods=['DELETE'])
def delete_customer_address(address_id: int) -> Response:
    customer_address_controller.delete(address_id)
    return make_response("CustomerAddress deleted", HTTPStatus.OK)
