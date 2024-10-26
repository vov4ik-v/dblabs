from .general_service import GeneralService
from ..dao import order_dao


class OrderService(GeneralService):
    _dao = order_dao
