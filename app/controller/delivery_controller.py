from .general_controller import GeneralController
from ..service import delivery_service
from ..domain.delivery import Delivery

class DeliveryController(GeneralController):
    _service = delivery_service

    def find_all_deliveries_with_relations(self) -> list:
        deliveries = self._service.find_all(Delivery.order, Delivery.courier)
        return [delivery.put_into_dto() for delivery in deliveries]

    def find_delivery_with_relations(self, delivery_id: int) -> dict:
        delivery = self._service.find_by_id_with_relations(delivery_id, Delivery.order, Delivery.courier)
        return delivery.put_into_dto() if delivery else None
