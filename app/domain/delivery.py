from __future__ import annotations
from typing import Dict, Any
from app import db

class Delivery(db.Model):
    __tablename__ = 'delivery'

    delivery_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, nullable=False)
    courier_id = db.Column(db.Integer, nullable=False)
    expected_delivery_time = db.Column(db.String(50), nullable=False)
    actual_delivery_time = db.Column(db.String(50), nullable=True)
    delivery_fee = db.Column(db.Float, nullable=False, default=0.0)

    def __init__(self, order_id: int, courier_id: int, expected_delivery_time: str, actual_delivery_time: str = None, delivery_fee: float = 0.0, delivery_id: int = None):
        self.delivery_id = delivery_id
        self.order_id = order_id
        self.courier_id = courier_id
        self.expected_delivery_time = expected_delivery_time
        self.actual_delivery_time = actual_delivery_time
        self.delivery_fee = delivery_fee

    def __repr__(self) -> str:
        return f"Delivery({self.delivery_id}, {self.order_id}, {self.courier_id}, '{self.expected_delivery_time}', '{self.actual_delivery_time}', {self.delivery_fee})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'delivery_id': self.delivery_id,
            'order_id': self.order_id,
            'courier_id': self.courier_id,
            'expected_delivery_time': self.expected_delivery_time,
            'actual_delivery_time': self.actual_delivery_time,
            'delivery_fee': self.delivery_fee
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Delivery:
        return Delivery(
            delivery_id=dto_dict.get('delivery_id'),
            order_id=dto_dict.get('order_id'),
            courier_id=dto_dict.get('courier_id'),
            expected_delivery_time=dto_dict.get('expected_delivery_time'),
            actual_delivery_time=dto_dict.get('actual_delivery_time'),
            delivery_fee=dto_dict.get('delivery_fee')
        )
