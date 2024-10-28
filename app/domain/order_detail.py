from __future__ import annotations
from typing import Dict, Any
from app import db

class OrderDetail(db.Model):
    __tablename__ = 'order_detail'

    order_detail_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    addon_id = db.Column(db.Integer, db.ForeignKey('addon.addon_id'), nullable=True)

    order = db.relationship('Order', back_populates='order_details')
    product = db.relationship('Product', back_populates='order_details')
    addon = db.relationship('Addon', back_populates='order_details')

    def __init__(self, order_id: int, product_id: int, quantity: int, price: float, addon_id: int = None, order_detail_id: int = None):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.addon_id = addon_id

    def __repr__(self) -> str:
        return f"OrderDetail({self.order_detail_id}, {self.order_id}, {self.product_id}, {self.quantity}, {self.price}, {self.addon_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'order_detail_id': self.order_detail_id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.price,
            'addon_id': self.addon_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> OrderDetail:
        return OrderDetail(
            order_detail_id=dto_dict.get('order_detail_id'),
            order_id=dto_dict.get('order_id'),
            product_id=dto_dict.get('product_id'),
            quantity=dto_dict.get('quantity'),
            price=dto_dict.get('price'),
            addon_id=dto_dict.get('addon_id')
        )
