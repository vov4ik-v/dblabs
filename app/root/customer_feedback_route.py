from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controller.customer_feedback_controller import CustomerFeedbackController

# Створення Blueprint для customer_feedback
customer_feedback_bp = Blueprint('customer_feedback', __name__, url_prefix='/customer_feedback')
customer_feedback_controller = CustomerFeedbackController()


@customer_feedback_bp.route('', methods=['POST'])
def create_feedback():
    content = request.get_json()
    customer_id = content.get('customer_id')
    feedback_text = content.get('feedback_text')

    # Викликає метод контролера для створення відгуку
    feedback_dto = customer_feedback_controller.create_feedback(customer_id, feedback_text)

    # Повертаємо DTO замість об'єкта CustomerFeedback
    return make_response(jsonify(feedback_dto), HTTPStatus.CREATED)
