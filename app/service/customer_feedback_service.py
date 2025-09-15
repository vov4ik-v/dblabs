from typing import Dict, Any, List

from sqlalchemy import text
from .general_service import GeneralService
from ..dao.customer_feedback_dao import CustomerFeedbackDAO
from ..domain.customer_feedback import CustomerFeedback
from app.extensions import db

class CustomerFeedbackService(GeneralService):
    _dao = CustomerFeedbackDAO()

    def create_feedback(self, customer_id: int, feedback_text: str) -> Dict[str, Any]:
        # Викликає збережену процедуру для вставки відгуку
        db.session.execute(
            text("CALL insert_feedback(:customer_id, :feedback_text)"),
            {'customer_id': customer_id, 'feedback_text': feedback_text}
        )
        db.session.commit()

        # Створює об'єкт CustomerFeedback
        feedback = CustomerFeedback(customer_id=customer_id, feedback_text=feedback_text)

        # Повертає об'єкт як DTO, який можна серіалізувати
        return feedback.put_into_dto()

    def get_all_feedbacks(self) -> List[Dict[str, Any]]:
        feedbacks = self._dao.find_all()
        return [feedback.put_into_dto() for feedback in feedbacks]
