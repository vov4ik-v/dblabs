from .general_controller import GeneralController
from ..service import cancelled_order_service
from ..domain.cancelled_order import CancelledOrder

class CancelledOrderController(GeneralController):
    _service = cancelled_order_service

    def find_all_cancelled_orders_with_order(self):
        return self.find_all(CancelledOrder.order)

    def find_cancelled_order_with_order(self, cancelled_order_id: int):
        return self.find_by_id_with_relations(cancelled_order_id, CancelledOrder.order)
