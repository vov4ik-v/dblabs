from __future__ import annotations
from typing import Dict, Any
from app import db

customer_courier = db.Table(
    'customer_courier',  # Назва таблиці
    db.Column("customer_courier_id", db.Integer, primary_key=True),
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.customer_id'), primary_key=True),
    db.Column('courier_id', db.Integer, db.ForeignKey('courier.courier_id'), primary_key=True)
)


class Courier(db.Model):
    __tablename__ = 'courier'

    courier_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    deliveries = db.relationship('Delivery', back_populates='courier')

    regular_customers = db.relationship(
        'Customer',
        secondary=customer_courier,
        back_populates='favorite_couriers'
    )

    def put_into_dto(self, include_regular_customers: bool = True) -> Dict[str, Any]:
        dto = {
            'courier_id': self.courier_id,
            'name': self.name,
            'phone': self.phone
        }
        if include_regular_customers:
            dto['regular_customers'] = [customer.put_into_dto(include_addresses=False, include_favorite_couriers= False) for customer in self.regular_customers]
        return dto


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Courier:
        return Courier(
            courier_id=dto_dict.get('courier_id'),
            name=dto_dict.get('name'),
            phone=dto_dict.get('phone')
        )
