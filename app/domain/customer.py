from __future__ import annotations
from typing import Dict, Any
from app.extensions import db
from app.domain.courier import customer_courier


class Customer(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=True)

    addresses = db.relationship('CustomerAddress', back_populates='customer')
    orders = db.relationship('Order', back_populates='customer')

    favorite_couriers = db.relationship(
        'Courier',
        secondary=customer_courier,
        back_populates='regular_customers'
    )

    def put_into_dto(self, include_addresses: bool = True, include_favorite_couriers: bool = True) -> Dict[str, Any]:
        dto = {
            'customer_id': self.customer_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }
        if include_addresses:
            dto['addresses'] = [address.put_into_dto() for address in self.addresses]
        if include_favorite_couriers:
            dto['favorite_couriers'] = [courier.put_into_dto(include_regular_customers=False) for courier in self.favorite_couriers]
        return dto


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Customer:
        return Customer(
            customer_id=dto_dict.get('customer_id'),
            name=dto_dict.get('name'),
            phone=dto_dict.get('phone'),
            email=dto_dict.get('email')
        )
