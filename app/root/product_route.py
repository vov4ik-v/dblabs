from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller.product_controller import ProductController
from ..domain import Product

product_bp = Blueprint('product', __name__, url_prefix='/products')
product_controller = ProductController()

@product_bp.route('', methods=['GET'])
def get_all_products() -> Response:
    """
    List all products (with ingredients)
    ---
    tags: [product]
    responses:
      200:
        description: List of products with ingredients
        content:
          application/json:
            schema: {type: array, items: {type: object}}
    """
    products = product_controller.find_all_products_with_ingredients()
    return make_response(jsonify(products), HTTPStatus.OK)


@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id: int) -> Response:
    """
    Get product by ID (with ingredients)
    ---
    tags: [product]
    parameters:
      - in: path
        name: product_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: OK}
      404: {description: Not found}
    """
    product = product_controller.find_product_with_ingredients(product_id)
    return make_response(jsonify(product), HTTPStatus.OK)


@product_bp.route('', methods=['POST'])
def create_product() -> Response:
    """
    Create a new product
    ---
    tags: [product]
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required: [name, price]
            properties:
              name: {type: string, example: "Pizza Margherita"}
              price: {type: number, example: 12.5}
              ingredient_ids:
                type: array
                items: {type: integer}
                example: [1,2,3]
    responses:
      201: {description: Created}
    """
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.create(product)
    return make_response(jsonify(product.put_into_dto()), HTTPStatus.CREATED)


@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id: int) -> Response:
    """
    Replace product by ID
    ---
    tags: [product]
    parameters:
      - in: path
        name: product_id
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
    product = Product.create_from_dto(content)
    product_controller.update(product_id, product)
    return make_response("Product updated", HTTPStatus.OK)


@product_bp.route('/<int:product_id>', methods=['PATCH'])
def patch_product(product_id: int) -> Response:
    """
    Partially update product by ID
    ---
    tags: [product]
    parameters:
      - in: path
        name: product_id
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
    product_controller.patch(product_id, content)
    return make_response("Product updated", HTTPStatus.OK)


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int) -> Response:
    """
    Delete product by ID
    ---
    tags: [product]
    parameters:
      - in: path
        name: product_id
        required: true
        schema: {type: integer}
    responses:
      200: {description: Deleted}
      404: {description: Not found}
    """
    product_controller.delete(product_id)
    return make_response("Product deleted", HTTPStatus.OK)

