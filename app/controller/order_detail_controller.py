from .general_controller import GeneralController
from ..service import order_detail_service


class OrderDetailController(GeneralController):
    _service = order_detail_service
