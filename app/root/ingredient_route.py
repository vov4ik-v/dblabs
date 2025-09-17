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
    tags: [ingredient]
    responses:
      200:
        description: List of ingredients
        content:
          application/json:
            schema: {type: array, items: {type: object}}
    """
    return make_response(jsonify(ingredient_controller.find_all()), HTTPStatus.OK)


@ingredient_bp.route('', methods=['POST'])
def create_ingredient() -> Response:
    """
    Create a new ingredient
    ---
    tags: [ingredient]
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [name]
            properties:
              name: {type: string, example: "Tomato"}
    responses:
      201: {description: Created}
    """
    content = request.get_json()
    ingredient = Ingredient.create_from_dto(content)
    ingredient_controller.create(ingredient)
    return make_response(jsonify(ingredient.put_into_dto()), HTTPStatus.CREATED)


@ingredient_bp.route('/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id: int) -> Response:
    """
    Get ingredient by ID
    ---
    tags: [ingredient]
    parameters:
      - in: path
        name: ingredient_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: OK}
      404: {description: Not found}
    """
    return make_response(jsonify(ingredient_controller.find_by_id(ingredient_id)), HTTPStatus.OK)


@ingredient_bp.route('/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id: int) -> Response:
    """
    Replace ingredient by ID
    ---
    tags: [ingredient]
    parameters:
      - in: path
        name: ingredient_id
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
    ingredient = Ingredient.create_from_dto(content)
    ingredient_controller.update(ingredient_id, ingredient)
    return make_response("Ingredient updated", HTTPStatus.OK)


@ingredient_bp.route('/<int:ingredient_id>', methods=['PATCH'])
def patch_ingredient(ingredient_id: int) -> Response:
    """
    Partially update ingredient by ID
    ---
    tags: [ingredient]
    parameters:
      - in: path
        name: ingredient_id
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
    ingredient_controller.patch(ingredient_id, content)
    return make_response("Ingredient updated", HTTPStatus.OK)


@ingredient_bp.route('/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id: int) -> Response:
    """
    Delete ingredient by ID
    ---
    tags: [ingredient]
    parameters:
      - in: path
        name: ingredient_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    ingredient_controller.delete(ingredient_id)
    return make_response("Ingredient deleted", HTTPStatus.OK)

