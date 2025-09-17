from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import courier_controller
from ..domain.courier import Courier

courier_bp = Blueprint('courier', __name__, url_prefix='/courier')


@courier_bp.route('', methods=['GET'])
def get_all_couriers() -> Response:
    """
    List all couriers
    ---
    tags: [courier]
    responses:
      200:
        description: List of couriers
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(courier_controller.find_all()), HTTPStatus.OK)


@courier_bp.route('', methods=['POST'])
def create_courier() -> Response:
    """
    Create a new courier
    ---
    tags: [courier]
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [name, phone]
            properties:
              name: {type: string, example: "Alex Rider"}
              phone: {type: string, example: "+380501112233"}
    responses:
      201:
        description: Created courier
    """
    content = request.get_json()
    courier = Courier.create_from_dto(content)
    courier_controller.create(courier)
    return make_response(jsonify(courier.put_into_dto()), HTTPStatus.CREATED)


@courier_bp.route('/<int:courier_id>', methods=['GET'])
def get_courier(courier_id: int) -> Response:
    """
    Get courier by ID
    ---
    tags: [courier]
    parameters:
      - in: path
        name: courier_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: OK}
      404: {description: Courier not found}
    """
    return make_response(jsonify(courier_controller.find_by_id(courier_id)), HTTPStatus.OK)


@courier_bp.route('/<int:courier_id>', methods=['PUT'])
def update_courier(courier_id: int) -> Response:
    """
    Replace courier by ID
    ---
    tags: [courier]
    parameters:
      - in: path
        name: courier_id
        required: true
        schema: {type: integer}
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
    responses:
      200: {description: Updated}
      404: {description: Courier not found}
    """
    content = request.get_json()
    courier = Courier.create_from_dto(content)
    courier_controller.update(courier_id, courier)
    return make_response("Courier updated", HTTPStatus.OK)


@courier_bp.route('/<int:courier_id>', methods=['PATCH'])
def patch_courier(courier_id: int) -> Response:
    """
    Partially update courier by ID
    ---
    tags: [courier]
    parameters:
      - in: path
        name: courier_id
        required: true
        schema: {type: integer}
    requestBody:
      required: true
      content:
        application/json:
          schema: {type: object}
    responses:
      200: {description: Updated}
      404: {description: Courier not found}
    """
    content = request.get_json()
    courier_controller.patch(courier_id, content)
    return make_response("Courier updated", HTTPStatus.OK)


@courier_bp.route('/<int:courier_id>', methods=['DELETE'])
def delete_courier(courier_id: int) -> Response:
    """
    Delete courier by ID
    ---
    tags: [courier]
    parameters:
      - in: path
        name: courier_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: Deleted}
      404: {description: Courier not found}
    """
    courier_controller.delete(courier_id)
    return make_response("Courier deleted", HTTPStatus.OK)
