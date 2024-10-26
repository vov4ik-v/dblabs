from .general_service import GeneralService
from ..dao import order_detail_dao


class OrderDetailService(GeneralService):
    _dao = order_detail_dao
