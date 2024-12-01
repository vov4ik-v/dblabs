from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controller.customer_feedback_controller import CustomerFeedbackController

customer_feedback_bp = Blueprint('customer_feedback', __name__, url_prefix='/customer_feedback')
customer_feedback_controller = CustomerFeedbackController()


@customer_feedback_bp.route('', methods=['POST'])
def create_feedback():
    content = request.get_json()
    customer_id = content.get('customer_id')
    feedback_text = content.get('feedback_text')

    feedback_dto = customer_feedback_controller.create_feedback(customer_id, feedback_text)

    return make_response(jsonify(feedback_dto), HTTPStatus.CREATED)

@customer_feedback_bp.route('', methods=['GET'])
def get_all_feedbacks():
    feedbacks = customer_feedback_controller.get_all_feedbacks()
    return make_response(jsonify(feedbacks), HTTPStatus.OK)
