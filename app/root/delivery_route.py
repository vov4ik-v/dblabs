from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.delivery_controller import DeliveryController
from ..domain.delivery import Delivery

delivery_bp = Blueprint('delivery', __name__, url_prefix='/deliveries')
delivery_controller = DeliveryController()

@delivery_bp.route('', methods=['GET'])
def get_all_deliveries() -> Response:
    """
    List all deliveries (with related entities)
    ---
    tags: [delivery]
    responses:
      200:
        description: List of deliveries with relations
        content:
          application/json:
            schema: {type: array, items: {type: object}}
    """
    deliveries = delivery_controller.find_all_deliveries_with_relations()
    return make_response(jsonify(deliveries), HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['GET'])
def get_delivery(delivery_id: int) -> Response:
    """
    Get delivery by ID (with related entities)
    ---
    tags: [delivery]
    parameters:
      - in: path
        name: delivery_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: OK}
      404: {description: Not found}
    """
    delivery = delivery_controller.find_delivery_with_relations(delivery_id)
    return make_response(jsonify(delivery), HTTPStatus.OK)


@delivery_bp.route('', methods=['POST'])
def create_delivery() -> Response:
    """
    Create a new delivery
    ---
    tags: [delivery]
    requestBody:
      required: true
      content:
        application/json:
          schema: {type: object}
    responses:
      201: {description: Created}
    """
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_controller.create(delivery)
    return make_response(jsonify(delivery.put_into_dto()), HTTPStatus.CREATED)


@delivery_bp.route('/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id: int) -> Response:
    """
    Replace delivery by ID
    ---
    tags: [delivery]
    parameters:
      - in: path
        name: delivery_id
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
    delivery = Delivery.create_from_dto(content)
    delivery_controller.update(delivery_id, delivery)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['PATCH'])
def patch_delivery(delivery_id: int) -> Response:
    """
    Partially update delivery by ID
    ---
    tags: [delivery]
    parameters:
      - in: path
        name: delivery_id
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
    delivery_controller.patch(delivery_id, content)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.route('/<int:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id: int) -> Response:
    """
    Delete delivery by ID
    ---
    tags: [delivery]
    parameters:
      - in: path
        name: delivery_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    delivery_controller.delete(delivery_id)
    return make_response("Delivery deleted", HTTPStatus.OK)
