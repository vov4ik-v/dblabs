from .general_service import GeneralService
from ..dao import cancelled_order_dao


class CancelledOrderService(GeneralService):
    _dao = cancelled_order_dao
