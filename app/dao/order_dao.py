from .general_dao import GeneralDAO
from ..domain import Order


class OrderDAO(GeneralDAO):
    _domain_type = Order
