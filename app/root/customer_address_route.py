from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.customer_address_controller import CustomerAddressController
from ..domain.customer_address import CustomerAddress

customer_address_bp = Blueprint('customer_address', __name__, url_prefix='/customer_addresses')
customer_address_controller = CustomerAddressController()

@customer_address_bp.route('', methods=['GET'])
def get_all_customer_addresses() -> Response:
    """
    List all customer addresses (with customer relation)
    ---
    tags: [customer_address]
    responses:
      200:
        description: List of customer addresses
        content:
          application/json:
            schema: {type: array, items: {type: object}}
    """
    customer_addresses = customer_address_controller.find_all(CustomerAddress.customer)
    return make_response(jsonify(customer_addresses), HTTPStatus.OK)


@customer_address_bp.route('', methods=['POST'])
def create_customer_address() -> Response:
    """
    Create a new customer address
    ---
    tags: [customer_address]
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [customer_id, address]
            properties:
              customer_id: {type: integer, example: 1}
              address: {type: string, example: "1 High St, London"}
              city: {type: string, example: "Kyiv"}
              postal_code: {type: string, example: "01001"}
    responses:
      201: {description: Created}
    """
    content = request.get_json()
    customer_address = CustomerAddress.create_from_dto(content)
    customer_address_controller.create(customer_address)
    return make_response(jsonify(customer_address.put_into_dto()), HTTPStatus.CREATED)


@customer_address_bp.route('/<int:address_id>', methods=['GET'])
def get_customer_address(address_id: int) -> Response:
    """
    Get customer address by ID (with customer relation)
    ---
    tags: [customer_address]
    parameters:
      - in: path
        name: address_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: OK}
      404: {description: Not found}
    """
    customer_address = customer_address_controller.find_by_id(address_id, CustomerAddress.customer)
    return make_response(jsonify(customer_address), HTTPStatus.OK)


@customer_address_bp.route('/<int:address_id>', methods=['PUT'])
def update_customer_address(address_id: int) -> Response:
    """
    Replace customer address by ID
    ---
    tags: [customer_address]
    parameters:
      - in: path
        name: address_id
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
    customer_address = CustomerAddress.create_from_dto(content)
    customer_address_controller.update(address_id, customer_address)
    return make_response("CustomerAddress updated", HTTPStatus.OK)


@customer_address_bp.route('/<int:address_id>', methods=['PATCH'])
def patch_customer_address(address_id: int) -> Response:
    """
    Partially update customer address by ID
    ---
    tags: [customer_address]
    parameters:
      - in: path
        name: address_id
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
    customer_address_controller.patch(address_id, content)
    return make_response("CustomerAddress updated", HTTPStatus.OK)


@customer_address_bp.route('/<int:address_id>', methods=['DELETE'])
def delete_customer_address(address_id: int) -> Response:
    """
    Delete customer address by ID
    ---
    tags: [customer_address]
    parameters:
      - in: path
        name: address_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    customer_address_controller.delete(address_id)
    return make_response("CustomerAddress deleted", HTTPStatus.OK)
