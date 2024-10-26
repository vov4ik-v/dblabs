from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import addon_controller
from ..domain.addon import Addon

addon_bp = Blueprint('addon', __name__, url_prefix='/addon')


@addon_bp.route('', methods=['GET'])
def get_all_addons() -> Response:
    return make_response(jsonify(addon_controller.find_all()), HTTPStatus.OK)


@addon_bp.route('', methods=['POST'])
def create_addon() -> Response:
    content = request.get_json()
    addon = Addon.create_from_dto(content)
    addon_controller.create(addon)
    return make_response(jsonify(addon.put_into_dto()), HTTPStatus.CREATED)


@addon_bp.route('/<int:addon_id>', methods=['GET'])
def get_addon(addon_id: int) -> Response:
    return make_response(jsonify(addon_controller.find_by_id(addon_id)), HTTPStatus.OK)


@addon_bp.route('/<int:addon_id>', methods=['PUT'])
def update_addon(addon_id: int) -> Response:
    content = request.get_json()
    addon = Addon.create_from_dto(content)
    addon_controller.update(addon_id, addon)
    return make_response("Addon updated", HTTPStatus.OK)


@addon_bp.route('/<int:addon_id>', methods=['PATCH'])
def patch_addon(addon_id: int) -> Response:
    content = request.get_json()
    addon_controller.patch(addon_id, content)
    return make_response("Addon updated", HTTPStatus.OK)


@addon_bp.route('/<int:addon_id>', methods=['DELETE'])
def delete_addon(addon_id: int) -> Response:
    addon_controller.delete(addon_id)
    return make_response("Addon deleted", HTTPStatus.OK)
