from __future__ import annotations
from typing import Dict, Any
from app.extensions import db


class CustomerFeedback(db.Model):
    __tablename__ = 'customer_feedback'

    feedback_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, nullable=False)
    feedback_text = db.Column(db.Text, nullable=False)
    feedback_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def put_into_dto(self) -> Dict[str, Any]:
        """Перетворення об'єкта на DTO-формат."""
        return {
            'feedback_id': self.feedback_id,
            'customer_id': self.customer_id,
            'feedback_text': self.feedback_text,
            'feedback_date': self.feedback_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CustomerFeedback:
        """Створює об'єкт CustomerFeedback із словника DTO."""
        return CustomerFeedback(
            customer_id=dto_dict.get('customer_id'),
            feedback_text=dto_dict.get('feedback_text')
        )
