from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import addon_controller
from ..domain.addon import Addon

addon_bp = Blueprint('addon', __name__, url_prefix='/addon')


@addon_bp.route('', methods=['GET'])
def get_all_addons() -> Response:
    """
    List all addons
    ---
    tags: [addon]
    responses:
      200:
        description: List of addons
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id: {type: integer, example: 1}
                  name: {type: string, example: "Extra cheese"}
                  price: {type: number, example: 1.5}
    """
    return make_response(jsonify(addon_controller.find_all()), HTTPStatus.OK)


@addon_bp.route('', methods=['POST'])
def create_addon() -> Response:
    """
    Create a new addon
    ---
    tags: [addon]
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [name, price]
            properties:
              name: {type: string, example: "Extra cheese"}
              price: {type: number, example: 1.5}
    responses:
      201:
        description: Created addon
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    addon = Addon.create_from_dto(content)
    addon_controller.create(addon)
    return make_response(jsonify(addon.put_into_dto()), HTTPStatus.CREATED)


@addon_bp.route('/<int:addon_id>', methods=['GET'])
def get_addon(addon_id: int) -> Response:
    """
    Get addon by ID
    ---
    tags: [addon]
    parameters:
      - in: path
        name: addon_id
        required: true
        schema: {type: integer}
    responses:
      200:
        description: Addon found
      404:
        description: Addon not found
    """
    return make_response(jsonify(addon_controller.find_by_id(addon_id)), HTTPStatus.OK)


@addon_bp.route('/<int:addon_id>', methods=['PUT'])
def update_addon(addon_id: int) -> Response:
    """
    Replace addon by ID
    ---
    tags: [addon]
    parameters:
      - in: path
        name: addon_id
        required: true
        schema: {type: integer}
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name: {type: string}
              price: {type: number}
    responses:
      200:
        description: Updated
      404:
        description: Addon not found
    """
    content = request.get_json()
    addon = Addon.create_from_dto(content)
    addon_controller.update(addon_id, addon)
    return make_response("Addon updated", HTTPStatus.OK)


@addon_bp.route('/<int:addon_id>', methods=['PATCH'])
def patch_addon(addon_id: int) -> Response:
    """
    Partially update addon by ID
    ---
    tags: [addon]
    parameters:
      - in: path
        name: addon_id
        required: true
        schema: {type: integer}
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
    responses:
      200:
        description: Patched
      404:
        description: Addon not found
    """
    content = request.get_json()
    addon_controller.patch(addon_id, content)
    return make_response("Addon updated", HTTPStatus.OK)


@addon_bp.route('/<int:addon_id>', methods=['DELETE'])
def delete_addon(addon_id: int) -> Response:
    """
    Delete addon by ID
    ---
    tags: [addon]
    parameters:
      - in: path
        name: addon_id
        required: true
        schema: {type: integer}
    responses:
      200:
        description: Deleted
      404:
        description: Addon not found
    """
    addon_controller.delete(addon_id)
    return make_response("Addon deleted", HTTPStatus.OK)
