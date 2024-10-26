from .general_dao import GeneralDAO
from ..domain import Delivery


class DeliveryDAO(GeneralDAO):
    _domain_type = Delivery
