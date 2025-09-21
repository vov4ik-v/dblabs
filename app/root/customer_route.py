# app/route/customer_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.customer_controller import CustomerController
from ..domain.customer import Customer

customer_bp = Blueprint('customer', __name__, url_prefix='/customers')
customer_controller = CustomerController()


@customer_bp.route('', methods=['GET'])
def get_all_customers() -> Response:
    """
    List all customers (with addresses)
    ---
    tags:
      - Customer
    responses:
      200:
        description: List of customers with addresses
        schema:
          type: array
          items:
            type: object
    """
    customers = customer_controller.find_all(Customer.addresses)
    return make_response(jsonify(customers), HTTPStatus.OK)


@customer_bp.route('', methods=['POST'])
def create_customer() -> Response:
    """
    Create a new customer
    ---
    tags:
      - Customer
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/CustomerCreate'
    responses:
      201:
        description: Created
        schema:
          $ref: '#/definitions/Customer'
    """
    content = request.get_json() or {}
    customer = Customer.create_from_dto(content)
    customer_controller.create(customer)
    return make_response(jsonify(customer.put_into_dto()), HTTPStatus.CREATED)


@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id: int) -> Response:
    """
    Get customer by ID (with addresses)
    ---
    tags:
      - Customer
    parameters:
      - in: path
        name: customer_id
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
    customer = customer_controller.find_by_id(customer_id, Customer.addresses)
    return make_response(jsonify(customer), HTTPStatus.OK)


@customer_bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id: int) -> Response:
    """
    Replace customer by ID
    ---
    tags:
      - Customer
    parameters:
      - in: path
        name: customer_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/CustomerUpdate'
    responses:
      200:
        description: Updated
        schema:
          $ref: '#/definitions/Customer'
      404:
        description: Not found
    """
    content = request.get_json() or {}
    customer = Customer.create_from_dto(content)
    customer_controller.update(customer_id, customer)
    updated = customer_controller.find_by_id(customer_id, Customer.addresses)
    return make_response(jsonify(updated), HTTPStatus.OK)


@customer_bp.route('/<int:customer_id>', methods=['PATCH'])
def patch_customer(customer_id: int) -> Response:
    """
    Partially update customer by ID
    ---
    tags:
      - Customer
    parameters:
      - in: path
        name: customer_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/CustomerUpdate'
    responses:
      200:
        description: Updated
        schema:
          type: object
      404:
        description: Not found
    """
    content = request.get_json() or {}
    customer_controller.patch(customer_id, content)
    updated = customer_controller.find_by_id(customer_id, Customer.addresses)
    return make_response(jsonify(updated), HTTPStatus.OK)


@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id: int) -> Response:
    """
    Delete customer by ID
    ---
    tags:
      - Customer
    parameters:
      - in: path
        name: customer_id
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
    customer_controller.delete(customer_id)
    return make_response(jsonify({"message": "Customer deleted"}), HTTPStatus.OK)
