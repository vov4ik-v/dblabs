from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from ..controller import addon_controller
from ..domain.addon import Addon

addon_bp = Blueprint("addon", __name__, url_prefix="/addon")


@addon_bp.route("", methods=["GET"])
def get_all_addons() -> Response:
    """
    Get all Addons
    ---
    tags:
      - Addon
    responses:
      200:
        description: List of addons
        schema:
          type: array
          items:
            $ref: '#/definitions/Addon'
    """
    return make_response(jsonify(addon_controller.find_all()), HTTPStatus.OK)


@addon_bp.route("", methods=["POST"])
def create_addon() -> Response:
    """
    Create a new Addon
    ---
    tags:
      - Addon
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/AddonCreate'
    responses:
      201:
        description: Created
        schema:
          $ref: '#/definitions/Addon'
      400:
        description: Invalid payload
    """
    content = request.get_json() or {}
    addon = Addon.create_from_dto(content)
    created = addon_controller.create(addon)
    return make_response(jsonify(created), HTTPStatus.CREATED)


@addon_bp.route("/<int:addon_id>", methods=["GET"])
def get_addon(addon_id: int) -> Response:
    """
    Get an Addon by ID
    ---
    tags:
      - Addon
    parameters:
      - in: path
        name: addon_id
        required: true
        type: integer
        description: Addon ID
    responses:
      200:
        description: Found addon
        schema:
          $ref: '#/definitions/Addon'
      404:
        description: Not found
    """
    return make_response(jsonify(addon_controller.find_by_id(addon_id)), HTTPStatus.OK)


@addon_bp.route("/<int:addon_id>", methods=["PUT"])
def update_addon(addon_id: int) -> Response:
    """
    Replace an Addon (PUT)
    ---
    tags:
      - Addon
    parameters:
      - in: path
        name: addon_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/AddonUpdate'
    responses:
      200:
        description: Updated addon
        schema:
          $ref: '#/definitions/Addon'
      404:
        description: Not found
    """
    content = request.get_json() or {}
    addon = Addon.create_from_dto(content)
    addon_controller.update(addon_id, addon)
    updated = addon_controller.find_by_id(addon_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@addon_bp.route("/<int:addon_id>", methods=["PATCH"])
def patch_addon(addon_id: int) -> Response:
    """
    Partially update an Addon (PATCH)
    ---
    tags:
      - Addon
    parameters:
      - in: path
        name: addon_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/AddonUpdate'
    responses:
      200:
        description: Patched addon
        schema:
          $ref: '#/definitions/Addon'
      404:
        description: Not found
    """
    content = request.get_json() or {}
    addon_controller.patch(addon_id, content)
    patched = addon_controller.find_by_id(addon_id)
    return make_response(jsonify(patched), HTTPStatus.OK)


@addon_bp.route("/<int:addon_id>", methods=["DELETE"])
def delete_addon(addon_id: int) -> Response:
    """
    Delete an Addon by ID
    ---
    tags:
      - Addon
    parameters:
      - in: path
        name: addon_id
        required: true
        type: integer
    responses:
      200:
        description: Deleted
        schema:
          type: object
          properties:
            message:
              type: string
              example: Addon deleted
      404:
        description: Not found
    """
    addon_controller.delete(addon_id)
    return make_response(jsonify({"message": "Addon deleted"}), HTTPStatus.OK)
