from __future__ import annotations
from typing import Dict, Any
from app.extensions import db

class CustomerAddress(db.Model):
    __tablename__ = 'customer_address'

    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)

    customer = db.relationship('Customer', back_populates='addresses')
    orders = db.relationship('Order', back_populates='address')

    def __init__(self, customer_id: int, address: str, city: str, zip_code: str, address_id: int = None):
        self.address_id = address_id
        self.customer_id = customer_id
        self.address = address
        self.city = city
        self.zip_code = zip_code

    def __repr__(self) -> str:
        return f"CustomerAddress({self.address_id}, {self.customer_id}, '{self.address}', '{self.city}', '{self.zip_code}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'address_id': self.address_id,
            'customer_id': self.customer_id,
            'address': self.address,
            'city': self.city,
            'zip_code': self.zip_code
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CustomerAddress:
        return CustomerAddress(
            address_id=dto_dict.get('address_id'),
            customer_id=dto_dict.get('customer_id'),
            address=dto_dict.get('address'),
            city=dto_dict.get('city'),
            zip_code=dto_dict.get('zip_code')
        )
