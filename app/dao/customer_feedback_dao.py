from .general_dao import GeneralDAO
from ..domain.customer_feedback import CustomerFeedback

class CustomerFeedbackDAO(GeneralDAO):
    _domain_type = CustomerFeedback

    def find_by_id(self, feedback_id: int) -> CustomerFeedback:
        return CustomerFeedback.query.get(feedback_id)
