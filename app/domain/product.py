from __future__ import annotations
from typing import Dict, Any
from app import db

class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name: str, type: str, price: float, product_id: int = None):
        self.product_id = product_id
        self.name = name
        self.type = type
        self.price = price

    def __repr__(self) -> str:
        return f"Product({self.product_id}, '{self.name}', '{self.type}', {self.price})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'product_id': self.product_id,
            'name': self.name,
            'type': self.type,
            'price': self.price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Product:
        return Product(
            product_id=dto_dict.get('product_id'),
            name=dto_dict.get('name'),
            type=dto_dict.get('type'),
            price=dto_dict.get('price')
        )
