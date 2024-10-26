from .general_dao import GeneralDAO
from ..domain import Courier


class CourierDAO(GeneralDAO):
    _domain_type = Courier
