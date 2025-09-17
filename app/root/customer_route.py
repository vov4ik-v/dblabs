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
    tags: [customer]
    responses:
      200:
        description: List of customers with addresses
        content:
          application/json:
            schema: {type: array, items: {type: object}}
    """
    customers = customer_controller.find_all(Customer.addresses)
    return make_response(jsonify(customers), HTTPStatus.OK)


@customer_bp.route('', methods=['POST'])
def create_customer() -> Response:
    """
    Create a new customer
    ---
    tags: [customer]
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [name, email]
            properties:
              name: {type: string, example: "John Doe"}
              email: {type: string, example: "john@example.com"}
              phone: {type: string, example: "+380501112233"}
    responses:
      201: {description: Created}
    """
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customer_controller.create(customer)
    return make_response(jsonify(customer.put_into_dto()), HTTPStatus.CREATED)


@customer_bp.route('/<int:customer_id>', methods=['GET'])
def get_customer(customer_id: int) -> Response:
    """
    Get customer by ID (with addresses)
    ---
    tags: [customer]
    parameters:
      - in: path
        name: customer_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: OK}
      404: {description: Not found}
    """
    customer = customer_controller.find_by_id(customer_id, Customer.addresses)
    return make_response(jsonify(customer), HTTPStatus.OK)


@customer_bp.route('/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id: int) -> Response:
    """
    Replace customer by ID
    ---
    tags: [customer]
    parameters:
      - in: path
        name: customer_id
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
    customer = Customer.create_from_dto(content)
    customer_controller.update(customer_id, customer)
    return make_response("Customer updated", HTTPStatus.OK)


@customer_bp.route('/<int:customer_id>', methods=['PATCH'])
def patch_customer(customer_id: int) -> Response:
    """
    Partially update customer by ID
    ---
    tags: [customer]
    parameters:
      - in: path
        name: customer_id
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
    customer_controller.patch(customer_id, content)
    return make_response("Customer updated", HTTPStatus.OK)


@customer_bp.route('/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id: int) -> Response:
    """
    Delete customer by ID
    ---
    tags: [customer]
    parameters:
      - in: path
        name: customer_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    customer_controller.delete(customer_id)
    return make_response("Customer deleted", HTTPStatus.OK)
