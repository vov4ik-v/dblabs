from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import ingredient_controller
from ..domain.ingredient import Ingredient

ingredient_bp = Blueprint('ingredient', __name__, url_prefix='/ingredients')

@ingredient_bp.route('', methods=['GET'])
def get_all_ingredients() -> Response:
    return make_response(jsonify(ingredient_controller.find_all()), HTTPStatus.OK)

@ingredient_bp.route('', methods=['POST'])
def create_ingredient() -> Response:
    content = request.get_json()
    ingredient = Ingredient.create_from_dto(content)
    ingredient_controller.create(ingredient)
    return make_response(jsonify(ingredient.put_into_dto()), HTTPStatus.CREATED)

@ingredient_bp.route('/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id: int) -> Response:
    return make_response(jsonify(ingredient_controller.find_by_id_with_relations(ingredient_id)), HTTPStatus.OK)

@ingredient_bp.route('/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id: int) -> Response:
    content = request.get_json()
    ingredient = Ingredient.create_from_dto(content)
    ingredient_controller.update(ingredient_id, ingredient)
    return make_response("Ingredient updated", HTTPStatus.OK)

@ingredient_bp.route('/<int:ingredient_id>', methods=['PATCH'])
def patch_ingredient(ingredient_id: int) -> Response:
    content = request.get_json()
    ingredient_controller.patch(ingredient_id, content)
    return make_response("Ingredient updated", HTTPStatus.OK)

@ingredient_bp.route('/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id: int) -> Response:
    ingredient_controller.delete(ingredient_id)
    return make_response("Ingredient deleted", HTTPStatus.OK)
