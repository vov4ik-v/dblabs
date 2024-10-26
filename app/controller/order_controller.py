from .general_controller import GeneralController
from ..service import order_service


class OrderController(GeneralController):
    _service = order_service
