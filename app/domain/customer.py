from __future__ import annotations
from typing import Dict, Any
from app import db

class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=True)

    def __init__(self, name: str, phone: str, email: str = None, customer_id: int = None):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self) -> str:
        return f"Customer({self.customer_id}, '{self.name}', '{self.phone}', '{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Customer:
        return Customer(
            customer_id=dto_dict.get('customer_id'),
            name=dto_dict.get('name'),
            phone=dto_dict.get('phone'),
            email=dto_dict.get('email')
        )
