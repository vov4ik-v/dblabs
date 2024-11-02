from __future__ import annotations
from typing import Dict, Any
from app import db

class Addon(db.Model):
    __tablename__ = 'addon'

    addon_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    order_details = db.relationship('OrderDetail', back_populates='addon')


    def __init__(self, name: str, price: float, addon_id: int = None):
        self.addon_id = addon_id
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"Addon({self.addon_id}, '{self.name}', {self.price})"

    def put_into_dto(self) -> Dict[str, Any]:
        """Перетворення об'єкта на DTO-формат."""
        return {
            'addon_id': self.addon_id,
            'name': self.name,
            'price': self.price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Addon:
        """Створює об'єкт Addon із словника DTO."""
        return Addon(
            name=dto_dict.get('name'),
            price=dto_dict.get('price')
        )
