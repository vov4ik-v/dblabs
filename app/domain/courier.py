from __future__ import annotations
from typing import Dict, Any
from app import db

class Courier(db.Model):
    __tablename__ = 'courier'

    courier_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    deliveries = db.relationship('Delivery', back_populates='courier')

    def __init__(self, name: str, phone: str, courier_id: int = None):
        self.courier_id = courier_id
        self.name = name
        self.phone = phone

    def __repr__(self) -> str:
        return f"Courier({self.courier_id}, '{self.name}', '{self.phone}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'courier_id': self.courier_id,
            'name': self.name,
            'phone': self.phone
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Courier:
        return Courier(
            courier_id=dto_dict.get('courier_id'),
            name=dto_dict.get('name'),
            phone=dto_dict.get('phone')
        )
