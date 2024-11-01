from __future__ import annotations
from typing import Dict, Any
from app import db

class CancelledOrder(db.Model):
    __tablename__ = 'cancelled_order'

    cancelled_order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    cancel_reason = db.Column(db.String(255), nullable=False)
    cancel_date = db.Column(db.String(50), nullable=False)

    order = db.relationship('Order', back_populates='cancelled_order')

    def __init__(self, order_id: int, cancel_reason: str, cancel_date: str, cancelled_order_id: int = None):
        self.cancelled_order_id = cancelled_order_id
        self.order_id = order_id
        self.cancel_reason = cancel_reason
        self.cancel_date = cancel_date

    def __repr__(self) -> str:
        return f"CancelledOrder({self.cancelled_order_id}, {self.order_id}, '{self.cancel_reason}', '{self.cancel_date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'cancelled_order_id': self.cancelled_order_id,
            'cancel_reason': self.cancel_reason,
            'cancel_date': self.cancel_date,
            'order': self.order.put_into_dto(detailed=False) if self.order else None  # Використовуємо `detailed=False`
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CancelledOrder:
        return CancelledOrder(
            cancelled_order_id=dto_dict.get('cancelled_order_id'),
            order_id=dto_dict.get('order_id'),
            cancel_reason=dto_dict.get('cancel_reason'),
            cancel_date=dto_dict.get('cancel_date')
        )

