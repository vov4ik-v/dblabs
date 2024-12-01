from typing import Dict, Any, List

from .general_controller import GeneralController
from ..service.customer_feedback_service import CustomerFeedbackService
from ..domain.customer_feedback import CustomerFeedback

class CustomerFeedbackController(GeneralController):
    _service = CustomerFeedbackService()

    def create_feedback(self, customer_id: int, feedback_text: str) -> Dict[str, Any]:
        feedback_dto = self._service.create_feedback(customer_id, feedback_text)
        return feedback_dto  # Повертає DTO

    def get_all_feedbacks(self) -> List[Dict[str, Any]]:
        return self._service.get_all_feedbacks()
