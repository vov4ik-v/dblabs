from .general_dao import GeneralDAO
from ..domain import OrderDetail


class OrderDetailDAO(GeneralDAO):
    _domain_type = OrderDetail
