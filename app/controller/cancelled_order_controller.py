from .general_controller import GeneralController
from ..service import cancelled_order_service


class CancelledOrderController(GeneralController):
    _service = cancelled_order_service
