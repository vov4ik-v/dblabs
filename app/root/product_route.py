# app/route/product_route.py
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
    tags:
      - Product
    responses:
      200:
        description: List of products with ingredients
        schema:
          type: array
          items:
            type: object
    """
    products = product_controller.find_all_products_with_ingredients()
    return make_response(jsonify(products), HTTPStatus.OK)


@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id: int) -> Response:
    """
    Get product by ID (with ingredients)
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
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
    product = product_controller.find_product_with_ingredients(product_id)
    return make_response(jsonify(product), HTTPStatus.OK)


@product_bp.route('', methods=['POST'])
def create_product() -> Response:
    """
    Create a new product
    ---
    tags:
      - Product
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ProductCreate'
    responses:
      201:
        description: Created
        schema:
          $ref: '#/definitions/Product'
    """
    content = request.get_json() or {}
    product = Product.create_from_dto(content)
    product_controller.create(product)
    return make_response(jsonify(product.put_into_dto()), HTTPStatus.CREATED)


@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id: int) -> Response:
    """
    Replace product by ID
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ProductUpdate'
    responses:
      200:
        description: Updated
        schema:
          $ref: '#/definitions/Product'
      404:
        description: Not found
    """
    content = request.get_json() or {}
    product = Product.create_from_dto(content)
    product_controller.update(product_id, product)
    updated = product_controller.find_product_with_ingredients(product_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@product_bp.route('/<int:product_id>', methods=['PATCH'])
def patch_product(product_id: int) -> Response:
    """
    Partially update product by ID
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ProductUpdate'
    responses:
      200:
        description: Updated
        schema:
          type: object
      404:
        description: Not found
    """
    content = request.get_json() or {}
    product_controller.patch(product_id, content)
    updated = product_controller.find_product_with_ingredients(product_id)
    return make_response(jsonify(updated), HTTPStatus.OK)


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int) -> Response:
    """
    Delete product by ID
    ---
    tags:
      - Product
    parameters:
      - in: path
        name: product_id
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
    product_controller.delete(product_id)
    return make_response(jsonify({"message": "Product deleted"}), HTTPStatus.OK)
