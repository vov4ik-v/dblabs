from .general_controller import GeneralController
from ..service import order_detail_service
from ..domain.order_detail import OrderDetail

class OrderDetailController(GeneralController):
    _service = order_detail_service

    def find_all_order_details_with_relations(self) -> list:
        order_details = self._service.find_all(OrderDetail.product, OrderDetail.addon)
        return [order_detail.put_into_dto() for order_detail in order_details]

    def find_order_detail_with_relations(self, order_detail_id: int) -> dict:
        order_detail = self._service.find_by_id_with_relations(order_detail_id, OrderDetail.product, OrderDetail.addon)
        return order_detail.put_into_dto() if order_detail else None
