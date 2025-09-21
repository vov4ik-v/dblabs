# app/route/ingredient_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import ingredient_controller
from ..domain.ingredient import Ingredient

ingredient_bp = Blueprint('ingredient', __name__, url_prefix='/ingredients')


@ingredient_bp.route('', methods=['GET'])
def get_all_ingredients() -> Response:
    """
    List all ingredients
    ---
    tags:
      - Ingredient
    responses:
      200:
        description: List of ingredients
        schema:
          type: array
          items:
            type: object
    """
    return make_response(jsonify(ingredient_controller.find_all()), HTTPStatus.OK)


@ingredient_bp.route('', methods=['POST'])
def create_ingredient() -> Response:
    """
    Create a new ingredient
    ---
    tags:
      - Ingredient
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/IngredientCreate'
    responses:
      201:
        description: Created
        schema:
          $ref: '#/definitions/Ingredient'
    """
    content = request.get_json() or {}
    ingredient = Ingredient.create_from_dto(content)
    ingredient_controller.create(ingredient)
    return make_response(jsonify(ingredient.put_into_dto()), HTTPStatus.CREATED)


@ingredient_bp.route('/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id: int) -> Response:
    """
    Get ingredient by ID
    ---
    tags:
      - Ingredient
    parameters:
      - in: path
        name: ingredient_id
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
    return make_response(jsonify(ingredient_controller.find_by_id(ingredient_id)), HTTPStatus.OK)


@ingredient_bp.route('/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id: int) -> Response:
    """
    Replace ingredient by ID
    ---
    tags:
      - Ingredient
    parameters:
      - in: path
        name: ingredient_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/IngredientUpdate'
    responses:
      200:
        description: Updated
        schema:
          $ref: '#/definitions/Ingredient'
      404:
        description: Not found
    """
    content = request.get_json() or {}
    ingredient = Ingredient.create_from_dto(content)
    ingredient_controller.update(ingredient_id, ingredient)
    updated = ingredient_controller.find_by_id(ingredient_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@ingredient_bp.route('/<int:ingredient_id>', methods=['PATCH'])
def patch_ingredient(ingredient_id: int) -> Response:
    """
    Partially update ingredient by ID
    ---
    tags:
      - Ingredient
    parameters:
      - in: path
        name: ingredient_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/IngredientUpdate'
    responses:
      200:
        description: Updated
        schema:
          type: object
      404:
        description: Not found
    """
    content = request.get_json() or {}
    ingredient_controller.patch(ingredient_id, content)
    updated = ingredient_controller.find_by_id(ingredient_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@ingredient_bp.route('/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id: int) -> Response:
    """
    Delete ingredient by ID
    ---
    tags:
      - Ingredient
    parameters:
      - in: path
        name: ingredient_id
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
    ingredient_controller.delete(ingredient_id)
    return make_response(jsonify({"message": "Ingredient deleted"}), HTTPStatus.OK)
