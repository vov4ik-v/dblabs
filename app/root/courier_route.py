from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from sqlalchemy import text

from app.extensions import db
from ..controller import courier_controller
from ..domain.courier import Courier, customer_courier
from ..service import customer_service, courier_service

courier_bp = Blueprint('courier', __name__, url_prefix='/couriers')


@courier_bp.route('/all/customers', methods=['GET'])
def get_customer_courier_details() -> Response:
    customer_courier_records = db.session.query(customer_courier).all()

    details_dict = {}

    for record in customer_courier_records:
        customer = customer_service.find_by_id_with_relations(record.customer_id)
        courier = courier_service.find_by_id_with_relations(record.courier_id)

        if customer and courier:
            details_dict[record.customer_courier_id] = {
                "customer": {
                    "customer_id": customer.customer_id,
                    "name": customer.name,
                    "phone": customer.phone,
                    "email": customer.email,
                },
                "courier": {
                    "courier_id": courier.courier_id,
                    "name": courier.name,
                    "phone": courier.phone
                }
            }

    return make_response(jsonify(details_dict), HTTPStatus.OK)

@courier_bp.route('/<int:customer_courier_id>/customers', methods=['GET'])
def get_customer_courier_detail_by_id(customer_courier_id: int) -> Response:
    record = db.session.query(customer_courier).filter_by(customer_courier_id=customer_courier_id).first()

    if not record:
        return make_response("Customer-Courier relationship not found", HTTPStatus.NOT_FOUND)

    customer = customer_service.find_by_id_with_relations(record.customer_id)
    courier = courier_service.find_by_id_with_relations(record.courier_id)

    if customer and courier:
        detail = {
            "customer": {
                "customer_id": customer.customer_id,
                "name": customer.name,
                "phone": customer.phone,
                "email": customer.email,
            },
            "courier": {
                "courier_id": courier.courier_id,
                "name": courier.name,
                "phone": courier.phone
            }
        }
        return make_response(jsonify(detail), HTTPStatus.OK)

    return make_response("Customer or Courier details not found", HTTPStatus.NOT_FOUND)


@courier_bp.route('/insert_10_couriers', methods=['POST'])
def insert_10_couriers():
    try:
        # Використовуємо text() для обгортання SQL-запиту
        db.session.execute(text("CALL insert_10_couriers()"))
        db.session.commit()
        return jsonify({"message": "10 couriers inserted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@courier_bp.route('', methods=['GET'])
def get_all_couriers() -> Response:
    couriers = courier_controller.find_all_couriers_with_relations()
    return make_response(jsonify(couriers), HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>', methods=['GET'])
def get_courier(courier_id: int) -> Response:
    courier = courier_controller.find_courier_with_relations(courier_id)
    return make_response(jsonify(courier), HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>/regular_customers/<int:customer_id>', methods=['POST'])
def add_regular_customer(courier_id: int, customer_id: int) -> Response:
    courier_controller.add_regular_customer(courier_id, customer_id)
    return make_response("Regular customer added", HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>/regular_customers/<int:customer_id>', methods=['DELETE'])
def remove_regular_customer(courier_id: int, customer_id: int) -> Response:
    courier_controller.remove_regular_customer(courier_id, customer_id)
    return make_response("Regular customer removed", HTTPStatus.OK)

@courier_bp.route('', methods=['POST'])
def create_courier() -> Response:
    content = request.get_json()
    courier = Courier.create_from_dto(content)
    courier_controller.create(courier)
    return make_response(jsonify(courier.put_into_dto(include_regular_customers=True)), HTTPStatus.CREATED)

@courier_bp.route('/<int:courier_id>', methods=['PUT'])
def update_courier(courier_id: int) -> Response:
    content = request.get_json()
    courier = Courier.create_from_dto(content)
    courier_controller.update(courier_id, courier)
    return make_response("Courier updated", HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>', methods=['PATCH'])
def patch_courier(courier_id: int) -> Response:
    content = request.get_json()
    courier_controller.patch(courier_id, content)
    return make_response("Courier updated", HTTPStatus.OK)

@courier_bp.route('/<int:courier_id>', methods=['DELETE'])
def delete_courier(courier_id: int) -> Response:
    courier_controller.delete(courier_id)
    return make_response("Courier deleted", HTTPStatus.OK)
