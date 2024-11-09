from .general_service import GeneralService
from ..dao import order_dao

class OrderService(GeneralService):
    _dao = order_dao

    def calculate_order_total_price(self, operation: str) -> float:
        # Викликаємо метод DAO для виконання обчислення
        return self._dao.calculate_order_total_price(operation)
