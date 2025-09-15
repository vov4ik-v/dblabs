from .general_controller import GeneralController
from ..service import order_service
from ..domain.order import Order


class OrderController(GeneralController):
    _service = order_service

    def find_all_orders_with_relations(self) -> list:
        orders = self._service.find_all(Order.customer, Order.address, Order.order_details, Order.order_details)
        return [order.put_into_dto() for order in orders]

    def find_order_with_relations(self, order_id: int) -> dict:
        order = self._service.find_by_id_with_relations(order_id, Order.customer, Order.address, Order.order_details)
        return order.put_into_dto() if order else None

    def calculate_order_total_price(self, operation: str) -> dict:
        result = self._service.calculate_order_total_price(operation)
        return {"result": result}
