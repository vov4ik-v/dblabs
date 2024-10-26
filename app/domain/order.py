from __future__ import annotations
from typing import Dict, Any
from app import db

class Order(db.Model):
    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, nullable=False)
    address_id = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.String(50), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, customer_id: int, address_id: int, order_date: str, total_price: float, status: str, order_id: int = None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.address_id = address_id
        self.order_date = order_date
        self.total_price = total_price
        self.status = status

    def __repr__(self) -> str:
        return f"Order({self.order_id}, {self.customer_id}, {self.address_id}, '{self.order_date}', {self.total_price}, '{self.status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'address_id': self.address_id,
            'order_date': self.order_date,
            'total_price': self.total_price,
            'status': self.status
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        return Order(
            order_id=dto_dict.get('order_id'),
            customer_id=dto_dict.get('customer_id'),
            address_id=dto_dict.get('address_id'),
            order_date=dto_dict.get('order_date'),
            total_price=dto_dict.get('total_price'),
            status=dto_dict.get('status')
        )
